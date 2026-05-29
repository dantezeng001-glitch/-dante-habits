# Bold Contrast Style — Component Library

> 近似品牌：Beats / Marshall

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。

---

## 1. Hero / Buy Panel

顶部内联购买区：产品名 + 标语 + 价格 + 颜色选择 + ADD TO BAG。

```html
<section class="hero-buy">
    <div class="container">
        <div class="buy-panel">
            <div class="buy-image">[Product Image — Hero Shot]</div>
            <div class="buy-info">
                <h1>Beats Studio Pro</h1>
                <p class="buy-tagline">Iconic Sound</p>
                <p class="buy-price"><span class="price-label">Sale Price</span> $349.99</p>
                <div class="color-swatches">
                    <span class="swatch active" style="background:#1a1a1a" title="Black"></span>
                    <span class="swatch" style="background:#c4b5a0" title="Sandstone"></span>
                    <span class="swatch" style="background:#2d3436" title="Deep Brown"></span>
                </div>
                <button class="btn-primary">ADD TO BAG</button>
            </div>
        </div>
    </div>
</section>
```

```css
.hero-buy { padding: 48px 0; background: var(--color-bg-white); }
.buy-panel { display: grid; grid-template-columns: 1fr 1fr; gap: var(--grid-gap); align-items: center; }
.buy-image {
    background: var(--color-bg-light); border-radius: var(--radius-card); aspect-ratio: 1;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; color: var(--color-text-secondary-light);
}
.buy-info h1 { font-size: 40px; font-weight: 800; margin-bottom: 8px; }
.buy-tagline { font-size: 24px; font-weight: 500; color: var(--color-text-secondary-light); margin-bottom: 24px; }
.buy-price { font-size: 24px; font-weight: 700; margin-bottom: 24px; }
.price-label { font-size: 13px; font-weight: 400; color: var(--color-text-secondary-light); display: block; margin-bottom: 4px; }
.color-swatches { display: flex; gap: 12px; margin-bottom: 32px; }
.swatch {
    width: 32px; height: 32px; border-radius: 50%; border: 2px solid transparent;
    cursor: pointer; transition: var(--transition-standard);
}
.swatch.active { border-color: var(--color-text-primary-light); }
```

---

## 2. Promise Bar

三项承诺横排条。

```html
<div class="promise-bar">
    <div class="container">
        <div class="promise-items">
            <div class="promise-item"><strong>Free Shipping</strong></div>
            <div class="promise-item"><strong>Free In-store Pickup</strong></div>
            <div class="promise-item"><strong>3 Months Free Apple Music</strong></div>
        </div>
    </div>
</div>
```

```css
.promise-bar { padding: 16px 0; background: var(--color-bg-light); border-top: 1px solid var(--color-border-light); }
.promise-items { display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; }
.promise-item { font-size: 13px; font-weight: 500; text-align: center; }
```

---

## 3. Feature Icons Strip

4-6 个水平卡片，图标 + 短文案。

```html
<section class="feature-strip">
    <div class="container">
        <div class="strip-items">
            <div class="strip-item">
                <div class="strip-icon">[Icon]</div>
                <p>Active Noise Cancelling</p>
            </div>
            <div class="strip-item">
                <div class="strip-icon">[Icon]</div>
                <p>Up to 40 Hours of Listening Time</p>
            </div>
            <!-- more items -->
        </div>
        <a href="#specs" class="strip-link">View Tech Specs</a>
    </div>
</section>
```

```css
.feature-strip { padding: 32px 0; background: var(--color-bg-white); border-bottom: 1px solid var(--color-border-light); }
.strip-items { display: flex; justify-content: center; gap: 32px; flex-wrap: wrap; margin-bottom: 16px; }
.strip-item { text-align: center; max-width: 140px; }
.strip-icon { font-size: 28px; margin-bottom: 8px; }
.strip-item p { font-size: 13px; font-weight: 500; line-height: 1.3; }
.strip-link { display: block; text-align: center; font-size: 14px; color: var(--color-text-primary-light); text-decoration: underline; }
```

---

## 4. Deep-Dive Section（带 Category Tag）

```html
<section class="deep-section deep-section--dark">
    <div class="container">
        <span class="category-tag">SOUND</span>
        <h2>Re-engineered for incredible sound.</h2>
        <p>Body paragraph describing audio technology and user benefit.</p>
        <div class="deep-visual">[Image: product detail or lifestyle]</div>
    </div>
</section>
```

```css
.deep-section { padding: var(--section-padding-large); text-align: center; }
.deep-section--dark { background: var(--color-bg-dark); color: var(--color-text-primary-dark); }
.deep-section--dark p { color: var(--color-text-secondary-dark); }
.deep-section--light { background: var(--color-bg-white); color: var(--color-text-primary-light); }
.deep-section--light p { color: var(--color-text-secondary-light); }
.category-tag {
    display: inline-block; font-size: 12px; font-weight: 600;
    letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;
}
.deep-section h2 { font-size: 36px; font-weight: 700; margin-bottom: 16px; line-height: 1.15; max-width: var(--max-width-narrow); margin-left: auto; margin-right: auto; }
.deep-section p { font-size: 17px; line-height: 1.6; max-width: var(--max-width-narrow); margin: 0 auto 32px; }
.deep-visual {
    max-width: 800px; margin: 0 auto; border-radius: var(--radius-card); aspect-ratio: 16/9;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; padding: 24px;
}
.deep-section--dark .deep-visual { color: var(--color-text-secondary-dark); }
```

---

## 5. Data Callout（大字报）

```html
<div class="data-callout">
    <div class="data-item">
        <div class="number">Up to 80%</div>
        <div class="label">reduced distortion</div>
        <div class="basis">vs Beats Studio3 Wireless</div>
    </div>
    <div class="data-item">
        <div class="number">40 hours</div>
        <div class="label">total battery life</div>
    </div>
</div>
```

```css
.data-callout { display: flex; justify-content: center; gap: 80px; padding: 48px 0; flex-wrap: wrap; }
.data-item { text-align: center; }
.data-callout .number { font-size: 56px; font-weight: 800; line-height: 1; margin-bottom: 8px; }
.data-callout .label { font-size: 14px; font-weight: 400; }
.data-callout .basis { font-size: 12px; font-weight: 400; margin-top: 4px; opacity: 0.6; }
```

---

## 6. Expert Quote Cards

```html
<section class="quotes-section">
    <div class="container">
        <div class="quote-cards">
            <div class="quote-card">
                <blockquote>"Quote from tech reviewer about the product."</blockquote>
                <cite>@reviewer_handle — Publication Title</cite>
            </div>
            <!-- repeat 2 more -->
        </div>
    </div>
</section>
```

```css
.quotes-section { padding: var(--section-padding); background: var(--color-bg-light); }
.quote-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.quote-card { text-align: center; padding: 32px 24px; background: var(--color-bg-white); border-radius: var(--radius-card); }
.quote-card blockquote { font-size: 16px; font-style: italic; line-height: 1.5; margin-bottom: 16px; }
.quote-card cite { font-size: 13px; font-style: normal; color: var(--color-text-secondary-light); }
```

---

## 7. Numbered Feature List

```html
<div class="numbered-features">
    <div class="numbered-item">
        <span class="num">01</span>
        <div>
            <h3>Active Noise Cancelling</h3>
            <p>Block out the world and focus on your music.</p>
        </div>
    </div>
    <div class="numbered-item">
        <span class="num">02</span>
        <div>
            <h3>Transparency Mode</h3>
            <p>Stay connected to the sounds around you.</p>
        </div>
    </div>
</div>
```

```css
.numbered-features { max-width: var(--max-width-narrow); margin: 0 auto; }
.numbered-item { display: flex; gap: 24px; padding: 24px 0; border-bottom: 1px solid var(--color-border); }
.num { font-size: 14px; font-weight: 600; color: var(--color-text-secondary-light); min-width: 32px; }
.numbered-item h3 { font-size: 18px; font-weight: 600; margin-bottom: 4px; }
.numbered-item p { font-size: 15px; color: var(--color-text-secondary-light); line-height: 1.5; }
```

---

## 8. In the Box

```html
<section class="box-section">
    <div class="container">
        <h2>In the Box</h2>
        <ul class="box-list">
            <li>Beats Studio Pro Wireless Headphones</li>
            <li>USB-C to USB-C charging cable</li>
            <li>3.5mm audio cable</li>
            <li>Carrying case</li>
            <li>Quick Start Guide</li>
        </ul>
    </div>
</section>
```

```css
.box-section { padding: var(--section-padding); background: var(--color-bg-light); text-align: center; }
.box-section h2 { font-size: 32px; font-weight: 700; margin-bottom: 32px; }
.box-list { list-style: none; max-width: 400px; margin: 0 auto; }
.box-list li { padding: 10px 0; font-size: 15px; border-bottom: 1px solid var(--color-border-light); }
```

---

## 9. FAQ Accordion

```html
<section class="faq-section">
    <div class="container">
        <h2>FAQ</h2>
        <div class="faq-list">
            <div class="faq-item">
                <div class="faq-q">How good is the sound quality?</div>
                <div class="faq-a">Direct answer. Then 1-2 sentences of detail.</div>
            </div>
        </div>
    </div>
</section>
```

```css
.faq-section { padding: var(--section-padding); background: var(--color-bg-white); }
.faq-section h2 { text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 48px; }
.faq-list { max-width: var(--max-width-narrow); margin: 0 auto; }
.faq-item { border-bottom: 1px solid var(--color-border-light); }
.faq-q {
    padding: 20px 0; font-weight: 600; font-size: 16px; cursor: pointer;
    display: flex; justify-content: space-between; align-items: center;
}
.faq-q::after { content: "+"; font-size: 24px; color: var(--color-text-secondary-light); }
.faq-a { padding: 0 0 20px; font-size: 15px; color: var(--color-text-secondary-light); line-height: 1.6; }
```

---

## 10. Newsletter Signup

```html
<section class="newsletter">
    <div class="container">
        <h2>Join Our List</h2>
        <p>Be the first to know about new products and offers.</p>
        <form class="newsletter-form">
            <input type="email" placeholder="Email Address">
            <button type="submit" class="btn-primary">Sign Up</button>
        </form>
    </div>
</section>
```

```css
.newsletter { padding: var(--section-padding); background: var(--color-bg-dark); color: var(--color-text-primary-dark); text-align: center; }
.newsletter h2 { font-size: 32px; font-weight: 700; margin-bottom: 12px; }
.newsletter p { font-size: 16px; color: var(--color-text-secondary-dark); margin-bottom: 32px; }
.newsletter-form { display: flex; gap: 12px; justify-content: center; max-width: 480px; margin: 0 auto; }
.newsletter-form input {
    flex: 1; padding: 14px 20px; border-radius: var(--radius-button);
    border: 1px solid var(--color-border); background: transparent;
    color: var(--color-text-primary-dark); font-size: 16px;
}
```

---

## 11. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--color-text-primary-light); line-height: 1.6; }
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 var(--container-px); }
.btn-primary {
    display: inline-block; background: var(--color-text-primary-light); color: var(--color-bg-white);
    padding: 14px 40px; border-radius: var(--radius-button); font-size: 16px; font-weight: 600;
    text-transform: uppercase; text-decoration: none; border: none; cursor: pointer;
    transition: background var(--transition-standard); letter-spacing: 0.5px;
}
.btn-primary:hover { background: #333; }
.deep-section--dark .btn-primary { background: var(--color-bg-white); color: var(--color-text-primary-light); }
.deep-section--dark .btn-primary:hover { background: #e0e0e0; }
```
