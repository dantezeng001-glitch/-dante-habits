# Tech Premium Style — Component Library

> 近似品牌：Sony

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。

---

## 1. Hero-Marketing（营销页全屏 Hero）

全屏深色居中，产品名 + 定位句 + 产品图 + 视频链接。

```html
<section class="hero">
    <div class="hero-content">
        <h1>WH-1000XM6</h1>
        <p class="hero-subtitle">Best Wireless Noise Canceling Headphones</p>
        <h2 class="hero-tagline">Beyond quiet. Transcendent sound.</h2>
        <a href="#" class="hero-video-link">▶ Watch the video</a>
    </div>
    <div class="hero-image">[Image: product centered on pure black background, hero shot]</div>
</section>
```

```css
.hero {
    min-height: 100vh; display: flex; flex-direction: column;
    align-items: center; justify-content: center; text-align: center;
    background: var(--color-bg-primary); color: var(--color-text-primary-dark);
    overflow: hidden; position: relative; padding: 80px var(--padding-inline);
}
.hero-content { position: relative; z-index: 2; }
.hero h1 { font-size: var(--font-size-hero); font-weight: 700; letter-spacing: -0.5px; margin-bottom: 8px; }
.hero-subtitle { font-size: var(--font-size-body); color: var(--color-text-secondary-dark); margin-bottom: 24px; }
.hero-tagline { font-size: var(--font-size-h2); font-weight: 700; margin-bottom: 32px; line-height: 1.15; }
.hero-video-link {
    font-size: 16px; color: var(--color-text-primary-dark);
    text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.3);
    padding-bottom: 4px; transition: var(--transition-quick);
}
.hero-video-link:hover { border-bottom-color: #fff; }
.hero-image {
    width: 100%; max-width: 800px; aspect-ratio: 16/9;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--color-text-secondary-dark); margin-top: 48px;
}
```

---

## 2. Hero-Purchase（购买页 Hero）

左侧图片 gallery + 右侧购买面板（价格、颜色选择器、ADD TO CART）。

```html
<section class="purchase-hero">
    <div class="container">
        <div class="purchase-panel">
            <div class="purchase-gallery">
                <div class="gallery-main">[Image: product main angle, white background]</div>
                <div class="gallery-thumbs">
                    <div class="thumb active">[Thumb 1]</div>
                    <div class="thumb">[Thumb 2]</div>
                    <div class="thumb">[Thumb 3]</div>
                    <div class="thumb">[Thumb 4]</div>
                </div>
            </div>
            <div class="purchase-info">
                <h1>WH-1000XM6 Wireless Noise Canceling Headphones</h1>
                <div class="purchase-model">Model: WH1000XM6/B</div>
                <div class="purchase-rating">
                    <span class="stars">★★★★★</span>
                    <span class="rating-count">4.8 (2,847 reviews)</span>
                </div>
                <div class="purchase-price">
                    <span class="price-current">$399.99</span>
                    <span class="price-save">Save $50</span>
                </div>
                <div class="purchase-affirm">
                    Starting at $34/mo with <strong>Affirm</strong>. <a href="#">Learn more</a>
                </div>
                <div class="color-selector">
                    <p class="color-label">Color: <strong>Black</strong></p>
                    <div class="color-options">
                        <button class="color-swatch active" style="background:#1a1a1a;" aria-label="Black"></button>
                        <button class="color-swatch" style="background:#c5bfb5;" aria-label="Silver"></button>
                        <button class="color-swatch" style="background:#2c3e50;" aria-label="Midnight Blue"></button>
                    </div>
                </div>
                <button class="btn-add-to-cart">ADD TO CART</button>
                <a href="#" class="link-where-to-buy">Where To Buy</a>
            </div>
        </div>
    </div>
</section>
```

```css
.purchase-hero { background: var(--color-bg-white); padding: 48px 0 60px; }
.purchase-panel { display: grid; grid-template-columns: 1fr 1fr; gap: var(--grid-gap); align-items: start; }
.gallery-main {
    aspect-ratio: 1; background: var(--color-bg-light); border-radius: var(--radius-card);
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--color-text-secondary-light); margin-bottom: 16px;
}
.gallery-thumbs { display: flex; gap: 12px; }
.thumb {
    width: 72px; height: 72px; border-radius: var(--radius-small);
    border: 2px solid transparent; background: var(--color-bg-light);
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; color: var(--color-text-secondary-light); cursor: pointer;
}
.thumb.active { border-color: var(--color-text-primary-light); }
.purchase-info h1 { font-size: 24px; font-weight: 700; margin-bottom: 8px; color: var(--color-text-primary-light); }
.purchase-model { font-size: 13px; color: var(--color-text-secondary-light); margin-bottom: 12px; }
.purchase-rating { margin-bottom: 16px; }
.stars { color: #f5a623; font-size: 16px; }
.rating-count { font-size: 14px; color: var(--color-accent-blue); margin-left: 8px; }
.purchase-price { margin-bottom: 8px; }
.price-current { font-size: var(--font-size-price); font-weight: 700; color: var(--color-text-primary-light); }
.price-save { font-size: 16px; color: var(--color-promo-red); font-weight: 600; margin-left: 12px; }
.purchase-affirm { font-size: 14px; color: var(--color-text-secondary-light); margin-bottom: 24px; }
.purchase-affirm a { color: var(--color-accent-blue); text-decoration: none; }
.color-label { font-size: 14px; margin-bottom: 12px; color: var(--color-text-primary-light); }
.color-options { display: flex; gap: 12px; margin-bottom: 32px; }
.color-swatch {
    width: 36px; height: 36px; border-radius: 50%; border: 2px solid transparent;
    cursor: pointer; outline: none; transition: var(--transition-quick);
}
.color-swatch.active { border-color: var(--color-text-primary-light); box-shadow: 0 0 0 2px #fff, 0 0 0 4px var(--color-text-primary-light); }
.btn-add-to-cart {
    display: block; width: 100%; padding: 16px; font-size: 16px; font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase;
    background: var(--color-text-primary-light); color: var(--color-bg-white);
    border: none; border-radius: var(--radius-button); cursor: pointer;
    transition: background var(--transition-quick); margin-bottom: 16px;
}
.btn-add-to-cart:hover { background: #333; }
.link-where-to-buy { display: block; text-align: center; font-size: 14px; color: var(--color-accent-blue); text-decoration: none; }
```

---

## 3. Feature-Badges-Bar（功能徽章横滑条）

水平滚动的功能徽章列表，每个含图标 + 短文案。

```html
<div class="feature-badges-bar">
    <div class="container">
        <div class="feature-badges">
            <div class="feature-badge">
                <div class="badge-icon">[Icon: NC wave]</div>
                <span>Industry-leading NC</span>
            </div>
            <div class="feature-badge">
                <div class="badge-icon">[Icon: speaker]</div>
                <span>LDAC Hi-Res Audio</span>
            </div>
            <div class="feature-badge">
                <div class="badge-icon">[Icon: battery]</div>
                <span>40hr Battery</span>
            </div>
            <div class="feature-badge">
                <div class="badge-icon">[Icon: mic]</div>
                <span>Crystal Clear Calls</span>
            </div>
            <div class="feature-badge">
                <div class="badge-icon">[Icon: bluetooth]</div>
                <span>Multipoint Connect</span>
            </div>
            <div class="feature-badge">
                <div class="badge-icon">[Icon: chip]</div>
                <span>V2 Processor</span>
            </div>
        </div>
    </div>
</div>
```

```css
.feature-badges-bar { background: var(--color-bg-white); padding: 24px 0; border-bottom: 1px solid var(--color-border-light); }
.feature-badges {
    display: flex; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch; padding-bottom: 8px;
}
.feature-badge {
    flex: 0 0 auto; display: flex; align-items: center; gap: 10px;
    padding: 10px 20px; background: var(--color-bg-light);
    border-radius: var(--radius-badge); white-space: nowrap;
    scroll-snap-align: start; font-size: var(--font-size-badge); font-weight: 500;
    color: var(--color-text-primary-light);
}
.badge-icon { font-size: 18px; flex-shrink: 0; }
```

---

## 4. Media-Reviews-Block（媒体评价卡片区）

3 列引用卡片，每张含出版物评语 + 来源 + 年份。

```html
<div class="media-reviews">
    <div class="container">
        <h3 class="media-reviews-title">What the experts say</h3>
        <div class="reviews-grid">
            <div class="review-card">
                <blockquote>"The best noise-canceling headphones money can buy — and it's not even close."</blockquote>
                <cite>— The Verge, 2026</cite>
            </div>
            <div class="review-card">
                <blockquote>"Sony has done it again. The XM6 sets a new standard for wireless audio."</blockquote>
                <cite>— CNET, 2026</cite>
            </div>
            <div class="review-card">
                <blockquote>"Transcendent sound quality with noise canceling that borders on supernatural."</blockquote>
                <cite>— What Hi-Fi?, 2026</cite>
            </div>
        </div>
    </div>
</div>
```

```css
.media-reviews { padding: 80px 0; }
.media-reviews-title {
    font-size: var(--font-size-h3); font-weight: 700; text-align: center;
    margin-bottom: 48px; color: var(--color-text-primary-dark);
}
.reviews-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.review-card {
    background: var(--color-bg-secondary); border-radius: var(--radius-card);
    padding: 32px; display: flex; flex-direction: column; justify-content: space-between;
}
.review-card blockquote {
    font-size: 18px; font-weight: 400; line-height: 1.5;
    color: var(--color-text-primary-dark); margin-bottom: 24px; font-style: italic;
}
.review-card cite {
    font-size: 14px; color: var(--color-text-secondary-dark);
    font-style: normal; display: block;
}
@media (max-width: 734px) {
    .reviews-grid { grid-template-columns: 1fr; }
}
```

---

## 5. Feature-Section-Dark（全宽深色特性区块）

居中标题 + 正文 + 底部产品图。

```html
<section class="section--dark">
    <div class="container" style="text-align:center;">
        <h2>Silence the world around you.</h2>
        <p style="max-width:var(--max-width-text);margin:16px auto 48px;">
            The most advanced noise canceling we've ever developed — powered by the
            Integrated Processor V2 and eight microphones that sense ambient sound
            7x faster than before.<sup>1</sup>
        </p>
        <div class="feature-image">[Image: product detail — ear cup microphone array close-up]</div>
    </div>
</section>
```

```css
.section--dark {
    background: var(--color-bg-primary); color: var(--color-text-primary-dark);
    padding: var(--section-padding);
}
.section--dark p { color: var(--color-text-secondary-dark); }
.section--dark h2 { font-size: var(--font-size-h2); font-weight: 700; line-height: 1.15; margin-bottom: 16px; }
.feature-image {
    width: 100%; max-width: 900px; margin: 0 auto; aspect-ratio: 16/9;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--color-text-secondary-dark);
}
```

---

## 6. Feature-Section-Split（50/50 左文右图深色区块）

```html
<section class="section--secondary">
    <div class="container">
        <div class="split">
            <div class="split-text">
                <h2>Sound that moves you.</h2>
                <h3>Custom 40mm driver unit</h3>
                <p>
                    Reimagined from the ground up — a newly developed driver with a
                    rigid dome and soft edge delivers ultra-low distortion across the
                    entire frequency range, so you hear every note as the artist intended.
                </p>
                <a href="#" class="link-sony">Learn More</a>
            </div>
            <div class="split-visual">[Image: product detail — driver unit exploded view]</div>
        </div>
    </div>
</section>
```

```css
.section--secondary {
    background: var(--color-bg-secondary); color: var(--color-text-primary-dark);
    padding: var(--section-padding);
}
.section--secondary p { color: var(--color-text-secondary-dark); }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: var(--grid-gap); align-items: center; }
.split-text h2 { font-size: var(--font-size-h2); font-weight: 700; margin-bottom: 16px; line-height: 1.15; }
.split-text h3 { font-size: var(--font-size-h3); font-weight: 700; margin-bottom: 12px; color: var(--color-text-secondary-dark); }
.split-text p { font-size: var(--font-size-body); line-height: 1.6; margin-bottom: 24px; }
.split-visual {
    aspect-ratio: 4/3; border-radius: var(--radius-card);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--color-text-secondary-dark); padding: 24px;
}
.link-sony { color: var(--color-accent-blue); text-decoration: none; font-size: 16px; font-weight: 500; }
.link-sony:hover { text-decoration: underline; }
```

---

## 7. Tech-Three-Layer（三层技术叙事）

Sony 特有的三层递进叙事：情感钩子 → 技术实质 → 量化对比。

```html
<section class="section--dark tech-three-layer">
    <div class="container">
        <div class="layer-emotional">
            <h2>Beyond quiet. Transcendent sound.</h2>
        </div>
        <div class="layer-technical">
            <h3>Integrated Processor V2</h3>
            <p>
                The all-new V2 chip processes noise-canceling signals independently
                from audio playback — delivering simultaneous precision for both.
                Eight beam-forming microphones create a detailed sound map of your
                environment, adapting 700 times per second.
            </p>
        </div>
        <div class="layer-quantified">
            <div class="stat-card">
                <div class="stat-number">7x</div>
                <div class="stat-label">faster ambient sound sensing than WH-1000XM5<sup>1</sup></div>
            </div>
        </div>
    </div>
</section>
```

```css
.tech-three-layer .layer-emotional { text-align: center; margin-bottom: 48px; }
.tech-three-layer .layer-emotional h2 { font-size: var(--font-size-hero); font-weight: 700; line-height: 1.1; }
.tech-three-layer .layer-technical { max-width: var(--max-width-text); margin: 0 auto 48px; text-align: center; }
.tech-three-layer .layer-technical h3 { font-size: var(--font-size-h3); font-weight: 700; margin-bottom: 16px; }
.tech-three-layer .layer-technical p { font-size: var(--font-size-body); line-height: 1.6; color: var(--color-text-secondary-dark); }
.tech-three-layer .layer-quantified { text-align: center; }
.stat-card { display: inline-block; padding: 40px 60px; }
.stat-number { font-size: var(--font-size-stat); font-weight: 700; line-height: 1; color: var(--color-text-primary-dark); }
.stat-label { font-size: 16px; color: var(--color-text-secondary-dark); margin-top: 12px; max-width: 300px; }
```

---

## 8. Engineer-Testimonial（工程师证言）

Sony 特色：工程师引言 + 姓名 + 工作室 + 合作艺术家列表。

```html
<div class="engineer-testimonial">
    <div class="container">
        <blockquote class="engineer-quote">
            "We didn't just want to cancel noise — we wanted to create a space
            where nothing exists between you and the music."
        </blockquote>
        <div class="engineer-info">
            <p class="engineer-name">Takeshi Nakamura</p>
            <p class="engineer-studio">Senior Acoustic Engineer, Sony Audio Division</p>
        </div>
        <div class="engineer-credits">
            <p class="credits-label">Trusted by:</p>
            <ul class="credits-list">
                <li>Mark Ronson</li>
                <li>Jacob Collier</li>
                <li>Sony Music Studios Tokyo</li>
            </ul>
        </div>
    </div>
</div>
```

```css
.engineer-testimonial {
    padding: 80px 0; text-align: center;
    border-top: 1px solid var(--color-border-dark);
    border-bottom: 1px solid var(--color-border-dark);
}
.engineer-quote {
    font-size: 24px; font-weight: 400; font-style: italic; line-height: 1.5;
    color: var(--color-text-primary-dark); max-width: var(--max-width-text);
    margin: 0 auto 32px; quotes: none;
}
.engineer-name { font-size: 16px; font-weight: 700; color: var(--color-text-primary-dark); }
.engineer-studio { font-size: 14px; color: var(--color-text-secondary-dark); margin-top: 4px; }
.engineer-credits { margin-top: 32px; }
.credits-label { font-size: 13px; color: var(--color-text-secondary-dark); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }
.credits-list { list-style: none; display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; }
.credits-list li { font-size: 14px; color: var(--color-text-secondary-dark); }
```

---

## 9. Benefits-Bar（购买服务横条）

购买页顶部水平服务条：Easy Returns / My Sony / Free Shipping / 0% APR / 5% Back。

```html
<div class="benefits-bar">
    <div class="container">
        <div class="benefits">
            <div class="benefit">
                <span class="benefit-icon">[Icon: return]</span>
                <span>Easy Returns</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">[Icon: user]</span>
                <span>My Sony Rewards</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">[Icon: truck]</span>
                <span>Free Shipping</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">[Icon: card]</span>
                <span>0% APR Financing</span>
            </div>
            <div class="benefit">
                <span class="benefit-icon">[Icon: percent]</span>
                <span>5% Back with Sony Card</span>
            </div>
        </div>
    </div>
</div>
```

```css
.benefits-bar { background: var(--color-bg-light); padding: 16px 0; border-bottom: 1px solid var(--color-border-light); }
.benefits { display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 16px; }
.benefit { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; color: var(--color-text-primary-light); }
.benefit-icon { font-size: 18px; }
```

---

## 10. Spec-Table（分组规格表）

Key-value 格式，按分组排列：Size & Weight / General / Battery / Bluetooth / NC。

```html
<section class="spec-section">
    <div class="container">
        <h2 class="spec-title">Specifications</h2>
        <div class="spec-groups">
            <div class="spec-group">
                <h3 class="spec-group-title">Size & Weight</h3>
                <table class="spec-table">
                    <tr><td>Weight</td><td>Approx. 250 g (8.82 oz)</td></tr>
                    <tr><td>Driver Unit</td><td>40mm</td></tr>
                </table>
            </div>
            <div class="spec-group">
                <h3 class="spec-group-title">Battery</h3>
                <table class="spec-table">
                    <tr><td>Battery Life (NC ON)</td><td>Up to 40 hours<sup>1</sup></td></tr>
                    <tr><td>Battery Life (NC OFF)</td><td>Up to 50 hours<sup>2</sup></td></tr>
                    <tr><td>Charging Time</td><td>Approx. 3.5 hours</td></tr>
                    <tr><td>Quick Charge</td><td>5 min charge = 3 hours playback</td></tr>
                </table>
            </div>
            <div class="spec-group">
                <h3 class="spec-group-title">Bluetooth</h3>
                <table class="spec-table">
                    <tr><td>Version</td><td>Bluetooth 5.3</td></tr>
                    <tr><td>Codecs</td><td>SBC, AAC, LDAC, LC3</td></tr>
                    <tr><td>Multipoint</td><td>Yes (2 devices)</td></tr>
                </table>
            </div>
        </div>
    </div>
</section>
```

```css
.spec-section { background: var(--color-bg-white); padding: 80px 0; }
.spec-title { font-size: var(--font-size-h2); font-weight: 700; margin-bottom: 48px; color: var(--color-text-primary-light); }
.spec-groups { display: grid; grid-template-columns: 1fr; gap: 40px; }
.spec-group-title { font-size: 18px; font-weight: 700; padding-bottom: 12px; margin-bottom: 0; border-bottom: 2px solid var(--color-text-primary-light); color: var(--color-text-primary-light); }
.spec-table { width: 100%; border-collapse: collapse; }
.spec-table td { padding: 14px 0; font-size: 15px; border-bottom: 1px solid var(--color-border-light); vertical-align: top; }
.spec-table td:first-child { font-weight: 500; color: var(--color-text-primary-light); width: 40%; }
.spec-table td:last-child { color: var(--color-text-secondary-light); }
```

---

## 11. Compare-Table（3 列产品对比表）

含产品图片、名称、价格、"Learn More" CTA。

```html
<section class="compare-section">
    <div class="container">
        <h2 class="compare-title">Compare Models</h2>
        <div class="compare-grid">
            <div class="compare-col">
                <div class="compare-product-image">[Image: WH-1000XM6]</div>
                <h3>WH-1000XM6</h3>
                <p class="compare-price">$399.99</p>
                <a href="#" class="link-sony">Learn More</a>
            </div>
            <div class="compare-col">
                <div class="compare-product-image">[Image: WH-1000XM5]</div>
                <h3>WH-1000XM5</h3>
                <p class="compare-price">$299.99</p>
                <a href="#" class="link-sony">Learn More</a>
            </div>
            <div class="compare-col">
                <div class="compare-product-image">[Image: WF-1000XM6]</div>
                <h3>WF-1000XM6</h3>
                <p class="compare-price">$279.99</p>
                <a href="#" class="link-sony">Learn More</a>
            </div>
        </div>
        <table class="compare-specs-table">
            <thead><tr><th></th><th>XM6</th><th>XM5</th><th>WF-XM6</th></tr></thead>
            <tbody>
                <tr><td>Noise Canceling</td><td>Industry Leading</td><td>Excellent</td><td>Industry Leading</td></tr>
                <tr><td>Battery Life</td><td>40 hrs</td><td>30 hrs</td><td>8 + 16 hrs</td></tr>
                <tr><td>Driver</td><td>40mm</td><td>30mm</td><td>8.4mm</td></tr>
                <tr><td>Bluetooth</td><td>5.3</td><td>5.2</td><td>5.3</td></tr>
            </tbody>
        </table>
    </div>
</section>
```

```css
.compare-section { background: var(--color-bg-white); padding: 80px 0; border-top: 1px solid var(--color-border-light); }
.compare-title { font-size: var(--font-size-h2); font-weight: 700; text-align: center; margin-bottom: 48px; color: var(--color-text-primary-light); }
.compare-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-bottom: 48px; }
.compare-col { text-align: center; }
.compare-product-image {
    aspect-ratio: 1; background: var(--color-bg-light); border-radius: var(--radius-card);
    margin-bottom: 16px; display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--color-text-secondary-light);
}
.compare-col h3 { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
.compare-price { font-size: 16px; color: var(--color-text-secondary-light); margin-bottom: 8px; }
.compare-specs-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.compare-specs-table th, .compare-specs-table td { padding: 14px 16px; text-align: center; border-bottom: 1px solid var(--color-border-light); }
.compare-specs-table th { font-weight: 700; padding-bottom: 20px; font-size: 15px; }
.compare-specs-table td:first-child { text-align: left; font-weight: 500; }
```

---

## 12. Footnotes（脚注区）

30+ 编号脚注，每条含测试条件。

```html
<section class="footnotes">
    <div class="container">
        <ol class="footnote-list">
            <li id="fn1">Battery life measured with NC on, AAC codec, DSEE off, at moderate volume. Actual results may vary.</li>
            <li id="fn2">Battery life measured with NC off, SBC codec. Actual results may vary depending on content and conditions.</li>
            <li id="fn3">Compared to WH-1000XM5. Based on internal Sony testing conducted in February 2026.</li>
            <li id="fn4">LDAC requires compatible source device. Actual audio quality depends on source and codec settings.</li>
            <li id="fn5">Multipoint connection supports up to 2 devices simultaneously. Some features may be limited.</li>
            <!-- ... up to fn30+ -->
        </ol>
    </div>
</section>
```

```css
.footnotes { padding: 40px 0; border-top: 1px solid var(--color-border-light); background: var(--color-bg-white); }
.footnote-list { padding-left: 24px; max-width: var(--max-width-content); margin: 0 auto; }
.footnote-list li { font-size: 11px; color: var(--color-text-secondary-light); line-height: 1.5; margin-bottom: 6px; }
.footnote-list sup { font-size: 0.7em; }
```

---

## 13. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--color-text-primary-light); line-height: 1.5; -webkit-font-smoothing: antialiased; }
.container { max-width: var(--max-width-content); margin: 0 auto; padding: 0 var(--padding-inline); }
sup { font-size: 0.6em; vertical-align: super; }

/* Tab Navigation (buy page) */
.tab-nav { display: flex; gap: 0; border-bottom: 1px solid var(--color-border-light); background: var(--color-bg-white); position: sticky; top: 0; z-index: 100; }
.tab-nav a {
    padding: 16px 24px; font-size: 14px; font-weight: 500;
    color: var(--color-text-secondary-light); text-decoration: none;
    border-bottom: 2px solid transparent; transition: var(--transition-quick);
}
.tab-nav a.active { color: var(--color-text-primary-light); border-bottom-color: var(--color-text-primary-light); }
.tab-nav a:hover { color: var(--color-text-primary-light); }
```
