# Apple Product Page — Design Tokens

白色主导 + 深黑交替的电影感节奏。产品图和链接蓝是页面仅有的色彩来源。

## CSS Variables

```css
:root {
    /* === Colors — Light Context === */
    --color-bg-white: #fff;
    --color-bg-light: #f5f5f7;
    --color-text-primary-light: #1d1d1f;
    --color-text-secondary-light: #6e6e73;
    --color-link-light: #0066cc;

    /* === Colors — Dark Context === */
    --color-bg-dark: #000;
    --color-bg-dark-alt: #1d1d1f;
    --color-text-primary-dark: #f5f5f7;
    --color-text-secondary-dark: #86868b;
    --color-link-dark: #2997ff;

    /* === Shared === */
    --color-footnote: #6e6e73;
    --color-btn-primary: #0071e3;
    --color-btn-primary-hover: #0077ed;

    /* === Typography === */
    --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display',
        'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    --font-size-display: clamp(48px, 7vw, 96px);
    --font-size-h1: clamp(40px, 5vw, 64px);
    --font-size-h2: clamp(32px, 4vw, 56px);
    --font-size-h3: clamp(24px, 3vw, 40px);
    --font-size-h4: clamp(19px, 2vw, 28px);
    --font-size-body: clamp(17px, 1.5vw, 21px);
    --font-size-caption: 12px;
    --font-size-stat: clamp(48px, 6vw, 96px);

    /* === Layout === */
    --max-width-content: 980px;
    --max-width-text: 700px;
    --max-width-full: 1440px;
    --section-gap: clamp(60px, 8vw, 120px);
    --padding-inline: max(22px, env(safe-area-inset-left, 22px));

    /* === Border Radius === */
    --radius-button: 980px;   /* 全圆角胶囊 */
    --radius-card: 18px;
    --radius-small: 8px;

    /* === Transitions === */
    --transition-fade: 0.6s cubic-bezier(0.28, 0.11, 0.32, 1);
    --transition-quick: 0.3s ease;
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| Display（Hero 标语） | clamp(48-96px) | 600 | 1.05 | 居中，深底白字 |
| H1（产品名） | clamp(40-64px) | 700 | 1.1 | 居中 |
| H2（Section 标题） | clamp(32-56px) | 600 | 1.1 | 居中或左对齐 |
| H3（子特性标题） | clamp(24-40px) | 600 | 1.15 | 左对齐 |
| H4（卡片标题） | clamp(19-28px) | 600 | 1.2 | 左对齐 |
| Body（正文） | clamp(17-21px) | 400 | 1.5 | max-width 700px 居中约束 |
| Caption（标签/脚注） | 12-14px | 400 | 1.4 | 灰色 |
| Stat 大数字 | clamp(48-96px) | 700 | 1 | 居中 |

## Border Radius

| 元素 | radius |
|------|--------|
| Primary 按钮 | 980px（全圆角胶囊） |
| 卡片 / shelf card | 18px |
| 小元素 / 标签 | 8px |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 间距 | clamp(60px, 8vw, 120px) |
| Hero 最小高度 | 100vh |
| 容器左右 padding | max(22px, safe-area) |
| 正文最大宽度 | 700px（居中约束） |
| 内容最大宽度 | 980px |
| 全宽元素最大宽度 | 1440px |
| 标题到正文 | 16-24px |
| 卡片内 padding | 30px |
| Shelf 卡片 gap | 20px |

## Responsive Breakpoints

```css
@media (max-width: 1068px) {
    /* 平板横屏：缩小字号、调整网格列数 */
    .hero h1 { font-size: 48px; }
    .shelf__card { flex: 0 0 calc(50% - 10px); }
}
@media (max-width: 734px) {
    /* 手机：单列布局、堆叠排列 */
    .split { grid-template-columns: 1fr; }
    .shelf__card { flex: 0 0 85%; }
    .card-grid { grid-template-columns: 1fr; }
}
```

## Color Usage Rules

1. **深浅交替**：营销页特性区块交替 `--color-bg-dark` / `--color-bg-light`，制造电影感节奏
2. **购买页**：全程浅色背景（`--color-bg-white` / `--color-bg-light`）
3. **深底文字**：标题用 `--color-text-primary-dark`，正文用 `--color-text-secondary-dark`（降对比度）
4. **浅底文字**：标题用 `--color-text-primary-light`，正文用 `--color-text-secondary-light`
5. **链接**：深底用 `--color-link-dark` (#2997ff)，浅底用 `--color-link-light` (#0066cc)
6. **CTA 按钮**：蓝底白字 (`--color-btn-primary`)，非黑底
7. **Hero 背景**：纯黑 `--color-bg-dark`，产品图悬浮
8. **无品牌强调色**：不使用橙/红/绿装饰色
