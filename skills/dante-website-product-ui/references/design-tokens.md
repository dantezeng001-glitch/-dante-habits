# Shokz Product Page — Design Tokens

所有 CSS 变量定义在 `:root` 中，全页共享。产品页以黑白灰为主调，产品图是页面唯一的色彩来源。

## CSS Variables

```css
:root {
    /* === Colors === */
    --black: #1a1a1a;
    --dark-gray: #2d2d2d;
    --mid-gray: #666;
    --light-gray: #f5f5f5;
    --white: #ffffff;
    --accent: #e8491d;        /* brand orange — 仅用于 NEW badge、highlight strip */
    --border: #eee;           /* 表格/分割线 */

    /* === Typography === */
    --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

    /* === Layout === */
    --max-width: 1200px;
    --section-padding: 80px 0;
    --container-px: 24px;     /* 容器左右 padding */
    --grid-gap: 60px;         /* 双栏 grid 间距 */
    --card-gap: 32px;         /* 多卡片 grid 间距 */
}
```

## Typography Scale

| 用途 | font-size | font-weight | line-height | 备注 |
|------|-----------|-------------|-------------|------|
| H1（产品名） | 36px | 700 | 1.2 | 全大写 |
| H2（section 标题） | 32px | 700 | 1.2 | — |
| H3（卡片标题） | 16–18px | 600 | 1.3 | — |
| Body（正文） | 16px | 400 | 1.7 | 颜色用 `--mid-gray` |
| Stat 大数字 | 48px | 800 | 1 | 颜色用 `--black` |
| Stat 标签 | 13px | 400 | 1.4 | 颜色用 `--mid-gray` |
| 小字/标签 | 13–14px | 500 | 1.5 | — |
| 按钮文字 | 16px | 600 | 1 | — |
| Badge 文字 | 11px | 600 | 1 | — |
| Footnote | 11px | 400 | 1.6 | 颜色 `#999` |
| Highlight strip | 13–15px | 500 | 1.3 | letter-spacing: 0.5px |

## Border Radius

| 元素 | radius |
|------|--------|
| 大卡片 / feature-visual | 16px |
| 中卡片 / stat-card / box-item | 12px |
| 小元素 / FAQ item / compare-table th | 8px |
| CTA 按钮 | 30px（胶囊型） |
| Badge | 4px |

## Spacing

| 场景 | 值 |
|------|-----|
| Section 垂直间距 | 80px top + bottom |
| Hero 垂直间距 | 60px top + bottom |
| 双栏 grid gap | 60px |
| 多卡片 grid gap | 32px |
| 标题到正文 | 16px |
| 正文段间距 | 16px |
| Stat 行距（stat → label） | 4px |
| FAQ item 间距 | 8px |
| Footnote 段间距 | 8px |

## Responsive Breakpoint

```css
@media (max-width: 768px) {
    /* 双栏 → 单栏 */
    .hero-grid, .feature-content { grid-template-columns: 1fr; gap: 32px; }
    .feature-content.reverse { direction: ltr; }
    /* 多列 → 单列 */
    .feature-grid { grid-template-columns: 1fr; }
    .stats-row { grid-template-columns: 1fr; }
    .highlight-items { gap: 24px; }
}
```

## Color Usage Rules

1. **CTA 按钮**：background `--black`，hover `--dark-gray`，文字 `--white`
2. **Section 背景交替**：奇数 section `--white`，偶数 section `--light-gray`
3. **Highlight strip**：background `--black`，文字 `--white`
4. **Compare table 表头**：background `--black`，文字 `--white`
5. **NEW badge**：background `--accent`，文字 `--white`
6. **正文二级文字**：`--mid-gray`
7. **Footnote 文字**：`#999`
8. **表格行 hover**：background `--light-gray`
9. **边框/分割线**：`--border` (#eee)
