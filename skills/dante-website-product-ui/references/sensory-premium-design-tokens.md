# Sensory Premium Style — Design Tokens

> 近似品牌：Bose / B&O / Jabra

极度克制：黑白灰 + 产品本身颜色。几何无衬线体，大量留白，杂志化编排。

## CSS Variables

```css
:root {
    /* === Colors === */
    --color-bg-white: #ffffff;
    --color-bg-light: #f7f7f7;
    --color-bg-dark: #1a1a1a;
    --color-bg-black: #000000;
    --color-text-primary: #1a1a1a;
    --color-text-secondary: #6e6e73;
    --color-text-inverse: #ffffff;
    --color-text-inverse-secondary: #a0a0a0;
    --color-border: #e0e0e0;
    --color-border-dark: #333;
    --color-rating: #d4a017;       /* 评分星级琥珀色 */

    /* === Typography === */
    --font-family: 'DIN Next', -apple-system, BlinkMacSystemFont,
        'Helvetica Neue', Arial, sans-serif;

    /* === Layout === */
    --max-width: 1200px;
    --max-width-narrow: 720px;
    --section-padding: 80px 0;
    --section-padding-large: 100px 0;
    --container-px: 24px;
    --grid-gap: 48px;
    --card-gap: 24px;

    /* === Border Radius === */
    --radius-button: 4px;          /* Bose 用直角或微圆角按钮 */
    --radius-card: 12px;
    --radius-pill: 8px;

    /* === Transitions === */
    --transition-standard: 0.3s ease;
    --transition-slow: 0.6s ease;
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| H1（产品名） | 32-40px | 700 | 1.2 | 购买面板上方 |
| H2（叙事标题） | 32-48px | 700 | 1.15 | 叙事区块，居中或左对齐 |
| H3（子标题） | 20-24px | 600 | 1.25 | — |
| Body（正文） | 16-18px | 400 | 1.65 | 宽松行高适配长滚动 |
| Feature Pill 文案 | 13-14px | 500 | 1.3 | Feature Icons Bar |
| Price | 24-28px | 700 | 1.2 | — |
| Spec Label | 14px | 600 | 1.4 | 规格表左列 |
| Spec Value | 14px | 400 | 1.4 | 规格表右列 |
| Button 文字 | 16px | 600 | 1 | — |
| Review Star | 16px | 400 | 1 | 琥珀色 |
| Footnote | 12px | 400 | 1.5 | `--color-text-secondary` |

## Border Radius

| 元素 | radius |
|------|--------|
| CTA 按钮（Add to Cart） | 4px（直角/微圆角） |
| 卡片 / Feature Card | 12px |
| Feature Pill | 8px |
| 色彩 swatch | 50%（圆形） |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 垂直间距 | 80-100px |
| 购买区 padding | 40px 0 |
| Feature Icons Bar 高度 | auto, padding 16px 0 |
| Feature Pill gap | 12px |
| 叙事区块间距 | 80-100px |
| 标题到正文 | 16-20px |
| Card grid gap | 24px |
| Trust item gap | 24px |
| FAQ item 间距 | 0（紧贴，用 border 分隔） |

## Responsive Breakpoints

```css
@media (max-width: 1024px) {
    .purchase-layout { grid-template-columns: 1fr; }
    .feature-pills { flex-wrap: wrap; }
}
@media (max-width: 768px) {
    .narrative-split { grid-template-columns: 1fr; gap: 32px; }
    .card-grid { grid-template-columns: 1fr; }
    .compare-table { overflow-x: auto; }
    .sticky-buy-bar { padding: 12px 16px; }
}
```

## Color Usage Rules

1. **极度克制**：页面不使用任何品牌强调色（无蓝/红/橙），仅黑白灰
2. **产品是唯一色彩**：产品配色（Driftwood Sand / Deep Plum 等）充当页面唯一的彩色元素
3. **叙事区深浅交替**：部分 section 用 `--color-bg-dark`（白字），部分用 `--color-bg-white`（黑字），制造杂志化节奏
4. **购买面板**：白底黑字，清晰直接
5. **CTA 按钮**：黑色填充 + 白色文字（全站唯一的实心按钮），其他 CTA 一律为文字链接
6. **评分星级**：琥珀色 `--color-rating`，唯一例外的非黑白色
7. **链接**：黑色文字 + 下划线，不用蓝色
