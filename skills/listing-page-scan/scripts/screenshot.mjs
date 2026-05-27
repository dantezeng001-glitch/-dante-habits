import puppeteer from 'puppeteer-core';
import sharp from 'sharp';
import path from 'path';
import fs from 'fs';
import os from 'os';

const TARGET_URL = process.argv[2] || '';

function findDesktop() {
  const home = os.homedir();
  const candidates = [
    path.join(home, 'OneDrive', 'Desktop'),
    path.join(home, 'OneDrive - *', 'Desktop'),
    path.join(home, 'Desktop'),
  ];
  for (const c of candidates) {
    if (fs.existsSync(c)) return c;
  }
  return home;
}

const OUTPUT_DIR = process.argv[3] || findDesktop();
const VIEWPORT_WIDTH = 1440;
const VIEWPORT_HEIGHT = 900;

if (!TARGET_URL) {
  console.error('Usage: node screenshot.mjs <URL> [output_dir]');
  process.exit(1);
}

function findBrowser() {
  const candidates = [
    process.env.CHROME_PATH,
    process.env.EDGE_PATH,
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium-browser',
    '/usr/bin/microsoft-edge',
  ].filter(Boolean);

  for (const p of candidates) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error('No Chromium-based browser found. Set CHROME_PATH or EDGE_PATH env var.');
}

async function autoScroll(page) {
  await page.evaluate(async () => {
    const distance = 400;
    const delay = 300;
    let currentPosition = 0;
    let lastHeight = document.body.scrollHeight;
    while (true) {
      window.scrollBy(0, distance);
      currentPosition += distance;
      await new Promise(r => setTimeout(r, delay));
      const newHeight = document.body.scrollHeight;
      if (currentPosition >= newHeight) {
        if (newHeight === lastHeight) break;
        lastHeight = newHeight;
      }
    }
    window.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 1000));
  });
}

async function waitForImages(page) {
  await page.evaluate(async () => {
    const images = Array.from(document.querySelectorAll('img'));
    await Promise.allSettled(
      images.filter(img => !img.complete).map(img =>
        new Promise(resolve => {
          img.addEventListener('load', resolve, { once: true });
          img.addEventListener('error', resolve, { once: true });
          setTimeout(resolve, 8000);
        })
      )
    );
  });
}

async function dismissPopups(page) {
  await new Promise(r => setTimeout(r, 3000));
  const dismissed = await page.evaluate(() => {
    let count = 0;
    document.querySelectorAll('*').forEach(el => {
      try {
        const style = getComputedStyle(el);
        if (style.position !== 'fixed') return;
        if (style.display === 'none' || style.visibility === 'hidden') return;
        const rect = el.getBoundingClientRect();
        const coversScreen = rect.width > window.innerWidth * 0.5 && rect.height > window.innerHeight * 0.5;
        const isOverlay = style.zIndex && parseInt(style.zIndex) > 999;
        if (coversScreen || isOverlay) {
          el.style.display = 'none';
          count++;
        }
      } catch (_) {}
    });
    return count;
  });
  console.log(`  Removed ${dismissed} overlay(s)`);
  await new Promise(r => setTimeout(r, 500));
}

async function expandCollapsed(page) {
  await page.evaluate(async () => {
    const triggers = [
      'view more', 'show more', 'read more', 'see more',
      '查看更多', '展开更多', '显示更多',
    ];
    const candidates = document.querySelectorAll(
      'button, a, [role="button"], summary, span, div'
    );
    for (const el of candidates) {
      try {
        const text = (el.textContent || '').trim().toLowerCase();
        const match = triggers.some(t => text === t || text.startsWith(t));
        if (match && el.offsetParent !== null && typeof el.click === 'function') {
          el.click();
          await new Promise(r => setTimeout(r, 800));
        }
      } catch (_) {}
    }
  });
  await new Promise(r => setTimeout(r, 1000));
}

async function neutralizeFixedAndSticky(page) {
  await page.evaluate(() => {
    const freezeStyle = document.createElement('style');
    freezeStyle.textContent = `
      *, *::before, *::after {
        animation-delay: -1ms !important;
        animation-duration: 1ms !important;
        animation-play-state: paused !important;
        transition-delay: 0s !important;
        transition-duration: 0s !important;
      }
    `;
    document.head.appendChild(freezeStyle);

    document.querySelectorAll('*').forEach(el => {
      try {
        const style = getComputedStyle(el);
        if (el.tagName === 'HTML' || el.tagName === 'BODY') return;
        if (style.position === 'fixed') {
          el.style.display = 'none';
        } else if (style.position === 'sticky') {
          el.style.position = 'relative';
        }
      } catch (_) {}
    });
  });
}

async function scrollAndCapture(page) {
  const totalHeight = await page.evaluate(() => document.body.scrollHeight);
  const chunks = [];
  let scrollY = 0;

  console.log(`  Page height: ${totalHeight}px → ${Math.ceil(totalHeight / VIEWPORT_HEIGHT)} slices`);

  while (scrollY < totalHeight) {
    await page.evaluate(y => window.scrollTo(0, y), scrollY);
    await new Promise(r => setTimeout(r, 400));

    const buf = await page.screenshot({ type: 'png', encoding: 'binary' });

    if (scrollY + VIEWPORT_HEIGHT > totalHeight) {
      const overlap = scrollY + VIEWPORT_HEIGHT - totalHeight;
      const meta = await sharp(buf).metadata();
      const cropTop = Math.round(overlap * (meta.height / VIEWPORT_HEIGHT));
      chunks.push(
        await sharp(buf)
          .extract({ left: 0, top: cropTop, width: meta.width, height: meta.height - cropTop })
          .toBuffer()
      );
    } else {
      chunks.push(buf);
    }

    const pct = Math.min(100, Math.round((scrollY + VIEWPORT_HEIGHT) / totalHeight * 100));
    process.stdout.write(`  ${pct}%\r`);
    scrollY += VIEWPORT_HEIGHT;
  }

  console.log(`  Captured ${chunks.length} chunks.`);
  return chunks;
}

async function stitchVertically(chunks, outputPath) {
  const metas = await Promise.all(chunks.map(c => sharp(c).metadata()));
  const totalWidth = metas[0].width;
  const totalHeight = metas.reduce((sum, m) => sum + m.height, 0);

  console.log(`  Stitching → ${totalWidth} × ${totalHeight} px`);

  const composites = [];
  let offsetY = 0;
  for (let i = 0; i < chunks.length; i++) {
    composites.push({ input: chunks[i], left: 0, top: offsetY });
    offsetY += metas[i].height;
  }

  await sharp({
    create: {
      width: totalWidth,
      height: totalHeight,
      channels: 4,
      background: { r: 255, g: 255, b: 255, alpha: 1 },
    },
  })
    .composite(composites)
    .png()
    .toFile(outputPath);
}

// ── Main ──

(async () => {
  const browserPath = findBrowser();
  console.log(`URL:     ${TARGET_URL}`);
  console.log(`Browser: ${path.basename(browserPath)}`);
  console.log(`Output:  ${OUTPUT_DIR}`);

  const browser = await puppeteer.launch({
    executablePath: browserPath,
    headless: true,
    args: [
      '--no-sandbox', '--disable-setuid-sandbox',
      '--disable-dev-shm-usage', '--disable-gpu',
      `--window-size=${VIEWPORT_WIDTH},${VIEWPORT_HEIGHT}`,
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: VIEWPORT_WIDTH, height: VIEWPORT_HEIGHT, deviceScaleFactor: 1 });
  await page.setUserAgent(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
  );

  console.log('Loading...');
  try {
    await page.goto(TARGET_URL, { waitUntil: 'networkidle2', timeout: 60000 });
  } catch (e) {
    console.log('Load timed out, continuing...');
  }

  console.log('Dismissing popups...');
  await dismissPopups(page);

  console.log('Expanding collapsed sections...');
  await expandCollapsed(page);

  console.log('Scrolling for lazy content...');
  await autoScroll(page);

  console.log('Waiting for images...');
  await waitForImages(page);
  await new Promise(r => setTimeout(r, 2000));

  console.log('Neutralizing fixed/sticky...');
  await neutralizeFixedAndSticky(page);
  await new Promise(r => setTimeout(r, 500));

  console.log('Capturing...');
  const chunks = await scrollAndCapture(page);

  const slug = new URL(TARGET_URL).pathname.replace(/\//g, '-').replace(/^-|-$/g, '') || 'page';
  const filename = `screenshot-${slug}.png`;
  const outputPath = path.join(OUTPUT_DIR, filename);

  console.log('Stitching...');
  await stitchVertically(chunks, outputPath);

  const stats = fs.statSync(outputPath);
  console.log(`\nDone → ${outputPath}  (${(stats.size / 1024 / 1024).toFixed(2)} MB)`);

  await browser.close();
})();
