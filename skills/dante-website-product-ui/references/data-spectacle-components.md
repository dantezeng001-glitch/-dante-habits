# Data Spectacle Style — Component Library

> 近似品牌：OPPO / Huawei / Soundcore / Oladance

可复用 HTML 组件片段。每个组件含完整 HTML 结构 + 对应 CSS。全暗沉浸式，一屏一功能，数据大字报为视觉核心。

---

## 1. Hero-Immersive

全视口暗色背景，居中浮空产品渲染图，标题 + Tech Pills + CTA。

```html
<section class="hero-immersive">
    <div class="hero-bg-glow"></div>
    <div class="container">
        <h1 class="hero-title">[PRODUCT NAME]</h1>
        <p class="hero-subtitle">[Sensory Tagline — 感官短语]</p>
        <div class="tech-pills">
            <span class="pill">LHDC 5.0</span>
            <span class="pill">Bone Mic</span>
            <span class="pill">Dual Driver</span>
            <span class="pill">ANC 3.0</span>
            <span class="pill">Dynaudio Co-tuned</span>
        </div>
        <div class="hero-product-image">[Image: floating product render, center, large]</div>
        <div class="hero-cta-group">
            <a href="#" class="btn-cta-primary">Buy Now</a>
            <a href="#" class="btn-cta-secondary">Learn More</a>
        </div>
    </div>
</section>
```

```css
.hero-immersive {
    position: relative; min-height: 100vh; display: flex; align-items: center;
    justify-content: center; background: var(--bg-primary); color: var(--text-primary);
    text-align: center; overflow: hidden; padding: 120px 0;
}
.hero-bg-glow {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 600px; height: 600px; border-radius: 50%;
    background: radial-gradient(circle, rgba(102,126,234,0.15) 0%, transparent 70%);
    filter: blur(80px); pointer-events: none;
}
.hero-title { font-size: clamp(48px, 8vw, 72px); font-weight: 800; line-height: 1.05; margin-bottom: 16px; }
.hero-subtitle { font-size: clamp(18px, 3vw, 28px); font-weight: 400; color: var(--text-secondary); margin-bottom: 32px; }
.tech-pills { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 48px; }
.pill {
    padding: 6px 16px; border: 1px solid var(--border); border-radius: var(--radius-pill);
    font-size: 13px; font-weight: 500; color: var(--text-secondary);
    background: rgba(255,255,255,0.05);
}
.hero-product-image {
    max-width: 560px; margin: 0 auto 48px; aspect-ratio: 4/3;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--text-secondary);
}
.hero-cta-group { display: flex; gap: 16px; justify-content: center; }
.btn-cta-primary {
    display: inline-block; padding: 14px 40px; border-radius: var(--radius-button);
    background: var(--text-primary); color: var(--bg-primary);
    font-size: 16px; font-weight: 600; text-decoration: none; border: none; cursor: pointer;
    transition: opacity var(--transition-standard);
}
.btn-cta-primary:hover { opacity: 0.85; }
.btn-cta-secondary {
    display: inline-block; padding: 14px 40px; border-radius: var(--radius-button);
    background: transparent; color: var(--text-primary);
    border: 1px solid var(--border); font-size: 16px; font-weight: 500;
    text-decoration: none; cursor: pointer; transition: border-color var(--transition-standard);
}
.btn-cta-secondary:hover { border-color: var(--text-secondary); }
```

---

## 2. Tech-Pills-Bar

水平胶囊徽章栏，展示核心技术卖点。可独立使用或嵌入 Hero。

```html
<div class="tech-pills-bar">
    <div class="container">
        <div class="tech-pills">
            <span class="pill">LHDC 4.0</span>
            <span class="pill">Bone Conduction Mic</span>
            <span class="pill">Dual Dynamic Driver</span>
            <span class="pill">Adaptive ANC</span>
            <span class="pill">Dynaudio Co-tuned</span>
            <span class="pill">IP55</span>
        </div>
    </div>
</div>
```

```css
.tech-pills-bar {
    padding: 24px 0; background: var(--bg-secondary);
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
}
.tech-pills {
    display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;
}
.pill {
    padding: 6px 16px; border: 1px solid var(--border); border-radius: var(--radius-pill);
    font-size: 13px; font-weight: 500; color: var(--text-secondary);
    background: rgba(255,255,255,0.05); white-space: nowrap;
}
```

---

## 3. Data-Callout-Panel

大字报数字网格——Chinese Tech 标志性组件。数字尺寸为所有风格之最（64-120px）。

```html
<section class="data-callout-section">
    <div class="container">
        <div class="data-callout-grid">
            <div class="data-cell">
                <div class="data-number">2×</div>
                <div class="data-label">bass depth vs previous gen</div>
            </div>
            <div class="data-cell">
                <div class="data-number">+67%</div>
                <div class="data-label">noise cancellation improvement</div>
                <div class="data-basis">vs [Previous Model]</div>
            </div>
            <div class="data-cell">
                <div class="data-number">+80%</div>
                <div class="data-label">transmission efficiency</div>
                <div class="data-basis">vs standard Bluetooth</div>
            </div>
            <div class="data-cell">
                <div class="data-number">96kHz</div>
                <div class="data-label">Hi-Res lossless audio</div>
            </div>
        </div>
    </div>
</section>
```

```css
.data-callout-section { padding: var(--section-padding); background: var(--bg-primary); }
.data-callout-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 48px;
    max-width: var(--max-width); margin: 0 auto; text-align: center;
}
.data-number {
    font-size: clamp(64px, 10vw, 120px); font-weight: 800; line-height: 1;
    color: var(--text-primary); margin-bottom: 12px;
    background: linear-gradient(180deg, #fff 60%, rgba(255,255,255,0.6) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.data-label { font-size: 15px; font-weight: 400; color: var(--text-secondary); line-height: 1.4; }
.data-basis { font-size: 12px; color: var(--footnote); margin-top: 6px; }

@media (max-width: 1024px) {
    .data-callout-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .data-callout-grid { grid-template-columns: 1fr; gap: 40px; }
    .data-number { font-size: 48px; }
}
```

---

## 4. Feature-Full-Screen

一屏一功能——每个 section 占满视口高度，暗色背景，居中排版。

```html
<section class="feature-fullscreen" style="background: var(--bg-primary);">
    <div class="container">
        <span class="tech-version-tag">Intelligent ANC 3.0</span>
        <h2>Silence, Redefined.</h2>
        <p>Third-generation adaptive noise cancellation with dual-mic feed-forward/feedback hybrid architecture. Real-time environmental scanning adjusts depth 200 times per second.</p>
        <div class="feature-fullscreen-visual">[Image: product detail — ANC cutaway or waveform visualization]</div>
        <div class="feature-fullscreen-data">
            <div class="data-cell">
                <div class="data-number">-45dB</div>
                <div class="data-label">peak noise reduction</div>
            </div>
        </div>
    </div>
</section>
```

```css
.feature-fullscreen {
    min-height: var(--section-min-height); display: flex; align-items: center;
    padding: var(--section-padding); text-align: center;
    color: var(--text-primary);
}
.feature-fullscreen .container { max-width: var(--max-width-narrow); }
.tech-version-tag {
    display: inline-block; padding: 4px 14px; border: 1px solid var(--border);
    border-radius: var(--radius-pill); font-size: 13px; font-weight: 600;
    color: var(--text-secondary); margin-bottom: 20px; letter-spacing: 0.5px;
}
.feature-fullscreen h2 {
    font-size: clamp(32px, 5vw, 48px); font-weight: 700; line-height: 1.15;
    margin-bottom: 20px;
}
.feature-fullscreen p {
    font-size: 17px; line-height: 1.7; color: var(--text-body);
    max-width: 640px; margin: 0 auto 40px;
}
.feature-fullscreen-visual {
    max-width: 800px; margin: 0 auto 40px; aspect-ratio: 16/9;
    border-radius: var(--radius-card); display: flex; align-items: center;
    justify-content: center; font-size: 13px; color: var(--text-secondary);
}
.feature-fullscreen-data { display: flex; justify-content: center; gap: 64px; flex-wrap: wrap; }
```

---

## 5. Feature-Split-Dark

50/50 左右分栏，暗色背景，文字在一侧、图片在另一侧。

```html
<section class="feature-split-dark">
    <div class="container">
        <div class="split-grid">
            <div class="split-text">
                <span class="tech-version-tag">Pure Voice 2.0</span>
                <h2>Crystal Calls, Any Environment.</h2>
                <p>Bone-conduction voice pickup sensor combined with dual beamforming microphones. Eliminates wind noise up to 40km/h while preserving natural vocal timbre.</p>
                <div class="split-data-inline">
                    <div class="data-cell">
                        <div class="data-number" style="font-size: 56px;">3×</div>
                        <div class="data-label">voice clarity vs previous gen</div>
                    </div>
                </div>
            </div>
            <div class="split-visual">[Image: mic technology cutaway or call scenario]</div>
        </div>
    </div>
</section>
```

```css
.feature-split-dark {
    min-height: var(--section-min-height); display: flex; align-items: center;
    padding: var(--section-padding); background: var(--bg-secondary);
    color: var(--text-primary);
}
.split-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: var(--grid-gap);
    align-items: center;
}
.split-text { text-align: left; }
.split-text h2 { font-size: clamp(28px, 4vw, 40px); font-weight: 700; line-height: 1.2; margin-bottom: 16px; }
.split-text p { font-size: 17px; line-height: 1.7; color: var(--text-body); margin-bottom: 32px; }
.split-data-inline { display: flex; gap: 48px; }
.split-visual {
    aspect-ratio: 4/3; border-radius: var(--radius-card-large);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; color: var(--text-secondary);
    background: rgba(255,255,255,0.03);
}

@media (max-width: 1024px) {
    .split-grid { grid-template-columns: 1fr; }
    .split-text { text-align: center; }
    .split-data-inline { justify-content: center; }
}
```

---

## 6. Predecessor-Comparison

与前代产品对比——百分比进度条可视化。

```html
<section class="predecessor-section">
    <div class="container">
        <h2>A Generational Leap.</h2>
        <p class="predecessor-subtitle">vs [Previous Model Name]</p>
        <div class="comparison-bars">
            <div class="bar-row">
                <span class="bar-label">Noise Cancellation Depth</span>
                <div class="bar-track">
                    <div class="bar-prev" style="width: 60%;"><span>Previous Gen</span></div>
                    <div class="bar-current" style="width: 100%;"><span>+67%</span></div>
                </div>
            </div>
            <div class="bar-row">
                <span class="bar-label">Audio Resolution</span>
                <div class="bar-track">
                    <div class="bar-prev" style="width: 50%;"><span>Previous Gen</span></div>
                    <div class="bar-current" style="width: 100%;"><span>2×</span></div>
                </div>
            </div>
            <div class="bar-row">
                <span class="bar-label">Battery Life</span>
                <div class="bar-track">
                    <div class="bar-prev" style="width: 65%;"><span>Previous Gen</span></div>
                    <div class="bar-current" style="width: 100%;"><span>+50%</span></div>
                </div>
            </div>
            <div class="bar-row">
                <span class="bar-label">Transmission Efficiency</span>
                <div class="bar-track">
                    <div class="bar-prev" style="width: 25%;"><span>Previous Gen</span></div>
                    <div class="bar-current" style="width: 100%;"><span>4×</span></div>
                </div>
            </div>
        </div>
    </div>
</section>
```

```css
.predecessor-section {
    min-height: var(--section-min-height); display: flex; align-items: center;
    padding: var(--section-padding); background: var(--bg-primary);
    color: var(--text-primary); text-align: center;
}
.predecessor-section h2 { font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin-bottom: 12px; }
.predecessor-subtitle { font-size: 16px; color: var(--text-secondary); margin-bottom: 60px; }
.comparison-bars { max-width: 700px; margin: 0 auto; text-align: left; }
.bar-row { margin-bottom: 32px; }
.bar-label { display: block; font-size: 14px; font-weight: 500; color: var(--text-secondary); margin-bottom: 12px; }
.bar-track { position: relative; display: flex; flex-direction: column; gap: 8px; }
.bar-prev, .bar-current {
    height: 36px; border-radius: 4px; display: flex; align-items: center;
    padding: 0 16px; font-size: 13px; font-weight: 600;
}
.bar-prev { background: rgba(255,255,255,0.08); color: var(--text-secondary); }
.bar-current { background: var(--text-primary); color: var(--bg-primary); }
.bar-prev span, .bar-current span { white-space: nowrap; }
```

---

## 7. Tech-Version-Badge

版本号徽章，"Pure Voice 2.0" / "ANC 3.0"。可独立使用或嵌入其他组件。

```html
<span class="tech-version-tag">Intelligent ANC 3.0</span>
<span class="tech-version-tag">Pure Voice 2.0</span>
<span class="tech-version-tag">LHDC 5.0</span>
```

```css
.tech-version-tag {
    display: inline-block; padding: 4px 14px;
    border: 1px solid var(--border); border-radius: var(--radius-pill);
    font-size: 13px; font-weight: 600; color: var(--text-secondary);
    letter-spacing: 0.5px; background: rgba(255,255,255,0.03);
}
```

---

## 8. Certification-Logos-Bar

认证 & 合作品牌 logo 横排展示。

```html
<section class="cert-bar">
    <div class="container">
        <div class="cert-logos">
            <div class="cert-item">
                <div class="cert-icon">[Logo: Hi-Res Audio]</div>
                <span>Hi-Res Audio</span>
            </div>
            <div class="cert-item">
                <div class="cert-icon">[Logo: LDAC]</div>
                <span>LDAC</span>
            </div>
            <div class="cert-item">
                <div class="cert-icon">[Logo: Dynaudio]</div>
                <span>Co-tuned by Dynaudio</span>
            </div>
            <div class="cert-item">
                <div class="cert-icon">[Logo: Red Dot Award]</div>
                <span>Red Dot Design Award</span>
            </div>
            <div class="cert-item">
                <div class="cert-icon">[Logo: IP55]</div>
                <span>IP55 Rated</span>
            </div>
        </div>
    </div>
</section>
```

```css
.cert-bar {
    padding: 60px 0; background: var(--bg-tertiary);
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
}
.cert-logos { display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; align-items: center; }
.cert-item { text-align: center; }
.cert-icon {
    width: 56px; height: 56px; margin: 0 auto 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; color: var(--text-secondary); opacity: 0.7;
}
.cert-item span { font-size: 12px; color: var(--text-secondary); display: block; }
```

---

## 9. Battery-Callout

大号续航数字 + 快充等式。

```html
<section class="battery-section">
    <div class="container">
        <span class="tech-version-tag">All-Day Power</span>
        <div class="battery-hero-number">50H</div>
        <p class="battery-subtitle">total battery life with charging case</p>
        <div class="battery-equation">
            <div class="eq-block">
                <span class="eq-number">10</span>
                <span class="eq-unit">min charge</span>
            </div>
            <span class="eq-sign">=</span>
            <div class="eq-block">
                <span class="eq-number">4</span>
                <span class="eq-unit">hrs playback</span>
            </div>
        </div>
        <p class="battery-note">Fast charge via USB-C. Full charge in 1.5 hours.¹</p>
    </div>
</section>
```

```css
.battery-section {
    min-height: var(--section-min-height); display: flex; align-items: center;
    padding: var(--section-padding); background: var(--bg-primary);
    color: var(--text-primary); text-align: center;
}
.battery-hero-number {
    font-size: clamp(80px, 15vw, 160px); font-weight: 800; line-height: 1;
    margin: 24px 0 16px;
    background: linear-gradient(180deg, #fff 40%, rgba(255,255,255,0.5) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.battery-subtitle { font-size: 18px; color: var(--text-secondary); margin-bottom: 48px; }
.battery-equation {
    display: flex; align-items: center; justify-content: center; gap: 32px;
    margin-bottom: 32px;
}
.eq-block { text-align: center; }
.eq-number { display: block; font-size: 48px; font-weight: 800; color: var(--text-primary); }
.eq-unit { display: block; font-size: 14px; color: var(--text-secondary); margin-top: 4px; }
.eq-sign { font-size: 36px; font-weight: 300; color: var(--text-secondary); }
.battery-note { font-size: 14px; color: var(--footnote); }
```

---

## 10. Brand-Philosophy-Block

三柱品牌价值观展示。

```html
<section class="philosophy-section">
    <div class="container">
        <h2>Our Philosophy</h2>
        <div class="philosophy-grid">
            <div class="philosophy-pillar">
                <div class="pillar-number">01</div>
                <h3>Connection</h3>
                <p>Sound bridges the gap between people. We engineer audio that brings you closer to the music, the moment, and each other.</p>
            </div>
            <div class="philosophy-pillar">
                <div class="pillar-number">02</div>
                <h3>Singularity</h3>
                <p>Each product is a singular pursuit of one thing done exceptionally well. No compromises, no filler features.</p>
            </div>
            <div class="philosophy-pillar">
                <div class="pillar-number">03</div>
                <h3>Human Centric</h3>
                <p>Technology serves the human experience. Every gram, every decibel, every curve is calibrated to how you live.</p>
            </div>
        </div>
    </div>
</section>
```

```css
.philosophy-section {
    padding: var(--section-padding); background: var(--bg-secondary);
    color: var(--text-primary); text-align: center;
}
.philosophy-section h2 { font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin-bottom: 60px; }
.philosophy-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; text-align: left; }
.pillar-number { font-size: 14px; font-weight: 600; color: var(--text-secondary); margin-bottom: 16px; }
.philosophy-pillar h3 { font-size: 24px; font-weight: 700; margin-bottom: 12px; }
.philosophy-pillar p { font-size: 16px; line-height: 1.7; color: var(--text-body); }

@media (max-width: 768px) {
    .philosophy-grid { grid-template-columns: 1fr; gap: 40px; text-align: center; }
}
```

---

## 11. Compare-Table

自家产品线对比表，4-6 列。

```html
<section class="compare-section">
    <div class="container">
        <h2>Find Your Match</h2>
        <div class="compare-table-wrapper">
            <table class="compare-table">
                <thead>
                    <tr>
                        <th></th>
                        <th>
                            <div class="compare-product-img">[Image]</div>
                            <strong>[Flagship Model]</strong>
                        </th>
                        <th>
                            <div class="compare-product-img">[Image]</div>
                            <strong>[Mid Model]</strong>
                        </th>
                        <th>
                            <div class="compare-product-img">[Image]</div>
                            <strong>[Entry Model]</strong>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Price</td><td>$XXX</td><td>$XXX</td><td>$XXX</td></tr>
                    <tr><td>Driver</td><td>[Spec]</td><td>[Spec]</td><td>[Spec]</td></tr>
                    <tr><td>ANC</td><td>[Spec]</td><td>[Spec]</td><td>[Spec]</td></tr>
                    <tr><td>Battery</td><td>[Spec]</td><td>[Spec]</td><td>[Spec]</td></tr>
                    <tr><td>Codec</td><td>[Spec]</td><td>[Spec]</td><td>[Spec]</td></tr>
                    <tr><td>IP Rating</td><td>[Spec]</td><td>[Spec]</td><td>[Spec]</td></tr>
                </tbody>
            </table>
        </div>
    </div>
</section>
```

```css
.compare-section {
    padding: var(--section-padding); background: var(--bg-primary);
    color: var(--text-primary); text-align: center;
}
.compare-section h2 { font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin-bottom: 48px; }
.compare-table-wrapper { overflow-x: auto; }
.compare-table {
    width: 100%; max-width: var(--max-width); margin: 0 auto;
    border-collapse: collapse; text-align: center;
}
.compare-table th, .compare-table td {
    padding: 16px 20px; border-bottom: 1px solid var(--border);
    font-size: 14px; vertical-align: middle;
}
.compare-table th { font-weight: 600; padding-bottom: 24px; }
.compare-table td:first-child {
    text-align: left; font-weight: 500; color: var(--text-secondary); min-width: 140px;
}
.compare-product-img {
    width: 80px; height: 80px; margin: 0 auto 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; color: var(--text-secondary);
}
```

---

## 12. FAQ-Accordion

可展开问答列表，带 JS 交互。

```html
<section class="faq-section">
    <div class="container">
        <h2>FAQ</h2>
        <div class="faq-list">
            <div class="faq-item">
                <div class="faq-q" onclick="this.parentElement.classList.toggle('open')">
                    What audio codecs are supported?
                </div>
                <div class="faq-a">
                    Supports LDAC, LHDC 5.0, AAC, and SBC. Hi-Res Audio certified with up to 96kHz/24bit transmission via LDAC.
                </div>
            </div>
            <div class="faq-item">
                <div class="faq-q" onclick="this.parentElement.classList.toggle('open')">
                    How does the adaptive ANC work?
                </div>
                <div class="faq-a">
                    The dual-mic hybrid system scans ambient noise 200 times per second and adjusts cancellation depth in real time. Three manual modes are also available via the companion app.
                </div>
            </div>
            <div class="faq-item">
                <div class="faq-q" onclick="this.parentElement.classList.toggle('open')">
                    What is the actual battery life?
                </div>
                <div class="faq-a">
                    8 hours per single charge with ANC on, up to 10 hours with ANC off. Charging case provides 3 additional charges for 32 hours total.¹
                </div>
            </div>
        </div>
    </div>
</section>
```

```css
.faq-section {
    padding: var(--section-padding); background: var(--bg-secondary);
    color: var(--text-primary);
}
.faq-section h2 { text-align: center; font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin-bottom: 48px; }
.faq-list { max-width: var(--max-width-narrow); margin: 0 auto; }
.faq-item { border-bottom: 1px solid var(--border); overflow: hidden; }
.faq-q {
    padding: 20px 0; font-weight: 600; font-size: 16px; cursor: pointer;
    display: flex; justify-content: space-between; align-items: center;
}
.faq-q::after {
    content: "+"; font-size: 24px; color: var(--text-secondary);
    transition: transform var(--transition-standard);
}
.faq-item.open .faq-q::after { content: "−"; }
.faq-a {
    max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.3s ease;
    font-size: 15px; color: var(--text-body); line-height: 1.7;
}
.faq-item.open .faq-a { max-height: 300px; padding: 0 0 20px; }
```

---

## 13. Footnotes-Block

15-18 条详细脚注，带上标编号对应。

```html
<section class="footnotes-block">
    <div class="container">
        <ol class="footnotes-list">
            <li id="fn1">Battery life tested under [specific conditions]. Actual results may vary based on usage patterns, settings, and environmental factors.</li>
            <li id="fn2">ANC depth measurement based on internal testing at [frequency range] with [method]. Compared to [Previous Model] under identical conditions.</li>
            <li id="fn3">"2× bass depth" refers to low-frequency response measured at [Hz], compared to [Previous Model].</li>
            <li id="fn4">Hi-Res Audio certification requires compatible source device and LDAC codec connection.</li>
            <li id="fn5">LHDC 5.0 requires compatible source device. Codec availability varies by device manufacturer and OS version.</li>
            <li id="fn6">Fast charge: 10-minute charge provides approximately 4 hours of playback. Tested with ANC off at 50% volume.</li>
            <li id="fn7">IP55 rating tested under controlled laboratory conditions. Not designed for swimming or submersion.</li>
            <li id="fn8">Dual-driver configuration uses [Xmm] dynamic driver + [Xmm] balanced armature per ear.</li>
            <li id="fn9">Bone conduction microphone performance tested in wind speeds up to 40km/h.</li>
            <li id="fn10">Adaptive ANC scans environment at 200Hz refresh rate. Depth adjustment range: [X]dB to [X]dB.</li>
            <li id="fn11">"67% noise cancellation improvement" based on broadband ANC measurement vs [Previous Model].</li>
            <li id="fn12">Dynaudio co-tuning involves collaborative acoustic tuning; Dynaudio does not manufacture the drivers.</li>
            <li id="fn13">Multipoint connection supports simultaneous pairing with 2 devices. Seamless switching may require compatible OS.</li>
            <li id="fn14">Companion app available on iOS 14+ and Android 9+. Features may vary by platform.</li>
            <li id="fn15">Total 50-hour battery life = single charge + charging case. Measured with ANC off, AAC codec, 50% volume.</li>
        </ol>
    </div>
</section>
```

```css
.footnotes-block {
    padding: 48px 0; background: var(--bg-primary);
    border-top: 1px solid var(--border);
}
.footnotes-list {
    max-width: var(--max-width); margin: 0 auto; padding: 0 var(--container-px);
    list-style: decimal; padding-left: 48px;
}
.footnotes-list li {
    font-size: 12px; color: var(--footnote); line-height: 1.6;
    margin-bottom: 6px; padding-left: 4px;
}
```

---

## 14. Shared Utilities

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: var(--font-family); background: var(--bg-primary);
    color: var(--text-primary); line-height: 1.6;
}
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 var(--container-px); }

sup { font-size: 0.7em; vertical-align: super; color: var(--text-secondary); }
::selection { background: rgba(255,255,255,0.2); color: var(--text-primary); }
```
