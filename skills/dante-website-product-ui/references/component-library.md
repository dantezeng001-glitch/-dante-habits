# Shokz Product Page — Component Library

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。
使用时整段复制到页面骨架中，只改文字内容和图片占位符。

---

## 1. Hero-Detail（产品详情页 hero）

全宽居中排列：产品名 + tagline + 价格 + CTA。用于 `/pages/` 类型页面。

```html
<section class="hero-detail">
    <div class="container">
        <h1>PRODUCT NAME</h1>
        <p class="hero-tagline">Tagline. One Sentence.</p>
        <p class="hero-price">$XX.XX</p>
        <a href="#" class="btn-primary">Shop Now</a>
    </div>
</section>
```

```css
.hero-detail {
    padding: 100px 0 60px;
    text-align: center;
    background: var(--white);
}
.hero-detail h1 { font-size: 48px; font-weight: 700; margin-bottom: 12px; text-transform: uppercase; }
.hero-tagline { font-size: 20px; color: var(--mid-gray); margin-bottom: 16px; }
.hero-price { font-size: 28px; font-weight: 700; margin-bottom: 32px; }
```

---

## 2. Hero-Purchase（购买页 hero）

左右双栏：左侧图片区 / 右侧购买信息。用于 `/products/` 类型页面。

```html
<section class="hero">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-image">[Product Image — Hero Shot]</div>
            <div class="hero-info">
                <h1>PRODUCT NAME</h1>
                <p class="hero-slogan">Tagline Sentence.</p>
                <p class="hero-price">$XX.XX</p>
                <ul class="hero-bullets">
                    <li>Core selling point 1</li>
                    <li>Core selling point 2</li>
                    <li>Core selling point 3</li>
                    <li>Core selling point 4</li>
                </ul>
                <!-- Color selector placeholder -->
                <div class="color-selector">[Color: Black / White]</div>
                <a href="#" class="btn-primary">Add to Cart</a>
            </div>
        </div>
    </div>
</section>
```

```css
.hero { padding: 60px 0; background: var(--white); }
.hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.hero-image {
    background: var(--light-gray); border-radius: 16px; aspect-ratio: 1;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--mid-gray);
}
.hero-info h1 { font-size: 36px; font-weight: 700; margin-bottom: 8px; text-transform: uppercase; }
.hero-slogan { font-size: 18px; color: var(--mid-gray); margin-bottom: 24px; }
.hero-price { font-size: 28px; font-weight: 700; margin-bottom: 24px; }
.hero-bullets { list-style: none; margin-bottom: 32px; }
.hero-bullets li {
    padding: 6px 0 6px 20px; position: relative; font-size: 15px;
}
.hero-bullets li::before {
    content: "•"; position: absolute; left: 0; color: var(--accent); font-weight: bold;
}
```

---

## 3. Highlight-Strip

黑底白字横条，展示 6-7 个核心数据/卖点缩写。

```html
<section class="highlight-strip">
    <div class="container">
        <div class="highlight-items">
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
            <div class="highlight-item"><strong>KEY DATA</strong>Label text</div>
        </div>
    </div>
</section>
```

```css
.highlight-strip { background: var(--black); color: var(--white); padding: 20px 0; overflow: hidden; }
.highlight-items { display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; }
.highlight-item { text-align: center; font-size: 13px; font-weight: 500; letter-spacing: 0.5px; white-space: nowrap; }
.highlight-item strong { display: block; font-size: 15px; margin-bottom: 2px; }
```

---

## 4. Feature-Section（图文双栏）

标准的图文交替 section。`.reverse` 类翻转图文左右位置。

```html
<section class="feature-section">
    <div class="container">
        <div class="feature-content">  <!-- add class="reverse" for alternating -->
            <div class="feature-text">
                <h2>Headline.<br>Benefit Statement.</h2>
                <p>Body paragraph describing the feature and its user value.</p>
            </div>
            <div class="feature-visual">[Image: description]</div>
        </div>
    </div>
</section>
```

```css
.feature-section { padding: var(--section-padding); }
.feature-section:nth-child(even) { background: var(--light-gray); }
.feature-content { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.feature-content.reverse { direction: rtl; }
.feature-content.reverse > * { direction: ltr; }
.feature-text h2 { font-size: 32px; font-weight: 700; margin-bottom: 16px; line-height: 1.2; }
.feature-text p { font-size: 16px; color: var(--mid-gray); line-height: 1.7; margin-bottom: 16px; }
.feature-visual {
    background: var(--light-gray); border-radius: 16px; aspect-ratio: 4/3;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--mid-gray); text-align: center; padding: 24px;
}
.feature-section:nth-child(even) .feature-visual { background: var(--white); }
```

---

## 5. Feature-Section-with-Stats

图文双栏 + 下方 3 列 stat cards。用于需要突出数据的 section（续航、降噪等）。

```html
<section class="feature-section">
    <div class="container">
        <div class="feature-content">
            <div class="feature-text">
                <h2>Headline.</h2>
                <p>Body text.</p>
            </div>
            <div class="feature-visual">[Image]</div>
        </div>
        <div class="stats-row">
            <div class="stat-card">
                <div class="number">99.4%*</div>
                <div class="label">Description of stat</div>
            </div>
            <div class="stat-card">
                <div class="number">42 dB*</div>
                <div class="label">Description of stat</div>
            </div>
            <div class="stat-card">
                <div class="number">AI</div>
                <div class="label">Description of stat</div>
            </div>
        </div>
    </div>
</section>
```

```css
.stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 32px; }
.stat-card { text-align: center; padding: 24px 16px; background: var(--white); border-radius: 12px; }
.stat-card .number { font-size: 36px; font-weight: 800; }
.stat-card .label { font-size: 13px; color: var(--mid-gray); margin-top: 4px; }
```

---

## 6. Feature-Grid-6（Designed Around You）

3×2 卡片网格，用于放置辅助卖点。

```html
<section class="grid-section">
    <div class="container">
        <h2>Designed Around You</h2>
        <div class="feature-grid">
            <div class="grid-card">
                <h3>Feature Name</h3>
                <p>Short description of this feature.</p>
            </div>
            <!-- repeat 5 more grid-card -->
        </div>
    </div>
</section>
```

```css
.grid-section { padding: var(--section-padding); background: var(--white); }
.grid-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.grid-card { text-align: center; padding: 32px 24px; background: var(--light-gray); border-radius: 16px; }
.grid-card h3 { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.grid-card p { font-size: 14px; color: var(--mid-gray); line-height: 1.5; }
```

---

## 7. Compare-Table

双列或三列产品对比表，含 NEW badge。

```html
<section class="compare-section">
    <div class="container">
        <h2>Which Product Is Right For You?</h2>
        <table class="compare-table">
            <thead>
                <tr>
                    <th></th>
                    <th>NEW PRODUCT <span class="badge-new">NEW</span></th>
                    <th>PREVIOUS PRODUCT</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Technology</td><td>New Tech</td><td>Old Tech</td></tr>
                <tr><td>Battery Life</td><td>XX hours</td><td>XX hours</td></tr>
                <tr><td>Quick Charge</td><td>X min = X hrs</td><td>X min = X hrs</td></tr>
                <tr><td>Water Resistance</td><td>IPXX</td><td>IPXX</td></tr>
                <tr><td>Weight</td><td>XX g</td><td>XX g</td></tr>
                <tr><td>Charging Port</td><td>USB-C</td><td>USB-C</td></tr>
            </tbody>
        </table>
    </div>
</section>
```

```css
.compare-section { padding: var(--section-padding); background: var(--white); }
.compare-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.compare-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.compare-table th, .compare-table td { padding: 16px 20px; text-align: left; border-bottom: 1px solid #eee; }
.compare-table th { background: var(--black); color: var(--white); font-weight: 600; }
.compare-table th:first-child { border-radius: 8px 0 0 0; }
.compare-table th:last-child { border-radius: 0 8px 0 0; }
.compare-table td:first-child { font-weight: 600; color: var(--dark-gray); }
.compare-table tr:hover td { background: var(--light-gray); }
.badge-new {
    display: inline-block; background: var(--accent); color: white;
    font-size: 11px; padding: 2px 8px; border-radius: 4px; margin-left: 8px; font-weight: 600;
}
```

---

## 8. FAQ-Accordion

分类手风琴 FAQ。每个分类含多个问答对。

```html
<section class="faq-section">
    <div class="container">
        <h2>FAQ</h2>
        <div class="faq-category">
            <h3>Product Info</h3>
            <div class="faq-item">
                <div class="faq-question">Is [Product] a bone conduction headphone?</div>
                <div class="faq-answer">Direct answer first. Then expand with details.</div>
            </div>
            <!-- more faq-item -->
        </div>
        <div class="faq-category">
            <h3>Comparisons</h3>
            <!-- faq-items -->
        </div>
        <div class="faq-category">
            <h3>User Guide</h3>
            <!-- faq-items -->
        </div>
        <div class="faq-category">
            <h3>Shokz App</h3>
            <!-- faq-items -->
        </div>
    </div>
</section>
```

```css
.faq-section { padding: var(--section-padding); background: var(--light-gray); }
.faq-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.faq-category { margin-bottom: 32px; }
.faq-category h3 { font-size: 18px; font-weight: 600; margin-bottom: 16px; color: var(--dark-gray); }
.faq-item { background: var(--white); border-radius: 8px; margin-bottom: 8px; overflow: hidden; }
.faq-question {
    padding: 16px 20px; font-weight: 500; cursor: pointer;
    display: flex; justify-content: space-between; align-items: center;
}
.faq-question::after { content: "+"; font-size: 20px; color: var(--mid-gray); }
.faq-answer { padding: 0 20px 16px; font-size: 14px; color: var(--mid-gray); line-height: 1.7; }
```

---

## 9. Box-Grid（What's in the Box）

配件展示 grid。

```html
<section class="box-section">
    <div class="container">
        <h2>What's In The Box</h2>
        <div class="box-items">
            <div class="box-item"><p>Product Headset</p></div>
            <div class="box-item"><p>Charging Case</p></div>
            <div class="box-item"><p>USB-C Charging Cable</p></div>
            <div class="box-item"><p>User Guide</p></div>
            <div class="box-item"><p>Warranty Card</p></div>
        </div>
    </div>
</section>
```

```css
.box-section { padding: var(--section-padding); background: var(--light-gray); }
.box-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.box-items { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; text-align: center; }
.box-item { padding: 24px; background: var(--white); border-radius: 12px; }
.box-item p { font-size: 14px; color: var(--dark-gray); }
```

---

## 10. Trust-Badges

四项购买保障横排。

```html
<div class="trust-badges">
    <div class="trust-item">
        <strong>Fast & Free Delivery</strong>
        <p>Every order ships free and fast.</p>
    </div>
    <div class="trust-item">
        <strong>45-Day Price Match Promise</strong>
        <p>We'll refund the difference. No hoops.</p>
    </div>
    <div class="trust-item">
        <strong>45-Day Free Returns</strong>
        <p>Try risk-free with our return policy.</p>
    </div>
    <div class="trust-item">
        <strong>2-Year Warranty</strong>
        <p>Hassle-free replacement guaranteed.</p>
    </div>
</div>
```

```css
.trust-badges { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; padding: 40px 0; }
.trust-item { text-align: center; }
.trust-item strong { display: block; font-size: 14px; margin-bottom: 4px; }
.trust-item p { font-size: 13px; color: var(--mid-gray); line-height: 1.5; }
```

---

## 11. Footnotes

底部免责声明区。

```html
<section class="footnotes">
    <div class="container">
        <p>* Weight data from Shokz testing laboratory. Actual weight may vary by ±X g.</p>
        <p>* Battery life data sourced from Shokz Lab under controlled conditions...</p>
        <p>* Actual Bluetooth range may vary depending on environmental factors...</p>
    </div>
</section>
```

```css
.footnotes { padding: 40px 0; background: var(--white); border-top: 1px solid #eee; }
.footnotes p { font-size: 11px; color: #999; line-height: 1.6; margin-bottom: 8px; }
```

---

## 12. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--black); line-height: 1.6; }
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 var(--container-px); }
.btn-primary {
    display: inline-block; background: var(--black); color: var(--white);
    padding: 16px 48px; border-radius: 30px; font-size: 16px; font-weight: 600;
    text-decoration: none; transition: background 0.2s; border: none; cursor: pointer;
}
.btn-primary:hover { background: var(--dark-gray); }
```
