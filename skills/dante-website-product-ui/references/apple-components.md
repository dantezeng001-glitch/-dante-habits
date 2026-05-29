# Apple Product Page — Component Library

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。

---

## 1. Hero（营销页）

全屏居中，深色背景，产品图悬浮。不放 CTA 按钮。

```html
<section class="hero">
    <div class="hero-content">
        <h1>AirPods Max 2</h1>
        <h2 class="hero-tagline">Listening. Remastered.</h2>
    </div>
    <div class="hero-image">[Image: product floating on dark background]</div>
</section>
```

```css
.hero {
    min-height: 100vh; display: flex; flex-direction: column;
    align-items: center; justify-content: center; text-align: center;
    background: var(--color-bg-dark); color: var(--color-text-primary-dark);
    overflow: hidden; position: relative;
}
.hero-content { position: relative; z-index: 2; padding: 60px var(--padding-inline); }
.hero h1 { font-size: var(--font-size-h1); font-weight: 700; margin-bottom: 8px; }
.hero-tagline { font-size: var(--font-size-h2); font-weight: 600; color: var(--color-text-secondary-dark); }
.hero-image {
    width: 100%; max-width: 800px; aspect-ratio: 4/3;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--color-text-secondary-dark); margin-top: 40px;
}
```

---

## 2. Feature Ticker

Hero 下方纯文字快速扫读列表，5-6 项垂直堆叠。

```html
<section class="section--dark ticker-section">
    <div class="container-narrow">
        <ul class="ticker-list">
            <li>Up to 1.5x more Active Noise Cancellation.<sup>1</sup></li>
            <li>Improved high-fidelity sound.</li>
            <li>New intelligent features: Live Translation.<sup>2</sup></li>
            <li>Over-ear design in five vibrant colors.</li>
        </ul>
    </div>
</section>
```

```css
.ticker-section { padding: var(--section-gap) 0; }
.ticker-list { list-style: none; max-width: var(--max-width-text); margin: 0 auto; }
.ticker-list li {
    font-size: var(--font-size-body); line-height: 1.6; padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.ticker-list sup { font-size: 0.6em; vertical-align: super; }
```

---

## 3. Deep-Dive Section（深浅交替特性区块）

```html
<section class="section--dark">
    <div class="container">
        <div class="split">
            <div class="split-text">
                <h2>Superior sound down to a science.</h2>
                <h3>Custom acoustic architecture</h3>
                <p>Body paragraph with technical details wrapped in aspirational narrative.</p>
            </div>
            <div class="split-visual">[Image: product detail close-up]</div>
        </div>
    </div>
</section>
```

```css
.section--dark { background: var(--color-bg-dark); color: var(--color-text-primary-dark); padding: var(--section-gap) 0; }
.section--dark p { color: var(--color-text-secondary-dark); }
.section--light { background: var(--color-bg-light); color: var(--color-text-primary-light); padding: var(--section-gap) 0; }
.section--light p { color: var(--color-text-secondary-light); }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.split-text h2 { font-size: var(--font-size-h2); font-weight: 600; margin-bottom: 16px; line-height: 1.1; }
.split-text h3 { font-size: var(--font-size-h3); font-weight: 600; margin-bottom: 12px; line-height: 1.15; }
.split-text p { font-size: var(--font-size-body); line-height: 1.5; margin-bottom: 16px; max-width: var(--max-width-text); }
.split-visual {
    border-radius: var(--radius-card); aspect-ratio: 4/3;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--color-text-secondary-dark); padding: 24px;
}
```

---

## 4. Data Callout Row

超大数字水平排列，用于电池/性能数据。

```html
<div class="data-callouts">
    <div class="callout">
        <div class="callout-number">30<span class="callout-unit">hrs</span></div>
        <div class="callout-label">Listening time<sup>1</sup></div>
    </div>
    <div class="callout">
        <div class="callout-number">5<span class="callout-unit">hrs</span></div>
        <div class="callout-label">From just 5 minutes of charge</div>
    </div>
</div>
```

```css
.data-callouts { display: flex; justify-content: center; gap: 80px; padding: 48px 0; }
.callout { text-align: center; }
.callout-number { font-size: var(--font-size-stat); font-weight: 700; line-height: 1; }
.callout-unit { font-size: 0.4em; font-weight: 600; }
.callout-label { font-size: 14px; margin-top: 8px; }
.section--dark .callout-label { color: var(--color-text-secondary-dark); }
.section--light .callout-label { color: var(--color-text-secondary-light); }
```

---

## 5. Tab Switcher

水平标签切换内容区。

```html
<div class="tabs">
    <div class="tab-bar">
        <button class="tab active">Live Translation</button>
        <button class="tab">Controls</button>
        <button class="tab">Siri</button>
        <button class="tab">Connectivity</button>
    </div>
    <div class="tab-panel active">
        <h4>Live Translation</h4>
        <p>Tab content paragraph describing feature.</p>
    </div>
</div>
```

```css
.tab-bar { display: flex; gap: 32px; justify-content: center; margin-bottom: 32px; }
.tab {
    background: none; border: none; font-size: 16px; font-weight: 500;
    color: var(--color-text-secondary-dark); cursor: pointer; padding: 8px 0;
    border-bottom: 2px solid transparent; transition: var(--transition-quick);
}
.tab.active { color: var(--color-text-primary-dark); border-bottom-color: var(--color-text-primary-dark); }
.tab-panel { max-width: var(--max-width-text); margin: 0 auto; }
.tab-panel h4 { font-size: var(--font-size-h4); font-weight: 600; margin-bottom: 12px; }
```

---

## 6. Purchase Guide Modules

4-5 个服务卡片水平排列。

```html
<section class="section--light">
    <div class="container">
        <div class="service-grid">
            <div class="service-card">
                <div class="service-icon">[Icon: engraving]</div>
                <h3>Make them yours.</h3>
                <p>Personalize your AirPods for free.</p>
            </div>
            <!-- repeat 3-4 more -->
        </div>
    </div>
</section>
```

```css
.service-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; }
.service-card { text-align: center; padding: 32px 20px; }
.service-icon { font-size: 32px; margin-bottom: 16px; }
.service-card h3 { font-size: 17px; font-weight: 600; margin-bottom: 8px; }
.service-card p { font-size: 14px; color: var(--color-text-secondary-light); }
```

---

## 7. Compare Table

```html
<section class="section--light">
    <div class="container">
        <h2 class="section-title">Compare</h2>
        <table class="compare-table">
            <thead>
                <tr>
                    <th></th>
                    <th><span class="compare-badge">Currently viewing</span>[Product A]</th>
                    <th>[Product B]</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Active Noise Cancellation</td><td>Up to 1.5x</td><td>Yes</td></tr>
                <tr><td>Battery Life</td><td class="compare-stat">20 hrs</td><td>6 hrs</td></tr>
            </tbody>
        </table>
        <a href="#" class="link-arrow">Compare all models</a>
    </div>
</section>
```

```css
.section-title { text-align: center; font-size: var(--font-size-h2); font-weight: 600; margin-bottom: 48px; }
.compare-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.compare-table th, .compare-table td { padding: 16px 20px; text-align: center; border-bottom: 1px solid var(--color-border); }
.compare-table th { font-weight: 600; vertical-align: bottom; padding-bottom: 24px; }
.compare-badge {
    display: block; font-size: 11px; color: var(--color-link-light);
    margin-bottom: 8px; font-weight: 400;
}
.compare-stat { font-size: 28px; font-weight: 700; }
.link-arrow { color: var(--color-link-light); text-decoration: none; font-size: 17px; display: inline-block; margin-top: 24px; }
.link-arrow::after { content: " >"; }
```

---

## 8. Horizontal Scroll Shelf（购买页专用）

```html
<section class="shelf-section">
    <div class="container">
        <h2 class="shelf-title">All Models</h2>
        <div class="shelf">
            <div class="shelf-card">
                <span class="shelf-badge">NEW</span>
                <div class="shelf-card-image">[Product Image]</div>
                <h3>AirPods Max 2</h3>
                <p class="shelf-card-desc">Take a closer look</p>
                <p class="shelf-card-price">From $549 or $45.75/mo. for 12 mo.</p>
                <a href="#" class="btn-primary">Buy</a>
            </div>
            <!-- more shelf-card -->
        </div>
    </div>
</section>
```

```css
.shelf-section { padding: var(--section-gap) 0; background: var(--color-bg-light); }
.shelf-title { font-size: var(--font-size-h2); font-weight: 600; margin-bottom: 32px; }
.shelf {
    display: flex; gap: 20px; overflow-x: auto;
    scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch;
    padding-bottom: 16px;
}
.shelf-card {
    flex: 0 0 calc(33.333% - 14px); scroll-snap-align: start;
    border-radius: var(--radius-card); background: var(--color-bg-white);
    padding: 30px; text-align: center;
}
.shelf-badge {
    display: inline-block; font-size: 11px; font-weight: 600;
    color: #bf4800; background: #fef0e5; padding: 4px 10px; border-radius: 4px;
}
.shelf-card-image { aspect-ratio: 1; margin: 24px 0; }
.shelf-card h3 { font-size: 21px; font-weight: 600; margin-bottom: 4px; }
.shelf-card-desc { font-size: 14px; color: var(--color-text-secondary-light); margin-bottom: 12px; }
.shelf-card-price { font-size: 14px; color: var(--color-text-secondary-light); margin-bottom: 20px; }
```

---

## 9. Footnotes

```html
<section class="footnotes">
    <div class="container-narrow">
        <ol class="footnote-list">
            <li id="fn1">Testing conducted by Apple in March 2026 using pre-production units...</li>
            <li id="fn2">Live Translation requires iOS 19 or later...</li>
        </ol>
    </div>
</section>
```

```css
.footnotes { padding: 40px 0; border-top: 1px solid var(--color-border); }
.footnote-list { padding-left: 20px; }
.footnote-list li { font-size: var(--font-size-caption); color: var(--color-footnote); line-height: 1.5; margin-bottom: 8px; }
```

---

## 10. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--color-text-primary-light); line-height: 1.5; -webkit-font-smoothing: antialiased; }
.container { max-width: var(--max-width-content); margin: 0 auto; padding: 0 var(--padding-inline); }
.container-narrow { max-width: var(--max-width-text); margin: 0 auto; padding: 0 var(--padding-inline); }
.btn-primary {
    display: inline-block; padding: 12px 24px;
    border-radius: var(--radius-button); background: var(--color-btn-primary);
    color: #fff; font-size: 17px; font-weight: 400;
    text-decoration: none; transition: background var(--transition-quick);
    border: none; cursor: pointer;
}
.btn-primary:hover { background: var(--color-btn-primary-hover); }
.link-blue { color: var(--color-link-light); text-decoration: none; font-size: 17px; }
.link-blue:hover { text-decoration: underline; }
.link-blue::after { content: " >"; }
```
