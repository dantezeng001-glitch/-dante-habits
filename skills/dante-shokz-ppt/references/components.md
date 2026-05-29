# Components · 11 类组件

> 每个组件对应 [`assets/snippets/`](../assets/snippets/) 下的一个 HTML 文件。**整段复制 snippet 到你的 `<section>` 里**，只改"可改字段"，不动数值。

snippet 复制 → 改文字 → 完成。这是 mid_eng 工程化的核心收益。

---

## 速查表

| # | 组件 | 文件 | 何时用 | 来源页 |
|---|------|------|--------|--------|
| 1 | 页眉 chrome | [`snippets/header-chrome.html`](../assets/snippets/header-chrome.html) | 每页（封面除外）顶部 | 所有页 |
| 2 | 页脚 chrome | [`snippets/footer-chrome.html`](../assets/snippets/footer-chrome.html) | 每页底部 | 所有页 |
| 3 | 封面 | [`snippets/cover.html`](../assets/snippets/cover.html) | P01 / 首页 | P01 |
| 4 | 章节分隔 | [`snippets/section-divider.html`](../assets/snippets/section-divider.html) | 大章节切换 | （可选） |
| 5 | STAR 卡 | [`snippets/star-card.html`](../assets/snippets/star-card.html) | 案例分析 | P06 / P08 |
| 6 | 9-cards Overview | [`snippets/case-overview-9-cards.html`](../assets/snippets/case-overview-9-cards.html) | 多任务/多项目全景 | P05 |
| 7 | 时间线 4 列 | [`snippets/timeline-4col.html`](../assets/snippets/timeline-4col.html) | 成长/迁移叙事 | P02 |
| 8 | 三栏 GOAL-ACTION-METRIC | [`snippets/three-column-goal-action-metric.html`](../assets/snippets/three-column-goal-action-metric.html) | 未来规划 / OKR | P11 |
| 9 | 三层涟漪 | [`snippets/ripple-3-layer.html`](../assets/snippets/ripple-3-layer.html) | 影响力扩散 | P09 |
| 10 | 关键变化卡 | [`snippets/change-card.html`](../assets/snippets/change-card.html) | 个人成长反思 | P15 |
| 11 | 复盘条 + inline 徽章 + 数据卡 | [`snippets/retro-bar.html`](../assets/snippets/retro-bar.html) [`snippets/inline-badge.html`](../assets/snippets/inline-badge.html) [`snippets/data-card-with-status.html`](../assets/snippets/data-card-with-status.html) | 嵌套用 | 多处 |

---

## 1. 页眉 chrome

**位置**：`top: 32px, left: 96px`

**用途**：每页左上角标注当前位置。语法：`<中文> · <ENGLISH>`，全大写英文。

**可改字段**：
- 中文区段名："个人简介"、"案例 ① · 月银白 SOP · 上半页"、"未来规划"
- 英文区段名："PROFILE"、"CASE 01 · STA"、"FUTURE PLAN"

**不可改**：`top: 32px`、字号 `11pt`、色 `#666666`、字体 `Consolas, 'Courier New', monospace`

---

## 2. 页脚 chrome

**位置**：左 `top: 674px, left: 96px`，右 `top: 674px, left: 1123.47px`

**两段固定内容**：
- 左：`Shokz 韶音 · BE OPEN`（公司口号，每页都一样）
- 右：`NN / 总数`（当前页 / 总页数，需要手动递增）

**可改字段**：右侧的页码（如 `02 / 16`）

**不可改**：左侧文字、所有数值、`#666666` 色

---

## 3. 封面

**结构**：
- 整页白底
- 左上 `SHOKZ · PMKT ·` 标签（11pt 等宽）
- 右上 presenter 英文名（11pt 等宽）
- 中央竖向橙色色条 `#FF7A3D`（8×74.66px）+ 紧邻一行小标题（"试用期答辩"/"产品上市策划"等）
- 主标题大字（60pt，黑+橙混色强调关键词）
- 中部 1088×528 的浅边框容器（仅作视觉框）
- 底部 PRESENTER 行（小标 + 姓名）+ DATE 行（右对齐）

**可改字段**：
- 顶部标签（场景说明）
- 主标题（60pt，黑+橙混色，最多 8 个汉字最佳）
- 副标题 / 场景描述
- presenter 中英文名（黑色 22pt 加粗）
- 角色描述："Shokz 韶音 · 北美业务部 · 产品营销"（16pt 灰色）
- 日期：`YYYY / MM`

**不可改**：橙色竖条位置（`left: 118.86, top: 251.38`）、所有 left/top/width/height

---

## 4. 章节分隔（可选）

**结构**（原 deck 没有专门的章节页，但留位）：
- 整页 `#050505` Ink 底
- 中央大字（章节名，48-60pt 白字 + 橙色编号）
- 右下角"NN / 总数"页码（白色，11pt 等宽）

**适用**：deck > 12 页时，每个大主题之间插一页分隔。本 skill **不强制**用章节分隔——原 deck 16 页就没用。

---

## 5. STAR 卡

**结构**（来自 P06/P08）：

每个 S/T/A/R 都是"黑色头部 + 灰色 body"两块叠放：
- **黑头**：`#050505` 底，高 `103.66px`（大头）或 `50px`（紧凑头）
  - 左侧 26-48pt 白色大字母（S/T/A/R）
  - 右侧两行：上面是橙色英文标签（`SITUATION` / `TASK` / `ACTION` / `RESULT`）+ 下面是中文译名（背景 / 任务 / 行动 / 结果）
- **灰 body**：`#F1F1F1` 底，包含正文卡片
  - 主标题行（14-16pt，黑色加粗）
  - 编号项目列表（① ② ③，橙色加粗 + 黑色正文）

**两种排法**：
- **三栏并列 STA**（P06）：S / T / A 各占 1/3，下方 R 占整页一行
- **二栏 STAR**（P08）：左 320 的 S/T 上下堆 + 右 748 的 A，R 单独成页

**可改字段**：标题、副标题、列表项内容（保留 ① ② ③ 编号）

**不可改**：S/T/A/R 字母、英文标签、配色、列宽

---

## 6. 9-cards Overview

**结构**（来自 P05）：

```
+--------+-------+-------+-------+
| Anchor | Card  | Card  | Card  |  ← 第 1 类
| 类别 1 |  01   |  02   |  03   |
+--------+-------+-------+-------+
| Anchor | Card  | Card  | Card  |  ← 第 2 类
| 类别 2 |  04   |  05   |  06   |
+--------+-------+-------+-------+
| Anchor | Card  | Card  | Card  |  ← 第 3 类
| 类别 3 |  07   |  08   |  09   |
+--------+-------+-------+-------+
```

- 左侧 3 个 Anchor（240×140）：英文类别名 + 中文类别名 + 大数字（件数） + 副说明
  - 每个 Anchor 不同浅底色：橙系（`#FFF1EA`）/ 灰系（`#E8E8E8`）/ Ink 黑（突出最重要类）
- 右侧 9 张数据卡（262×140）：每张顶部 ID `01-09` + 状态徽章 `DONE/WIP/LIVE`+ 中文卡名 + 一行任务说明 + 底部 detail
- 底部图例（11pt）

**可改字段**：类别名、件数、卡片内容、状态

**不可改**：左侧 240 锚点宽、右侧 262 卡宽、行高 140、垂直间距、ID 编号位

---

## 7. 时间线 4 列

**结构**（来自 P02）：

```
[era 1 date] [era 2 date] [era 3 date] [era 4 date]
[era 1 name] [era 2 name] [era 3 name] [era 4 name]
————————o————————o————————o————————■  ← 圆点轴
[era 1 desc] [era 2 desc] [era 3 desc] [era 4 desc]

[━━━━━━ Mental Journey 面板 ━━━━━━━━━━]
[col1: 3 boxes ↓] [col2 ↓] [col3 ↓] [col4 ↓]
```

- 4 列日期标签（Era 色背景：白灰 `#E5E5E5` → 淡蓝 `#DBE3EC` → 淡橙 `#F4D9BC` → Ink 黑）
- 4 列 Era 名（22pt 加粗）
- 圆点轴：3 段灰色细线 + 3 个 Ink 圆点 + 末尾 1 个橙色当前位置方块
- 4 列描述（13pt）
- 下方"心路历程"面板：浅灰 `#F1F1F1` 底，4 列 × 3 行心路 box

**可改字段**：日期、Era 名、描述、3 行心路文字

**不可改**：列宽（208/257/208/208）、Era 色顺序（如要表达"当前位置"，最后一列必须用 Ink 底）

---

## 8. 三栏 GOAL-ACTION-METRIC

**结构**（来自 P11）：

每栏白底 + 浅边框（`0.75pt solid #BABABA`）：
- 顶部大编号 `01 / 02 / 03`（36pt 橙色等宽）+ 旁边英文小标签（`DEEPEN` / `TRANSFORM · AI` / `CULTURE`）
- 标题行（18pt 加粗）："深入业务" / "改造业务 · AI" / "文化活动 · 双百"
- 分隔线
- `GOAL` 段（9pt 等宽小标 + 12pt 正文，含 ① ② 编号）
- 分隔线
- `ACTION` 段（同上）
- 分隔线
- `METRIC` 段（同上）

**可改字段**：编号、英文小标、标题、GOAL/ACTION/METRIC 各段内容

**不可改**：三栏宽 350.22 / 列间距、栏内分隔线位置、`GOAL/ACTION/METRIC` 这三个固定标签词

---

## 9. 三层涟漪

**结构**（来自 P09）：

整页顶部一个全宽 80px 黑色 `R` 大字 + 大字标题（结果总述）

下方三栏（350.22 / 350.22 / 350.22）：
- 每栏顶部一根 3pt 粗 border（不同色：灰 → 中灰 → 橙，表示扩散范围递增）
- 每栏内部：英文小标 `LAYER 01 · 部门内` / `LAYER 02 · 跨部门` / `LAYER 03 · 公司级`
- 中文标题（16pt 加粗）
- 12pt 正文段落（用橙色加粗强调关键词）

**可改字段**：三层名（不一定非要"部门内/跨部门/公司级"，可换为"个人/团队/组织"）、标题、正文

**不可改**：栏顶 3pt border 配色顺序（灰→中灰→橙表示"由近及远 / 由小到大"，反过来视觉错乱）

---

## 10. 关键变化卡

**结构**（来自 P15）：

整页两到三张全宽（1088×131.56）卡片纵向堆叠，每张白底 + `0.75pt solid #BABABA` 边框：
- 左侧 48pt 橙色大编号 `01 / 02 / 03`（等宽字体）+ 下方 10pt 灰色英文状态（`FORMED` / `SHAPING` / `EMERGING`）
- 中部分隔细线（垂直 0.75pt）
- 右侧：19pt 主标题（黑色 + 橙色 quoted 强调）+ 两行 12pt takeaway

**可改字段**：编号、英文状态词、主标题、takeaway

**不可改**：卡片高度、左侧编号宽 87px、分隔线位置

---

## 11. 嵌套用小组件

### 11.1 复盘条（retro-bar）

橙色边框白底全宽条（1088×80），左侧橙色徽章 `RETRO · 复盘`（10pt 等宽白字），右侧 13pt 正文带橙色加粗强调词。

**用途**：每个案例页底部加一行复盘金句。

### 11.2 inline 徽章

两种：
- `思考`：黑底 `#050505` + 白字 7pt 等宽
- `任务`：橙底 `#FF7A3D` + 白字 7pt 等宽

**用法**：直接 inline 在段落里：`[思考] 边做边固化 —— 把一次性流程当成可复用资产做`

### 11.3 数据卡（带状态徽章）

通用数据卡（262×140 或可变宽）：
- 顶行：左 8.5pt 等宽 ID（`01`）+ 右 8.5pt 等宽状态徽章（`DONE` 橙底白字 / `WIP` 灰底白字）
- 中部：12pt 加粗标题
- 9pt 灰色副说明
- 底部分隔线 + 9.5pt 任务描述

**适用**：在 9-cards、产品列表、TODO 看板、知识库索引等场景里复用。

---

## 12. 组件红线

- ❌ 在一个组件内套用另一个组件的"黑头部"（如把 STAR 黑头放进 9-cards 里）—— 黑头是 STAR 专属语言
- ❌ 改组件的 `width` / `height` 配比（如把 STAR 三栏 350 改成 400 试图塞更多字）—— 重写而不是改
- ❌ 给组件加 `border-radius`、`box-shadow`、`gradient` —— 违反平面工程美学
- ❌ 替换组件内英文标签为 emoji 或 icon（如把 `SITUATION` 换成 `🎯`）
- ❌ 在一页同时用 ≥ 4 个不同组件——视觉过载，应该拆页
