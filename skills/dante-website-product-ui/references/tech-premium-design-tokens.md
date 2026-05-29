# Tech Premium Style — Design Tokens

> 近似品牌：Sony

80%+ 深色背景的沉浸式影院风格。白色仅用于规格/购买区域。链接蓝和促销红是唯二强调色。

## CSS Variables

```css
:root {
    /* === Colors — Dark Context (dominant, 80%+ of page) === */
    --color-bg-primary: #000;
    --color-bg-secondary: #1a1a1a;
    --color-text-primary-dark: #fff;
    --color-text-secondary-dark: #999;
    --color-border-dark: #333;

    /* === Colors — Light Context (specs / purchase area) === */
    --color-bg-light: #f5f5f5;
    --color-bg-white: #fff;
    --color-text-primary-light: #1a1a1a;
    --color-text-secondary-light: #666;
    --color-border-light: #e0e0e0;

    /* === Accent === */
    --color-accent-blue: #0070D2;
    --color-promo-red: #e74c3c;

    /* === Typography === */
    --font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    --font-size-hero: clamp(48px, 6vw, 64px);
    --font-size-h2: clamp(32px, 4vw, 40px);
    --font-size-h3: clamp(24px, 3vw, 28px);
    --font-size-body: clamp(16px, 1.2vw, 18px);
    --font-size-price: clamp(28px, 3vw, 36px);
    --font-size-caption: 13px;
    --font-size-badge: 12px;
    --font-size-stat: clamp(48px, 8vw, 96px);

    /* === Layout === */
    --max-width-content: 1200px;
    --max-width-text: 800px;
    --section-padding: 100px 0;
    --padding-inline: max(24px, 4vw);
    --grid-gap: 60px;

    /* === Border Radius === */
    --radius-button: 6px;
    --radius-card: 18px;
    --radius-badge: 20px;
    --radius-small: 4px;

    /* === Transitions === */
    --transition-smooth: 0.4s cubic-bezier(0.25, 0.1, 0.25, 1);
    --transition-quick: 0.2s ease;
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| Hero H1（营销页主标） | clamp(48-64px) | 700 | 1.1 | 居中，深底白字 |
| H2（Section 标题） | clamp(32-40px) | 700 | 1.15 | 居中或左对齐 |
| H3（子特性标题） | clamp(24-28px) | 700 | 1.2 | 左对齐 |
| Body（正文） | clamp(16-18px) | 400 | 1.6 | max-width 800px |
| Price（价格） | clamp(28-36px) | 700 | 1 | 购买面板 |
| Caption / Badge | 12-14px | 500 | 1.3 | 功能徽章、标签 |
| Stat 大数字 | clamp(48-96px) | 700 | 1 | 居中，量化对比 |

## Border Radius

| 元素 | radius | 备注 |
|------|--------|------|
| CTA 按钮 | 6px | 非胶囊——Sony 用微圆角矩形 |
| 卡片 / 媒体评价 | 18px | |
| 功能徽章 | 20px | 药丸形 |
| 小元素 / 标签 | 4px | |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 间距 | 80-120px（`--section-padding`） |
| 容器左右 padding | max(24px, 4vw) |
| 内容最大宽度 | 1200px |
| 正文最大宽度 | 800px |
| 标题到正文 | 16-24px |
| 卡片内 padding | 24-32px |
| Grid gap | 60px |
| Feature Badge gap | 16px |
| Hero 最小高度 | 100vh |

## Responsive Breakpoints

```css
@media (max-width: 1068px) {
    /* 平板：缩小字号、2 列网格 */
    .hero h1 { font-size: 40px; }
    .split { grid-template-columns: 1fr; }
    .purchase-panel { grid-template-columns: 1fr; }
}
@media (max-width: 734px) {
    /* 手机：单列堆叠 */
    .feature-badges { overflow-x: auto; flex-wrap: nowrap; }
    .benefits-bar { flex-direction: column; }
    .spec-group { grid-template-columns: 1fr; }
    .compare-table { font-size: 12px; }
}
```

## Color Usage Rules

1. **深色主导**：营销页 80%+ section 使用 `--color-bg-primary` 或 `--color-bg-secondary`，与 Apple 深浅交替不同
2. **购买页**：购买面板区域用 `--color-bg-white`，Features 区仍用深色
3. **Benefits Bar**：使用 `--color-bg-light` (#f5f5f5)，是营销页中极少的浅色区域
4. **CTA 按钮**：黑底白字（`background: #000; color: #fff`），非 Apple 的蓝底
5. **链接**：`--color-accent-blue` (#0070D2) 统一深浅底
6. **促销价**：`--color-promo-red` (#e74c3c)，仅用于 "Save $XX" 场景
7. **深底文字**：标题 `--color-text-primary-dark` (#fff)，正文 `--color-text-secondary-dark` (#999)
8. **无品牌强调色**：Sony 页面不使用橙/绿/紫装饰色，纯黑白灰 + 蓝色链接
