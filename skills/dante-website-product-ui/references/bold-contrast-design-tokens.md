# Bold Contrast Style — Design Tokens

> 近似品牌：Beats / Marshall

深色主导、高对比、产品配色驱动。标题字重极粗，数据大字报是核心视觉锤。

## CSS Variables

```css
:root {
    /* === Colors === */
    --color-bg-dark: #0c0c0c;
    --color-bg-dark-alt: #1a1a1a;
    --color-bg-light: #f5f5f5;
    --color-bg-white: #ffffff;
    --color-text-primary-dark: #ffffff;
    --color-text-secondary-dark: #a0a0a0;
    --color-text-primary-light: #1a1a1a;
    --color-text-secondary-light: #666;
    --color-accent: #e4002b;       /* Beats red — 仅用于 logo / hover 等极少场景 */
    --color-border: #333;
    --color-border-light: #e0e0e0;

    /* === Typography === */
    --font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue',
        Helvetica, Arial, sans-serif;

    /* === Layout === */
    --max-width: 1200px;
    --max-width-narrow: 800px;
    --section-padding: 80px 0;
    --section-padding-large: 120px 0;
    --container-px: 24px;
    --grid-gap: 48px;
    --card-gap: 24px;

    /* === Border Radius === */
    --radius-button: 30px;
    --radius-card: 16px;
    --radius-small: 8px;

    /* === Transitions === */
    --transition-standard: 0.3s ease;
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| H1（产品名） | 40-48px | 800 (Black) | 1.1 | 购买区 |
| Hero 标语 | 24-32px | 500 | 1.3 | 产品名下方 |
| H2（章节主标题） | 36-48px | 700 | 1.15 | 居中 |
| H3（功能子标题） | 20-28px | 600 | 1.25 | 居中或左对齐 |
| Body（正文） | 16-18px | 400 | 1.6 | 每段 ≤ 3 句 |
| Data Number（大字报数字） | 48-72px | 800 | 1 | 超大展示 |
| Data Label（大字报注释） | 14px | 400 | 1.4 | `--color-text-secondary-*` |
| Category Tag（类目标签） | 12-13px | 600 | 1.3 | 全大写，letter-spacing: 2px |
| Feature Strip Item | 13-14px | 500 | 1.3 | 功能速览条 |
| Button 文字 | 16px | 600 | 1 | 全大写 |
| Badge | 11px | 600 | 1 | 全大写 |

## Border Radius

| 元素 | radius |
|------|--------|
| CTA 按钮 | 30px |
| 卡片 / 引用块 | 16px |
| 小元素 / FAQ item | 8px |
| 色彩 swatch | 50%（圆形） |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 垂直间距 | 80-120px |
| 购买区 padding | 48px 0 |
| 功能速览条 padding | 32px 0 |
| 章节内 grid gap | 48px |
| Feature strip item gap | 32px |
| 标题到正文 | 16px |
| Category tag 到 H2 | 12px |
| 大字报数字到注释 | 8px |
| FAQ item 间距 | 8px |

## Responsive Breakpoints

```css
@media (max-width: 1024px) {
    .buy-panel { grid-template-columns: 1fr; }
    .feature-strip-items { flex-wrap: wrap; justify-content: center; }
}
@media (max-width: 768px) {
    .feature-split { grid-template-columns: 1fr; gap: 32px; }
    .feature-strip-items { gap: 16px; }
    .data-callout .number { font-size: 48px; }
}
```

## Color Usage Rules

1. **深浅强交替**：深色 section（`--color-bg-dark`）和浅色 section（`--color-bg-white`）交替使用，对比度高于 Apple
2. **产品配色驱动**：选中的产品颜色渗透到购买区背景、章节背景渐变中
3. **CTA 按钮**：深底用白色填充按钮；浅底用黑色填充按钮。文字全大写
4. **Category Tag**：全大写、字间距加宽、小字号，置于 H2 上方
5. **Beats Red**（#e4002b）极少使用——仅 logo 和 hover 状态，不做装饰色
6. **三项承诺条**：白底黑字，带图标
7. **数据大字报**：数字用 `--color-text-primary-*`，注释用 `--color-text-secondary-*`
