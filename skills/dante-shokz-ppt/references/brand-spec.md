# Brand Spec · Shokz 韶音

> 单一真源。所有色值、字号、字体堆栈必须从这里查表，不发明新值。

来源：从 [`example/转正答辩_v3_动画版.html`](../example/转正答辩_v3_动画版.html) 抽出的实际使用值。

---

## 1. 色板（10 个值，全部）

### 1.1 主色（强制）

| 角色 | HEX | 用途 |
|------|-----|------|
| **Shokz Orange** | `#FF7A3D` | 主色强调、徽章底、关键词突出、活跃状态点 |
| **Ink** | `#050505` | 主文本、强调块底色、深色 STAR 头部 |

### 1.2 灰阶（强制）

| 角色 | HEX | 用途 |
|------|-----|------|
| Subdued Ink | `#2F2F2F` | 次要文本（非主标题但需要黑） |
| Mute | `#666666` | 副标题、英文标签、辅助说明 |
| Light Mute | `#999999` | 极次要辅助（timeline 箭头 / 卡片 ID 数字） |
| Divider | `#BABABA` | 分隔线 / 浅边框 |
| Border | `#E5E5E5` | 淡卡片边框 |
| Surface | `#F1F1F1` | 卡片背景 / 默认浅块底 |
| Tint Gray | `#E8E8E8` | 类别锚点浅底（如"科技树"类） |
| White | `#FFFFFF` | 主背景 / Ink 块上文本 |

### 1.3 Era 色（仅用于时间线/分类区分，不作主色）

| 角色 | HEX | 何时用 |
|------|-----|------|
| Pale Blue | `#DBE3EC` | 时间线/分类的"中段 era"标签底（如读 CMU / 美国阶段） |
| Pale Orange | `#F4D9BC` | 时间线/分类的"上一份工作 era"（如隆基阶段） |
| Tint Orange | `#FFF1EA` | 与橙色主色相关的类别浅底（如"产品上市"类锚点） |

> Era 色只在 `timeline-4col` / `case-overview-9-cards` 等"多列分类"场景里用，**不要拿来填卡片背景代替 `#F1F1F1`**。

### 1.4 禁区

- ❌ 紫色 / 蓝紫渐变 / 赛博霓虹 / 任何 `purple/violet/indigo` 色系
- ❌ 任何渐变色（`linear-gradient`、`radial-gradient`）——Shokz 体系是平涂
- ❌ 临场发明的"接近 Shokz Orange 的色"（`#FF6E2F`、`#FF8848` 等）
- ❌ 多个橙色变体（暗橙、亮橙、橙黄、橙红）——只有 `#FF7A3D` 一个橙
- ❌ 蓝色 / 绿色 / 红色作为强调色（Era 色除外）
- ❌ 黑色用纯 `#000000`（应该用 `#050505`，避免在纯黑边缘出现摩尔纹）

---

## 2. 字体堆栈（强制，不替换）

### 2.1 中文 body（默认正文）

```css
font-family: "Noto Sans SC","Microsoft YaHei","PingFang SC","Noto Sans",system-ui,sans-serif;
```

> 顺序逻辑：Noto Sans SC 是 Google 跨平台中文首选 → Win 兜底微软雅黑 → Mac 兜底苹方 → 拉丁字符 Noto Sans → 最后系统 ui。**这个顺序不要动**。

### 2.2 等宽标签（"中文 · ENGLISH" 里的英文部分、编号、页码、状态徽章）

```css
font-family: 'Consolas','Courier New',monospace;
```

> 用于：页眉 `SHOKZ · PMKT · 个人简介 · PROFILE` 这种、页脚页码 `01 / 16`、状态 `DONE / WIP`、卡片 ID `01-09`、SITUATION/TASK/ACTION/RESULT 标签。

### 2.3 反 slop 红线

- ❌ `Inter` / `Roboto` / `Arial` / `SF Pro` 作 display
- ❌ 衬线字体（Newsreader / Source Serif / EB Garamond）—— Shokz 是无衬线工程美学
- ❌ 用 emoji 替代字体（如 `🚀 火箭` 代替"启动"）

---

## 3. 字号体系（8 档）

> 一律用 `pt` 单位（原 deck 从 PPT 转换而来）。8 档之外的字号不要用，遇到不合适时**改组件而不是改字号**。

| 档 | 字号 | weight | 用途 | 例子 |
|---|---|---|---|---|
| **Display** | 60-156pt | 700 | 封面主标 / 章节巨字 / 致谢 | "学习业务 改造业务" / "致谢" |
| **H1** | 36pt | 700 | 页主标题 | "案例一：OpenRun Pro 2 月银白上市" |
| **H2** | 22pt | 700 | 二级标题 / Era 名 / 大数字 | "北京科技大学" / "9" / "4" |
| **H3** | 16-18pt | 700 / 400 | 段落标题 / 大块描述 | "9 件事 3 大类" / 关键变化的标题行 |
| **Body Lead** | 13-14pt | 400 | 段落正文（重点页） / 副标题 | 卡片正文 / 副标 "9 件事 · 3 大类 · 按节点推进" |
| **Body** | 11-12pt | 400 | 表格内 / 数据卡正文 / 卡片细则 | 对照表内容 / 数据卡描述行 |
| **Caption** | 11pt | 400 | **强制：所有页眉、页脚、等宽英文标签都是 11pt** | `案例 ① · 月银白 SOP` / `Shokz 韶音 · BE OPEN` / `01 / 16` |
| **Micro** | 9-10pt | 400 | 状态徽章 / 表头 / 卡片 ID / 极小英文 | `DONE` / `WIP` / `01` / `SITUATION` |
| **Tag** | 7-8.5pt | 700 | inline 思考-任务徽章、卡片角标 | inline `思考` / `任务` 小标 |

### 3.1 速查

- 想做"封面/章节巨字" → 60pt+
- 想做"页主标题" → 36pt
- 想做"页眉/页脚" → 11pt 等宽
- 想做"正文" → 12-13pt
- 想做"inline 强调小徽章" → 7pt 等宽 + bold

### 3.2 行距（line-height）

| 用途 | line-height |
|---|---|
| 默认 `.pp` 段落 | `1.15` |
| 内容密集卡片正文 | `1.32` 或 `1.35` |
| 高密度表格 | `1.5` |
| Body Lead 段落 | `1.55` |
| 极简强调（如 Display） | `1` 或 `1.1` |

---

## 4. 字重与样式

- `font-weight: 700` 表示加粗，**没有 600 / 500 / 800 这些中间值**——只有 400 和 700 两档
- `font-style: italic` 不在体系内，不要用
- `text-decoration: underline` 不在体系内，强调用粗体或橙色，不用下划线
- `letter-spacing` 仅在等宽英文标签里偶尔用 `0.5px-1px`，中文不用

---

## 5. 装饰与几何元素

### 5.1 边框

- 浅边框：`0.75pt solid #BABABA` 或 `1px solid #E5E5E5`
- 强调边框：`1.5pt solid #FF7A3D`（橙色框）或 `2px solid #FF7A3D`（更粗的强调框）
- 顶/底/左 单边粗 border 表示"分类色条"：`border-top: 3.0pt solid #FF7A3D`（涟漪卡顶部）/ `border-left: 3px solid #FF7A3D`（类别锚点左侧）
- **不用 `border-radius`**——所有元素都是直角矩形

### 5.2 阴影

只有外层 `.deck-slide` 有 `box-shadow: 0 8px 30px rgba(0,0,0,0.45)` 让幻灯片在深灰背景上漂浮。**deck 内的元素不要加 shadow**。

### 5.3 圆点 / 箭头

- 圆点：`width: 10.66px; height: 10.66px; background: #050505;`（timeline 节点）
- 当前位置标记：`16×16` 橙色方块（`#FF7A3D`）
- 箭头：用 unicode `↓` `→`，字号 14pt / 28pt，色 `#999999` 或 `#FF7A3D`

---

## 6. 背景

- 整个 body：`#2a2a2a`（深灰，让白色 deck 漂浮）
- 每页 `.deck-slide`：`#FFFFFF`（默认白）
- 强调页（如章节分隔 / 致谢页）：可整页 `#050505` Ink 底

---

## 7. 速查代码（CSS 变量版）

> 如果想在新 deck 里用 CSS 变量统一管理，把这一段放进 `<style>` 头部：

```css
:root {
  /* 主色 */
  --shokz-orange: #FF7A3D;
  --ink: #050505;

  /* 灰阶 */
  --ink-subdued: #2F2F2F;
  --mute: #666666;
  --mute-light: #999999;
  --divider: #BABABA;
  --border-light: #E5E5E5;
  --surface: #F1F1F1;
  --tint-gray: #E8E8E8;

  /* Era */
  --pale-blue: #DBE3EC;
  --pale-orange: #F4D9BC;
  --tint-orange: #FFF1EA;

  /* 字体 */
  --font-cn: "Noto Sans SC","Microsoft YaHei","PingFang SC","Noto Sans",system-ui,sans-serif;
  --font-mono: 'Consolas','Courier New',monospace;
}
```

> 但是注意：[`assets/deck.css`](../assets/deck.css) 已经导出了这套变量，新 deck 直接 link 它，不需要再重复定义。
