# Sensory Premium Style — Component Library

> 近似品牌：Bose / B&O / Jabra

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。

---

## 1. Feature Pills Bar

8 个水平排列的卖点标签（图标 + 短文案），可点击展开。

```html
<section class="pills-bar">
    <div class="container">
        <div class="pills">
            <div class="pill">
                <div class="pill-icon">[Icon]</div>
                <span>CustomTune for premium sound</span>
            </div>
            <div class="pill">
                <div class="pill-icon">[Icon]</div>
                <span>Our best noise cancelling</span>
            </div>
            <div class="pill">
                <div class="pill-icon">[Icon]</div>
                <span>Up to 30 hours</span>
            </div>
            <!-- repeat up to 8 total -->
        </div>
    </div>
</section>
```

```css
.pills-bar { padding: 16px 0; background: var(--color-bg-white); border-bottom: 1px solid var(--color-border); overflow-x: auto; }
.pills { display: flex; gap: 12px; justify-content: center; flex-wrap: nowrap; min-width: max-content; }
.pill {
    display: flex; align-items: center; gap: 8px; padding: 8px 16px;
    border: 1px solid var(--color-border); border-radius: var(--radius-pill);
    font-size: 13px; font-weight: 500; white-space: nowrap; cursor: pointer;
    transition: var(--transition-standard);
}
.pill:hover { border-color: var(--color-text-primary); }
.pill-icon { font-size: 18px; }
```

---

## 2. Purchase Panel（Split Layout）

左侧产品图库 + 右侧购买面板。

```html
<section class="purchase-zone">
    <div class="container">
        <div class="purchase-layout">
            <div class="purchase-gallery">
                <div class="gallery-main">[Product Image — Main Shot]</div>
                <div class="gallery-thumbs">
                    <div class="thumb active">[Thumb 1]</div>
                    <div class="thumb">[Thumb 2]</div>
                    <div class="thumb">[Thumb 3]</div>
                </div>
            </div>
            <div class="purchase-panel">
                <h1>Bose QuietComfort Ultra Headphones (2nd Gen)</h1>
                <div class="rating">★★★★½ <span>rated 4.6 out of 5 by 313</span></div>
                <p class="product-intro">Obsessively engineered with our best noise cancellation... <a href="#">Read more</a></p>
                <div class="color-select">
                    <span class="color-label">Color: <strong>Driftwood Sand</strong></span>
                    <div class="color-swatches">
                        <span class="swatch active" style="background:#c4b5a0"></span>
                        <span class="swatch" style="background:#1a1a1a"></span>
                        <span class="swatch" style="background:#5c4033"></span>
                    </div>
                </div>
                <p class="price">$449.00</p>
                <div class="quantity">Quantity: <select><option>1</option><option>2</option></select></div>
                <div class="bosecare">
                    <h3>BoseCare</h3>
                    <label class="care-option recommended">
                        <input type="radio" name="care" checked>
                        <span>Accident Protection Plan <strong>$99.95</strong> <em>Recommended</em></span>
                    </label>
                    <label class="care-option">
                        <input type="radio" name="care">
                        <span>Protection Plan <strong>$59.95</strong></span>
                    </label>
                    <label class="care-option">
                        <input type="radio" name="care">
                        <span>No extended warranty</span>
                    </label>
                </div>
                <button class="btn-primary">Add to Cart</button>
            </div>
        </div>
    </div>
</section>
```

```css
.purchase-zone { padding: 40px 0; background: var(--color-bg-white); }
.purchase-layout { display: grid; grid-template-columns: 1fr 1fr; gap: var(--grid-gap); align-items: start; }
.gallery-main {
    background: var(--color-bg-light); border-radius: var(--radius-card); aspect-ratio: 1;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--color-text-secondary); margin-bottom: 12px;
}
.gallery-thumbs { display: flex; gap: 8px; }
.thumb {
    width: 64px; height: 64px; border-radius: 8px; background: var(--color-bg-light);
    border: 2px solid transparent; cursor: pointer;
}
.thumb.active { border-color: var(--color-text-primary); }
.purchase-panel h1 { font-size: 32px; font-weight: 700; margin-bottom: 8px; line-height: 1.2; }
.rating { font-size: 14px; margin-bottom: 16px; }
.rating span { color: var(--color-text-secondary); }
.product-intro { font-size: 15px; color: var(--color-text-secondary); line-height: 1.5; margin-bottom: 24px; }
.color-label { font-size: 14px; display: block; margin-bottom: 8px; }
.color-swatches { display: flex; gap: 10px; margin-bottom: 24px; }
.swatch { width: 28px; height: 28px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; }
.swatch.active { border-color: var(--color-text-primary); }
.price { font-size: 28px; font-weight: 700; margin-bottom: 16px; }
.quantity { font-size: 14px; margin-bottom: 24px; }
.quantity select { padding: 8px 12px; border: 1px solid var(--color-border); border-radius: 4px; }
.bosecare { margin-bottom: 24px; }
.bosecare h3 { font-size: 16px; font-weight: 600; margin-bottom: 12px; }
.care-option { display: block; padding: 12px 16px; border: 1px solid var(--color-border); border-radius: 4px; margin-bottom: 8px; cursor: pointer; font-size: 14px; }
.care-option.recommended { border-color: var(--color-text-primary); }
.care-option em { font-size: 11px; font-style: normal; background: var(--color-bg-light); padding: 2px 8px; border-radius: 4px; margin-left: 8px; }
```

---

## 3. Trust Bar

```html
<div class="trust-bar">
    <div class="container">
        <h3 class="trust-title">Benefits of buying direct from Bose</h3>
        <div class="trust-items">
            <div class="trust-item"><strong>90-day return period</strong></div>
            <div class="trust-item"><strong>Price match promise</strong></div>
            <div class="trust-item"><strong>Complimentary shipping & returns</strong></div>
            <div class="trust-item"><strong>Pay later with Afterpay</strong></div>
        </div>
    </div>
</div>
```

```css
.trust-bar { padding: 32px 0; background: var(--color-bg-light); }
.trust-title { text-align: center; font-size: 14px; font-weight: 600; margin-bottom: 16px; }
.trust-items { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; text-align: center; }
.trust-item strong { font-size: 13px; font-weight: 500; }
```

---

## 4. Sticky Buy Bar

```html
<div class="sticky-buy-bar">
    <div class="container">
        <div class="sticky-inner">
            <span class="sticky-name">QC Ultra Headphones</span>
            <div class="sticky-swatches">
                <span class="swatch-mini active" style="background:#c4b5a0"></span>
                <span class="swatch-mini" style="background:#1a1a1a"></span>
            </div>
            <span class="sticky-price">$449.00</span>
            <button class="btn-primary btn-small">Add to Cart</button>
        </div>
    </div>
</div>
```

```css
.sticky-buy-bar {
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;
    background: var(--color-bg-white); border-top: 1px solid var(--color-border);
    padding: 12px 0; display: none;
}
.sticky-buy-bar.visible { display: block; }
.sticky-inner { display: flex; align-items: center; justify-content: center; gap: 24px; }
.sticky-name { font-size: 15px; font-weight: 600; }
.swatch-mini { width: 20px; height: 20px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; }
.swatch-mini.active { border-color: var(--color-text-primary); }
.sticky-price { font-size: 18px; font-weight: 700; }
.btn-small { padding: 10px 24px; font-size: 14px; }
```

---

## 5. Narrative Section（叙事区块，零 CTA）

```html
<section class="narrative narrative--dark">
    <div class="container">
        <div class="narrative-content">
            <h2>Sink deeper into sound</h2>
            <p>Body paragraph using second-person sensory language.</p>
        </div>
        <div class="narrative-visual">[Image: immersive lifestyle shot]</div>
    </div>
</section>
```

```css
.narrative { padding: var(--section-padding-large); }
.narrative--dark { background: var(--color-bg-dark); color: var(--color-text-inverse); }
.narrative--dark p { color: var(--color-text-inverse-secondary); }
.narrative--light { background: var(--color-bg-white); color: var(--color-text-primary); }
.narrative--light p { color: var(--color-text-secondary); }
.narrative-content { max-width: var(--max-width-narrow); margin: 0 auto 48px; text-align: center; }
.narrative h2 { font-size: 36px; font-weight: 700; margin-bottom: 16px; line-height: 1.15; }
.narrative p { font-size: 17px; line-height: 1.65; }
.narrative-visual {
    max-width: 960px; margin: 0 auto; border-radius: var(--radius-card);
    aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center;
    font-size: 13px; padding: 24px;
}
```

---

## 6. Feature Card Grid

```html
<section class="features-grid-section">
    <div class="container">
        <h2>Features</h2>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-card-icon">[Icon]</div>
                <h3>CustomTune</h3>
                <p>Sound that's uniquely shaped to your ears.</p>
            </div>
            <!-- repeat 5 more -->
        </div>
        <button class="show-more">SHOW MORE</button>
    </div>
</section>
```

```css
.features-grid-section { padding: var(--section-padding); background: var(--color-bg-light); }
.features-grid-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--card-gap); }
.feature-card { text-align: center; padding: 32px 24px; background: var(--color-bg-white); border-radius: var(--radius-card); }
.feature-card-icon { font-size: 32px; margin-bottom: 16px; }
.feature-card h3 { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.feature-card p { font-size: 14px; color: var(--color-text-secondary); line-height: 1.5; }
.show-more {
    display: block; margin: 32px auto 0; background: none; border: none;
    font-size: 13px; font-weight: 600; letter-spacing: 1px; cursor: pointer;
    color: var(--color-text-primary); text-decoration: underline;
}
```

---

## 7. Compare Table

```html
<section class="compare-section">
    <div class="container">
        <h2>Product Comparison</h2>
        <div class="compare-grid">
            <div class="compare-col">
                <div class="compare-product-img">[Product A Image]</div>
                <h3><a href="#">QC Ultra Headphones</a></h3>
                <p class="compare-price">$449</p>
            </div>
            <div class="compare-col">
                <div class="compare-product-img">[Product B Image]</div>
                <h3><a href="#">QC Headphones</a></h3>
                <p class="compare-price">$359</p>
            </div>
        </div>
        <table class="compare-table">
            <thead><tr><th>Audio Technology</th><th></th><th></th></tr></thead>
            <tbody>
                <tr><td>Active Noise Cancellation</td><td>Yes</td><td>Yes</td></tr>
                <tr><td>Bose Immersive Audio</td><td>Yes</td><td>—</td></tr>
                <tr><td>Battery Life</td><td>Up to 30 hrs</td><td>Up to 24 hrs</td></tr>
            </tbody>
        </table>
    </div>
</section>
```

```css
.compare-section { padding: var(--section-padding); background: var(--color-bg-white); }
.compare-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.compare-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; text-align: center; margin-bottom: 32px; }
.compare-product-img { aspect-ratio: 1; margin-bottom: 16px; }
.compare-grid h3 a { font-size: 16px; font-weight: 600; color: var(--color-text-primary); text-decoration: underline; }
.compare-price { font-size: 14px; color: var(--color-text-secondary); margin-top: 4px; }
.compare-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.compare-table th, .compare-table td { padding: 14px 16px; text-align: center; border-bottom: 1px solid var(--color-border); }
.compare-table th { font-weight: 600; text-align: left; background: var(--color-bg-light); }
.compare-table td:first-child { text-align: left; font-weight: 500; }
```

---

## 8. FAQ Accordion

```html
<section class="faq-section">
    <div class="container">
        <h2>FAQ's</h2>
        <div class="faq-list">
            <div class="faq-item">
                <div class="faq-q">Can I use these for phone calls?</div>
                <div class="faq-a">Yes. Your headphones feature enhanced voice pickup for clearer calls.</div>
            </div>
        </div>
    </div>
</section>
```

```css
.faq-section { padding: var(--section-padding); background: var(--color-bg-light); }
.faq-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.faq-list { max-width: var(--max-width-narrow); margin: 0 auto; }
.faq-item { border-bottom: 1px solid var(--color-border); }
.faq-q {
    padding: 20px 0; font-weight: 600; font-size: 16px; cursor: pointer;
    display: flex; justify-content: space-between; align-items: center;
}
.faq-q::after { content: "+"; font-size: 24px; color: var(--color-text-secondary); }
.faq-a { padding: 0 0 20px; font-size: 15px; color: var(--color-text-secondary); line-height: 1.65; }
```

---

## 9. Footnotes

```html
<section class="footnotes">
    <div class="container">
        <p>¹ Battery life varies based on settings, environmental conditions, and usage.</p>
        <p>² Testing conducted in a controlled laboratory setting.</p>
    </div>
</section>
```

```css
.footnotes { padding: 32px 0; border-top: 1px solid var(--color-border); }
.footnotes p { font-size: 12px; color: var(--color-text-secondary); line-height: 1.5; margin-bottom: 8px; }
```

---

## 10. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--color-text-primary); line-height: 1.6; }
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 var(--container-px); }
.btn-primary {
    display: inline-block; background: var(--color-text-primary); color: var(--color-text-inverse);
    padding: 14px 40px; border-radius: var(--radius-button); font-size: 16px; font-weight: 600;
    text-decoration: none; border: none; cursor: pointer;
    transition: background var(--transition-standard);
}
.btn-primary:hover { background: #333; }
```
