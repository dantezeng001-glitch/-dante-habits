# Data Spectacle Style — Design Tokens

> 近似品牌：OPPO / Huawei / Soundcore / Oladance

全暗沉浸式底色，白字高对比，产品色是唯一色彩变量。数据大字报数字为所有风格中最大（64-120px）。代表品牌：OPPO、华为、Soundcore、Oladance、Cleer。

## CSS Variables

```css
:root {
    /* === Colors === */
    --bg-primary: #000000;
    --bg-secondary: #111111;
    --bg-tertiary: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: #999999;
    --text-body: #bbbbbb;
    --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --cta-primary: #1a1a1a;
    --cta-text: #ffffff;
    --border: #333333;
    --footnote: #666666;
    --product-color: #ffffff;  /* 由具体产品覆盖 */

    /* === Typography === */
    --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
        'Helvetica Neue', Arial, sans-serif;

    /* === Layout === */
    --max-width: 1200px;
    --max-width-narrow: 800px;
    --section-padding: 100px 0;
    --section-min-height: 100vh;
    --container-px: 24px;
    --grid-gap: 48px;
    --card-gap: 24px;

    /* === Border Radius === */
    --radius-button: 32px;
    --radius-card: 16px;
    --radius-card-large: 20px;
    --radius-small: 8px;
    --radius-pill: 100px;

    /* === Transitions === */
    --transition-standard: 0.3s ease;
    --transition-slow: 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| H1（Hero 产品名） | 48-72px | 700-800 | 1.05 | 居中，全暗背景上白字 |
| Data Number（大字报数字） | clamp(64px, 10vw, 120px) | 800 (Extra Bold) | 1 | **所有风格中最大**，核心视觉锤 |
| Data Label（大字报注释） | 14-16px | 400 | 1.4 | `--text-secondary` |
| Data Basis（对比基准） | 12-13px | 400 | 1.4 | `--footnote` |
| H2（章节主标题） | 36-48px | 700 | 1.15 | 居中 |
| H3（功能子标题） | 24-32px | 600 | 1.25 | 居中或左对齐 |
| Body（正文） | 16-18px | 400 | 1.7 | `--text-body`，浅灰色 |
| Tech Pills | 12-14px | 500 | 1 | 圆角胶囊，border: 1px solid var(--border) |
| Tech Version Badge | 13-14px | 600 | 1.3 | 小号标签 "ANC 3.0" |
| CTA Button | 16-18px | 600 | 1 | 按品牌区分：部分全大写，部分标准 |
| Caption / Footnote | 12-14px | 400 | 1.5 | `--footnote` |
| Comparison Bar Label | 13-14px | 500 | 1.3 | 进度条旁标注 |

## Border Radius

| 元素 | radius |
|------|--------|
| CTA 按钮 | 30-40px（因品牌而异） |
| 卡片 / 功能板块 | 16-20px |
| Tech Pill / Badge | 100px（胶囊形） |
| 小元素 / FAQ item | 8px |
| 比较进度条 | 4px |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 垂直间距 | 80-120px |
| Section 最小高度 | 100vh（一屏一功能） |
| Hero padding | 120-160px 0 |
| 章节内 grid gap | 48px |
| Tech pills bar gap | 12-16px |
| 标题到正文 | 16-24px |
| 大字报数字到注释 | 8px |
| 对比条间距 | 16-20px |
| FAQ item 间距 | 0（border-bottom 分隔） |
| Footnotes 间距 | 6-8px per item |

## Responsive Breakpoints

```css
@media (max-width: 1024px) {
    :root {
        --section-min-height: auto;
    }
    .feature-full-screen { min-height: auto; padding: 80px 0; }
    .data-callout-grid { grid-template-columns: repeat(2, 1fr); }
    .feature-split { grid-template-columns: 1fr; gap: 32px; }
    .compare-table { overflow-x: auto; }
}

@media (max-width: 768px) {
    .hero h1 { font-size: 36px; }
    .hero .subtitle { font-size: 18px; }
    .data-number { font-size: 48px; }
    .data-callout-grid { grid-template-columns: 1fr; gap: 32px; }
    .tech-pills { flex-wrap: wrap; justify-content: center; }
    .predecessor-comparison { flex-direction: column; }
    .certification-logos { flex-wrap: wrap; gap: 24px; }
}
```

## Color Usage Rules

1. **全暗沉浸**：整个页面以 `--bg-primary` (#000) 为主基调，交替使用 `--bg-secondary` (#111) 和 `--bg-tertiary` (#1a1a1a) 制造层次——不使用浅色背景 section
2. **产品色是唯一变量**：`--product-color` 由具体产品定义（如 Soundcore 蓝、OPPO 绿），渗透到 CTA、渐变光效、accent 元素
3. **文字三级灰度**：标题 #fff → 正文 #bbb → 辅助/脚注 #999/#666
4. **CTA 按钮**：因品牌而异——黑底白字（华为）、品牌色填充（Soundcore）、白底黑字（Oladance）
5. **渐变光效**：Soundcore 风格偶尔使用 `--accent-gradient` 做背景光晕，其他品牌克制使用
6. **数据大字报**：数字用 `--text-primary`，注释用 `--text-secondary`，对比基准用 `--footnote`
7. **边框与分隔线**：`--border` (#333) 用于 FAQ 分隔、Tech pills 边框、表格线
