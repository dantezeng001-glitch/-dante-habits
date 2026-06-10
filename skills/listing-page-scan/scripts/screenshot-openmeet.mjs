import puppeteer from 'puppeteer-core';
import sharp from 'sharp';
import path from 'path';
import fs from 'fs';
import os from 'os';

const TARGET_URL = 'https://shokz.com/pages/product-comparison';
const SWITCH_COL = parseInt(process.argv[2] || '1', 10); // which column to switch (1/2/3)
const SWITCH_HANDLE = 'openmeet';

function findDesktop() {
  const home = os.homedir();
  for (const c of [path.join(home, 'OneDrive', 'Desktop'), path.join(home, 'Desktop')]) {
    if (fs.existsSync(c)) return c;
  }
  return home;
}
const OUTPUT_DIR = process.argv[3] || findDesktop();
const VIEWPORT_WIDTH = 1440;
const VIEWPORT_HEIGHT = 900;

function findBrowser() {
  const candidates = [
    process.env.CHROME_PATH, process.env.EDGE_PATH,
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  ].filter(Boolean);
  for (const p of candidates) if (fs.existsSync(p)) return p;
  throw new Error('No Chromium-based browser found.');
}

async function autoScroll(page) {
  await page.evaluate(async () => {
    const distance = 400, delay = 300;
    let cur = 0, lastHeight = document.body.scrollHeight;
    while (true) {
      window.scrollBy(0, distance); cur += distance;
      await new Promise(r => setTimeout(r, delay));
      const nh = document.body.scrollHeight;
      if (cur >= nh) { if (nh === lastHeight) break; lastHeight = nh; }
    }
    window.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 1000));
  });
}

async function waitForImages(page) {
  await page.evaluate(async () => {
    const imgs = Array.from(document.querySelectorAll('img'));
    await Promise.allSettled(imgs.filter(i => !i.complete).map(i => new Promise(res => {
      i.addEventListener('load', res, { once: true });
      i.addEventListener('error', res, { once: true });
      setTimeout(res, 8000);
    })));
  });
}

async function dismissPopups(page) {
  await new Promise(r => setTimeout(r, 3000));
  const n = await page.evaluate(() => {
    let c = 0;
    document.querySelectorAll('*').forEach(el => {
      try {
        const s = getComputedStyle(el);
        if (s.position !== 'fixed') return;
        if (s.display === 'none' || s.visibility === 'hidden') return;
        const r = el.getBoundingClientRect();
        const covers = r.width > innerWidth * 0.5 && r.height > innerHeight * 0.5;
        const overlay = s.zIndex && parseInt(s.zIndex) > 999;
        if (covers || overlay) { el.style.display = 'none'; c++; }
      } catch (_) {}
    });
    return c;
  });
  console.log(`  Removed ${n} overlay(s)`);
  await new Promise(r => setTimeout(r, 500));
}

async function switchColumn(page, col, handle) {
  const res = await page.evaluate((col, handle) => {
    const c = document.querySelector(`.item-inner-${col}.compare-col-${col}`);
    if (!c) return `column ${col} not found`;
    const wrap = c.querySelector('.select-wrapper');
    if (!wrap) return 'select-wrapper not found';
    const t = wrap.querySelector(`.s-item[data-handle="${handle}"]`);
    if (!t) return `option ${handle} not found`;
    t.click();
    return 'ok';
  }, col, handle);
  await new Promise(r => setTimeout(r, 2500));
  const label = await page.evaluate((col) => {
    const c = document.querySelector(`.item-inner-${col}.compare-col-${col}`);
    const b = c.querySelector('.content.active .swatch-active b');
    return b ? b.textContent.trim() : '(unknown)';
  }, col);
  return { res, label };
}

async function neutralize(page) {
  await page.evaluate(() => {
    const st = document.createElement('style');
    st.textContent = `*,*::before,*::after{animation-duration:1ms!important;animation-delay:-1ms!important;animation-play-state:paused!important;transition-duration:0s!important;transition-delay:0s!important;}`;
    document.head.appendChild(st);
    document.querySelectorAll('*').forEach(el => {
      try {
        const s = getComputedStyle(el);
        if (el.tagName === 'HTML' || el.tagName === 'BODY') return;
        if (s.position === 'fixed') el.style.display = 'none';
        else if (s.position === 'sticky') el.style.position = 'relative';
      } catch (_) {}
    });
  });
}

async function scrollAndCapture(page) {
  const total = await page.evaluate(() => document.body.scrollHeight);
  const chunks = [];
  let y = 0;
  console.log(`  Page height: ${total}px -> ${Math.ceil(total / VIEWPORT_HEIGHT)} slices`);
  while (y < total) {
    await page.evaluate(yy => window.scrollTo(0, yy), y);
    await new Promise(r => setTimeout(r, 400));
    const buf = await page.screenshot({ type: 'png' });
    if (y + VIEWPORT_HEIGHT > total) {
      const overlap = y + VIEWPORT_HEIGHT - total;
      const m = await sharp(buf).metadata();
      const cropTop = Math.round(overlap * (m.height / VIEWPORT_HEIGHT));
      chunks.push(await sharp(buf).extract({ left: 0, top: cropTop, width: m.width, height: m.height - cropTop }).toBuffer());
    } else chunks.push(buf);
    y += VIEWPORT_HEIGHT;
  }
  console.log(`  Captured ${chunks.length} chunks.`);
  return chunks;
}

async function stitch(chunks, out) {
  const metas = await Promise.all(chunks.map(c => sharp(c).metadata()));
  const w = metas[0].width;
  const h = metas.reduce((s, m) => s + m.height, 0);
  console.log(`  Stitching -> ${w} x ${h} px`);
  const comps = [];
  let off = 0;
  for (let i = 0; i < chunks.length; i++) { comps.push({ input: chunks[i], left: 0, top: off }); off += metas[i].height; }
  await sharp({ create: { width: w, height: h, channels: 4, background: { r: 255, g: 255, b: 255, alpha: 1 } } }).composite(comps).png().toFile(out);
}

(async () => {
  const bp = findBrowser();
  console.log(`URL:     ${TARGET_URL}`);
  console.log(`Switch:  column ${SWITCH_COL} -> ${SWITCH_HANDLE}`);
  console.log(`Browser: ${path.basename(bp)}`);
  console.log(`Output:  ${OUTPUT_DIR}`);
  const browser = await puppeteer.launch({
    executablePath: bp, headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', `--window-size=${VIEWPORT_WIDTH},${VIEWPORT_HEIGHT}`],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: VIEWPORT_WIDTH, height: VIEWPORT_HEIGHT, deviceScaleFactor: 1 });
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36');

  console.log('Loading...');
  try { await page.goto(TARGET_URL, { waitUntil: 'networkidle2', timeout: 60000 }); } catch (e) { console.log('Load timed out, continuing...'); }

  console.log('Dismissing popups...');
  await dismissPopups(page);

  console.log(`Switching column ${SWITCH_COL} to OpenMeet...`);
  const sw = await switchColumn(page, SWITCH_COL, SWITCH_HANDLE);
  console.log(`  switch=${sw.res}, column now shows: ${sw.label}`);
  if (sw.label.toLowerCase().indexOf('openmeet') === -1) {
    console.log('  WARNING: column did not switch to OpenMeet!');
  }

  console.log('Scrolling for lazy content...');
  await autoScroll(page);
  console.log('Waiting for images...');
  await waitForImages(page);
  await new Promise(r => setTimeout(r, 2000));

  console.log('Neutralizing fixed/sticky...');
  await neutralize(page);
  await new Promise(r => setTimeout(r, 500));

  console.log('Capturing...');
  const chunks = await scrollAndCapture(page);

  const filename = `screenshot-product-comparison-openmeet-col${SWITCH_COL}.png`;
  const out = path.join(OUTPUT_DIR, filename);
  console.log('Stitching...');
  await stitch(chunks, out);
  const stats = fs.statSync(out);
  console.log(`\nDone -> ${out}  (${(stats.size / 1024 / 1024).toFixed(2)} MB)`);
  await browser.close();
})();
