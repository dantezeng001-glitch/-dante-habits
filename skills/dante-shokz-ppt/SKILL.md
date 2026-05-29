---
name: Dante Shokz PPT
description: Dante 在 Shokz（韶音）做任何内部 PPT 的统一 skill——汇报 / 答辩 / 培训 / 产品上市 / 案例复盘 / 路演 / 双周会 / OKR 评审。锁定 Shokz 品牌色（Orange #FF7A3D + Ink #050505）、1280×720 画布、"中文 · ENGLISH" 双语眉头、11 类核心组件（STAR 卡 / 9-cards / 时间线 / 三层涟漪 / GOAL-ACTION-METRIC / 复盘条 / 思考-任务徽章）和 7 种叙事框架（STAR、STAR+WARNING、9-cards 全景、时间线+心路、三层涟漪、GOAL-ACTION-METRIC、FORMED-SHAPING）。当用户说"做 PPT / 汇报 / 答辩 / slides / 复盘 / 上市策划 / case study"且属 Shokz 内部场景，或显式说"用 Dante Shokz 模板"、"按 Shokz 品牌做"、"按转正答辩那套样式"时使用。
---

# Dante Shokz PPT

> 你是 Dante 在 Shokz 内部出 PPT 的专用搭子。**不是从零设计**——是拿这套已经验过场的版式骨架 + 11 个 snippet + 7 个叙事框架，把用户给到的内容稿/讲稿/brief 拼装成一份能直接上场的单 HTML deck。

---

## 1. 触发与边界

### 1.1 适用场景

只要满足下面任一条件就用本 skill：

- 用户在 Shokz / 韶音 / PMKT / 北美营销 上下文里要 PPT
- 用户提到具体产品（OpenSwim Pro / OpenRun Pro 2 / OpenFit Pro / OpenSwim / OpenRun / NCE / XS / 骨传导 / 开放式声学）
- 用户提到 Shokz 内部叙事词（试用期答辩 / 转正答辩 / 双百 / 科技树 / IMC / GTM / Skill 包 / 信息通）
- 用户显式说"按转正答辩那套来"、"用 Dante Shokz 模板"、"延续之前的视觉"

### 1.2 不适用场景

- **外部对客户的物料**（落地页 / EDM / 海外广告）→ 走通用 frontend-design / huashu-design
- **演讲动画 / 发布会视频**（要 motion + SFX + BGM）→ 走 huashu-design
- **打印物 / 海报 / 包装** → 不是 1280×720 横版 deck 的场景

### 1.3 这个 skill 不替你做什么

- 不替你想内容。**内容稿是用户输入**——本 skill 只管"内容如何被排出来"
- 不替你做产品图。涉及具体产品时用户必须给真实产品图（详见 §4 资产协议）
- 不替你做信息收集 / 检索 / 研究——那是 ppt-agent 的 Step 2A 干的事，本 skill 默认内容已就绪

---

## 2. 工作流（7 步主链）

每一步对应一个停顿点。**不要一口气把 7 步跑完再 show**——走 Junior pass：跑到第 3 步就 show 分镜给用户认，再往下。

### Step 1 · 场景识别 + 取内容稿

- 问清楚：什么场景？多少页预算？讲多久？谁看？
- 取内容稿——优先要 `.md` 格式的逐页文案；其次是讲稿；最次是一句话 brief
- **如果用户只给 brief**：先帮他把逐页文案稿写出来，让他确认后再往下，**不要带着没确认的内容直接做版**

### Step 2 · 叙事选型

读 [`references/narrative-frameworks.md`](references/narrative-frameworks.md)，从 7 种里挑 1-N 个匹配的：
- 答辩 / 复盘 → STAR + STAR+WARNING + FORMED-SHAPING
- 产品上市策划 → 9-cards + GOAL-ACTION-METRIC + STAR
- 培训 / 课件 → 时间线+心路 + 三层涟漪
- 路演 / 个人介绍 → 时间线+心路 + FORMED-SHAPING + STAR

### Step 3 · 分镜（必须 show 给用户认）

输出一张分镜表：第 N 页 / 用哪个叙事框架 / 对应内容稿哪一节 / 用哪些 snippet。**写完 stop**，等用户认。

```
P01 · 封面 · cover.html · 主题"X"
P02 · 个人简介 · timeline-4col.html · 内容稿 §1
P03 · ...
```

### Step 4 · 起手骨架

拷贝 [`assets/deck-skeleton.html`](assets/deck-skeleton.html) → 用户工作目录 → 改名（例如 `2026Q2-OpenRun-launch.html`）。这是空白外壳：含 `<head>` 样式引用、翻页脚本、`<div class="deck-wrap">` 包裹。

### Step 5 · 拼装每页

读 [`references/components.md`](references/components.md)，按分镜表挑对应 snippet，**整段复制** 到 deck 里，**只改 inner 文字 + 必要的颜色 token**——不要改组件的 left/top/width/height 数值（那是版式锁，改了就和原品牌不一致）。

### Step 6 · 自检

过 [`references/deck-page-checklist.md`](references/deck-page-checklist.md)：
- 每页有页眉（左侧"中文 · ENGLISH"）和页脚（左 `Shokz 韶音 · BE OPEN`、右 `NN / 总数`）
- 页码连续，不跳号
- 主色只用 `#FF7A3D` 和 `#050505`，不发明新色
- 密度合理（参考 [`references/layout-grid.md`](references/layout-grid.md) 的密度区间）

### Step 7 · 目检

浏览器打开，用 ↑↓ 翻一遍，看每页：
- 文字有没有溢出 `.deck-slide` 边界
- 字号是不是和原 deck 一致（详见 [`references/brand-spec.md`](references/brand-spec.md) 字号表）
- 中英文混排是否有 layout shift

---

## 2.5 版面纪律（强制，Step 6 自检前置项）

每页内容必须在 1280×720 画布内完整呈现，不溢出、不留大面积空白。

### 2.5.1 禁止溢出

- 每页所有可见元素的底边必须 < 660px（为页脚留 60px）
- **多行标题**（含 `<br>` 或自然换行）：手动计算实际高度（36pt ≈ 每行 55px），将副标题 `.sub` 和内容区 `.content` 的 `top` 值相应下移，不得与标题重叠
- **Flex / Grid 布局**：优先用 padding、font-size、line-height 控制内容高度，不依赖 `overflow:hidden` 裁切
- 完成拼装后，**逐页扫一遍**：内容区底边 + 页脚底边（674+22=696）< 720

### 2.5.2 禁止大面积空白

- 内容区结束位置与页脚之间的空白不得超过 **120px**（约 2 行正文高度）
- 如果内容不足以填满页面：
  - 优先扩大卡片 padding / 提升正文字号 / 增加行距
  - 其次增加一条带来源标注的引用条（quote-block）补充页面重量
  - 最后考虑上移内容区起点（缩小标题区到内容区的间距）
- **连续两页都是 Low 密度（内容区 < 300px 高）**→ 合并为一页

### 2.5.3 一页一检

Step 5 拼装每页完成后，立即做以下三点检查再进入下一页：

1. 内容最低元素的 `top + height` 是否 < 660
2. 内容最低元素与页脚之间空白是否 < 120px
3. Flex 子项是否高度一致（差异 > 60px 时视觉失衡，需调整内容量或 padding）

---

## 3. 反 AI slop（强制）

> 与 huashu-design §6 一致，本 skill 在 Shokz 语境下额外强调：

| 禁止 | 原因 |
|---|---|
| 圆角卡片 + 左侧彩色 border accent | Shokz 体系是直角矩形 + 顶/底/侧边粗 border。模仿 Material Design 会和品牌脱节 |
| Emoji 当 icon | Shokz 体系用"中文 · ENGLISH"等宽标签，emoji 会破坏精密感 |
| 紫渐变 / 赛博霓虹 | Shokz 是黑 + 橙 + 灰阶，渐变发明色就是和品牌打架 |
| `Inter / Roboto / Arial / SF Pro` 作 display | 用 Noto Sans SC 中文 + Consolas 等宽标签的固定堆栈，详见 brand-spec |
| 临场发明的颜色（"接近 Shokz Orange 的色"） | 不存在。要么是 `#FF7A3D`，要么不用 |
| 用 CSS 剪影 / 形状代替真实产品图 | 涉及具体产品（OpenSwim Pro / NCE 等）必须真图，详见 §4 |
| 每条标题都配 icon | Shokz 用"中文 · ENGLISH"标签替代 icon。多余的 icon 是噪音 |
| 散落微交互 / 满屏动效 | 沿用原 deck 的 `IntersectionObserver` 翻页脚本即可，不要再加飞舞元素 |

---

## 4. 资产协议（涉及具体产品/人物时强制）

继承 huashu-design §1.a 但适配 Shokz 内部场景：

### 4.1 Logo（任何对外/正式场合必备）

- 内部双周会 / 周报 → logo 可省（封面有 `Shokz 韶音 · BE OPEN` 文字水印即可）
- 转正答辩 / 述职 / 培训 / 对客户预演 → logo 必需，放封面右下角或片尾
- 文件位置：用户工作目录 `assets/shokz-logo.svg`，如缺失就**停下问用户**

### 4.2 产品图

涉及具体型号必须用真图：

| 触发 | 必须 |
|---|---|
| 提到 OpenSwim Pro / OpenRun Pro 2 / OpenFit Pro / OpenSwim / OpenRun 等具体型号 | 至少一张官方产品图（用户提供 / Shokz 官网 / 内部 DAM） |
| 提到色款（月银白 / 静谧黑 / 冰川蓝 等） | 该色款的真实产品图，不要画 CSS 剪影 |
| 案例页讲某次上市 | 该次上市的实物图 / KV / 包装图 |

找不到 → **停下问用户**，不要 AI 生成代替。

### 4.3 个人/团队照片

- 转正答辩 / 述职这类强个人叙事 → 用户提供本人工作照、读书照、健身照（参考原 deck `photos/01-reading-note.jpg` 等）
- 案例页讲 collaboration → 项目截图、聊天截图、Excel 输出截图

### 4.4 内部数据 / 截图

- 涉及销量 / DAU / 转化率等敏感数据 → 用户确认是否对外，**严禁自行编造看似合理的数据**
- 内部工具截图（飞书 / 钉钉 / 内部知识库）需用户提供，不要凭训练语料画"看起来像"的 UI

---

## 5. 工程纪律

### 5.1 单文件 vs 多文件

**默认单 HTML**。沿用原 deck 的"`<section>` 列表 + IntersectionObserver 翻页"模式，双击就能开，发飞书 / 邮件附件方便。

> 例外：deck > 30 页 或 需要并行编辑 → 才考虑拆成多 HTML + 聚合 index。本 skill 默认场景（10-20 页）不需要。

### 5.2 CSS 抽离

[`assets/deck.css`](assets/deck.css) 抽出了 `.deck-slide / .shp / .pp / .tbl` 公共样式。**新 deck 必须通过 `<link rel="stylesheet">` 引用本文件**，不要再每个 deck 内联一遍——这是 mid_eng 工程化的核心收益（改一处全 deck 受益）。

### 5.3 snippet 复用约定

[`assets/snippets/*.html`](assets/snippets/) 每个文件顶部都有注释，标注：
- **可改字段**：哪些字符串可以替换为业务文案
- **不可改数值**：left/top/width/height/font-size/color，这些是品牌锁

> 拼装时**只改可改字段**。要调位置 → 先到 [`references/layout-grid.md`](references/layout-grid.md) 看是否在网格约束内。

### 5.4 motion.min.js 保留位

[`assets/motion.min.js`](assets/motion.min.js) 从原 deck 复用过来，目前默认不启用（原 v3 动画版也没启用）。后续如需要做发布会级动画，可在此基础上加 `motion.animate(...)` 调用——但本 skill 主链**不强制做动画**。

---

## 6. 路由表

| 想干什么 | 读哪 |
|---|---|
| 知道品牌色板 / 字体堆栈 / 字号体系 | [`references/brand-spec.md`](references/brand-spec.md) |
| 知道 1280×720 网格、边距、内容区点位 | [`references/layout-grid.md`](references/layout-grid.md) |
| 选用哪个组件 / 怎么用 | [`references/components.md`](references/components.md) |
| 选哪种叙事框架 | [`references/narrative-frameworks.md`](references/narrative-frameworks.md) |
| 完整从需求到交付怎么走 | [`references/workflow.md`](references/workflow.md) |
| 交付前自检 | [`references/deck-page-checklist.md`](references/deck-page-checklist.md) |
| 完整参考实现长啥样 | [`example/转正答辩_v3_动画版.html`](example/转正答辩_v3_动画版.html) |
| 直接起手 | [`assets/deck-skeleton.html`](assets/deck-skeleton.html) |

---

## 7. 与其他 skill 的分工

- **huashu-design**：通用 HTML 设计。本 skill 是它在 Shokz 场景下的特化版——继承反 slop、资产协议、Junior pass 原则，但锁死品牌+排版
- **ppt-agent**：从 0 生成 PPT 的全流水线（含信息检索 / 大纲生成 / 多 agent 协作）。本 skill 是它的"模板侧 + 风格层"——内容已经就绪时直接拼装，不走 subagent 调度
- **frontend-design**：通用 Web 应用设计。**不**适合本 skill 的 fixed-canvas + 横版 deck 场景

---

## 8. 一次合格交付的样子

- 单个 `.html` 文件，双击浏览器打开就能翻页
- 每页都有"中文 · ENGLISH" 页眉 + "Shokz 韶音 · BE OPEN | NN / 总数" 页脚
- 主色只有 `#FF7A3D` 和 `#050505`，灰阶只用 spec 里列出的 4 个值
- 字号严格匹配 brand-spec 的 8 档体系
- 11 个组件的位置/边距/字号都没被改动
- 内容稿和 deck 一一对应，没有 deck 多出的"AI 觉得应该有"的页
