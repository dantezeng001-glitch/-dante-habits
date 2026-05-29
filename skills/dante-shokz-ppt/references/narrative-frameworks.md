# Narrative Frameworks · 7 种叙事框架

> 组件解决"怎么排版"；框架解决"用什么逻辑讲"。每种框架都是从原 deck 提炼出来的，已经验过场——什么场景该用、什么场景不该用，下面写清楚。

---

## 选型决策表

按场景反查：

| 场景 | 首选框架 | 备选 |
|---|---|---|
| 试用期答辩 / 转正答辩 | 时间线+心路、9-cards、STAR、STAR+WARNING、GAM、FORMED-SHAPING（=原 deck 全套） | — |
| 述职 / 年度总结 | 9-cards、STAR、GAM | FORMED-SHAPING |
| 单个项目复盘 | STAR | STAR+WARNING |
| 反面案例 / 风险披露 | STAR+WARNING | — |
| 季度 / 双周汇报 | 9-cards、GAM | STAR（重点项目展开） |
| 产品上市策划 | GAM、9-cards、STAR | 三层涟漪（如已上市，讲扩散）|
| 培训课件 | 时间线+心路（讲行业演进）、三层涟漪（讲影响） | — |
| 个人介绍 / 路演 | 时间线+心路、FORMED-SHAPING | STAR（讲代表作） |
| OKR 评审 | GAM | 9-cards |
| 影响力 / 成果扩散 | 三层涟漪 | — |
| 跨年/跨季度变化 | FORMED-SHAPING | — |

---

## 1. STAR · 成功案例

**何时用**：讲一个已交付的项目 / 一个成功推进的事情 / 一个值得拿出来说的工作产出。

**结构**：
- **S** Situation 背景：项目起源、约束条件、时间压力
- **T** Task 任务：你的职责是什么、要交付什么
- **A** Action 行动：分 N 步说清楚做了什么
- **R** Result 结果：交付了什么 + 复盘金句

**版式**：
- 单页 STAR：S+T+A 三栏，R 单独成行（参考原 deck P06）
- 双页 STAR：上半页 S/T/A，下半页 R + 复盘（参考原 deck P06+P07）
- **页数预算**：1-2 页

**何时不用**：
- ❌ 还没交付完成的项目 → 用 STAR+WARNING 或不要硬讲
- ❌ 多个并列项目要一起说 → 用 9-cards Overview 先看全貌
- ❌ 个人成长 / 心路历程 → 用时间线+心路或 FORMED-SHAPING

**用 snippet**：[`snippets/star-card.html`](../assets/snippets/star-card.html)

---

## 2. STAR + WARNING · 反面案例

**何时用**：自己做了但没真正落地 / 走了弯路 / 路线后期被纠正 / 主动披露失败教训。

> 比 STAR 多一个"自我警觉"块，主动说"这件事还没成 + 卡点在哪 + 我承认有些事不在我能拉动的范围"。

**结构**：
- S 背景
- T 任务
- A 行动 + 路线纠偏（重点写"从 X 降级为 Y"）
- R 当前状态（橙色边框 HONEST 卡，写"理论可行，目前没真正跑起来"）
- 底部加一条全宽 Ink 黑 + 橙感叹号的 **WARNING 自省条**：写"卡点不是工具不够强，是我的判断力/拉动力还没跟上"

**版式**：
- 通常 1 页打满，可用 3 栏（S/A/HONEST）+ 1 栏 R 对照表 + 底部 WARNING 条
- 参考原 deck P10
- **页数预算**：1 页

**何时不用**：
- ❌ 用来推卸责任："不是我的问题是上游"（这是甩锅，不是 STAR+WARNING）
- ❌ 没做的事编一个"我尝试过失败了"（造假，不诚实）
- ❌ 整 deck 全是 WARNING（变成负面专场，反而没说服力——比例 1 失败 / 2-3 成功）

**用 snippet**：[`snippets/star-card.html`](../assets/snippets/star-card.html) + [`snippets/retro-bar.html`](../assets/snippets/retro-bar.html) 改造为 WARNING 条

---

## 3. 9-cards 全景 · 多任务/多项目概览

**何时用**：试用期 / 季度 / 半年要展示"我做了几件事"，每件都不深入但要让人一眼看到全貌和分类。

**结构**：
- 左侧 3 个 Anchor：3 大类别 + 件数 + 类别状态摘要
- 右侧 3×3 网格：9 张数据卡，每张顶部 ID + 状态（DONE/WIP/LIVE/DRAFT）+ 中文卡名 + 任务属性 + 一行 detail
- 底部图例

**版式**：1 页（参考原 deck P05）

**何时不用**：
- ❌ 任务数 < 5：用 STAR 单独讲更有质感
- ❌ 任务数 > 12：拆成多页或合并次要任务
- ❌ 9 件事的"类别"没法收敛成 2-3 大类：先回去重新归类，硬塞 9 格只是表格化的 todo

**用 snippet**：[`snippets/case-overview-9-cards.html`](../assets/snippets/case-overview-9-cards.html)

---

## 4. 时间线 + 心路历程 · 成长/迁移叙事

**何时用**：个人介绍 / 行业迁移轨迹 / 学习路径 / 产品演进史。本质是"沿时间轴讲三件平行的事"。

**结构**：
- 上半页：4 列时间线（日期 + Era 名 + 圆点轴 + 描述）
- 下半页："心路历程"面板：4 列 × 3 行 box，每行表达一个心理变化点（往下用 ↓ 箭头连接）
- 末列高亮（Ink 黑底 + 橙字）表示"当前位置"

**版式**：1 页满（参考原 deck P02）

**何时不用**：
- ❌ 只有 2 段经历：用普通对比卡更合适
- ❌ 5+ 段经历：列宽不够会挤
- ❌ 不想讲心路只想讲履历：那就只用上半页"时间线 4 列"，下半页留白或换别的组件

**用 snippet**：[`snippets/timeline-4col.html`](../assets/snippets/timeline-4col.html)

---

## 5. 三层涟漪 · 影响力扩散叙事

**何时用**：讲一件事"做了之后产生了什么连锁效应"——通常按"个人 / 团队 / 组织"或"部门内 / 跨部门 / 公司级"分层。

**结构**：
- 顶部全宽黑底总述条（"R · 结果"+ 大标题"5 min 起手 + 三层涟漪持续扩散"）
- 下方三栏：每栏顶部 3pt 粗 border（灰 → 中灰 → 橙，色越深表示范围越远 / 影响越大）
- 每栏内：英文小标 `LAYER 01 · 部门内` + 中文标题 + 12pt 正文

**版式**：1 页（参考原 deck P09）

**何时不用**：
- ❌ 一件事还没真正扩散：硬讲三层会被一眼戳穿
- ❌ 影响范围只有 1 层（仅自己做了）：用 STAR 的 R 即可
- ❌ "三层"没有递进关系（如三件并列的事）：用 9-cards 或三栏并列

**用 snippet**：[`snippets/ripple-3-layer.html`](../assets/snippets/ripple-3-layer.html)

---

## 6. GOAL-ACTION-METRIC · 未来规划 / OKR

**何时用**：试用期之后的下一阶段规划 / OKR 评审 / 项目立项 / 季度计划。本质是"目标-行动-度量"三件套。

**结构**：
- 三栏并列（350×400）：每栏一个方向
- 每栏内分三段：GOAL（目标）/ ACTION（行动）/ METRIC（度量）
- 段间用浅灰细线分隔
- 每段用 ① ② 编号列子项

**版式**：1 页（参考原 deck P11）

**何时不用**：
- ❌ 没有可度量的 metric：那就退化为 GA 二段或直接 STAR 的 T+A
- ❌ 超过 3 个方向：拆成多页
- ❌ 当前项目的进度汇报（不是规划）：用 9-cards 的状态徽章

**用 snippet**：[`snippets/three-column-goal-action-metric.html`](../assets/snippets/three-column-goal-action-metric.html)

---

## 7. FORMED-SHAPING · 关键变化卡

**何时用**：个人成长反思 / 试用期反思 / 阶段性总结。讲"经过这段时间，我身上有什么变化"——比 STAR 更内化、比时间线更聚焦。

**结构**：
- 整页 2-3 张全宽变化卡纵向堆叠
- 每张：左侧 48pt 橙色大编号 + 状态英文（`FORMED` 已成型 / `SHAPING` 在塑造 / `EMERGING` 萌芽）
- 右侧主标题（含 quoted 强调）+ 2 行 takeaway

**版式**：1 页（参考原 deck P15）

**何时不用**：
- ❌ 没有真实变化只是套话："变得更有责任心"（空泛 → 落到具体行为）
- ❌ 变化数 > 3：选最关键的，多了显得平
- ❌ 用来讲工作产出：那是 STAR / 9-cards 的活，不是 FORMED-SHAPING

**用 snippet**：[`snippets/change-card.html`](../assets/snippets/change-card.html)

---

## 8. 框架组合范式

> 单个框架很少独立成 deck，下面是几种验过场的组合：

### 8.1 转正答辩 16 页范式（原 deck 同款）

```
P01 封面
P02 个人简介           ← 时间线+心路
P03 性格自评           ← 自定义（DISC 四象限，本 skill 暂不收为标准组件）
P04 岗位认知           ← 自定义
P05 全景概览           ← 9-cards
P06-07 案例 ①         ← STAR（双页版）
P08-09 案例 ②         ← STAR（双页版）+ 三层涟漪
P10 案例 ③ 反面       ← STAR+WARNING
P11 未来规划           ← GOAL-ACTION-METRIC
P12 心路历程           ← 三栏并列（轻量定制）
P13 文化感受           ← 自定义
P14 双百               ← 自定义
P15 关键变化           ← FORMED-SHAPING
P16 致谢
```

### 8.2 季度汇报 6-8 页范式

```
P01 封面
P02 概览                ← 9-cards
P03 重点项目 ①         ← STAR
P04 重点项目 ②         ← STAR
P05 (可选) 反面案例     ← STAR+WARNING
P06 下季度规划         ← GOAL-ACTION-METRIC
P07 致谢/Q&A
```

### 8.3 产品上市策划 10 页范式

```
P01 封面（产品名 + 上市时间 + 渠道）
P02 产品 / 市场背景    ← 自定义（产品 KV + 卖点）
P03 竞品对比            ← 9-cards（变体：3 大维度 × 3 竞品）
P04 营销目标           ← GOAL-ACTION-METRIC
P05-06 策略详解        ← STAR（讲打法）
P07 节奏 timeline       ← 时间线 4 列（变体：里程碑代替 Era）
P08 资源 / 预算         ← 自定义表格
P09 风险预案            ← STAR+WARNING
P10 致谢/Q&A
```

### 8.4 培训课件 12 页范式

```
P01 封面（课程主题）
P02 课程背景           ← 自定义
P03 行业演进             ← 时间线 4 列
P04-08 知识点 1-5      ← 每页 STAR 或自定义讲解
P09 影响 / 案例         ← 三层涟漪
P10 学完之后做什么      ← GOAL-ACTION-METRIC
P11 关键 takeaway       ← FORMED-SHAPING
P12 致谢
```

---

## 9. 选型流程图

```
用户给来内容/brief
  │
  ├─ 是个人介绍 / 长期成长？ → 时间线+心路 / FORMED-SHAPING
  │
  ├─ 是多任务全景？ → 9-cards
  │
  ├─ 是单个项目深入？
  │    ├─ 已成功交付 → STAR
  │    └─ 没真正落地 → STAR+WARNING
  │
  ├─ 是未来规划？ → GOAL-ACTION-METRIC
  │
  ├─ 是影响力 / 扩散叙事？ → 三层涟漪
  │
  └─ 都不像 → 回去问用户：核心是讲什么？（不要硬套框架）
```

---

## 10. 红线

- ❌ 一个 deck 里同一种框架重复 >3 次（除非是"3 个 STAR 案例"这种刻意设计）—— 否则审美疲劳
- ❌ 在 6 页内用 5 种以上不同框架 —— 视觉碎片化
- ❌ 把框架当填空题——内容凑不齐就编（如 STAR 没有 R 就编一个）
- ❌ 用 9-cards 装不到 9 件事的内容（只有 5 件硬塞）—— 改用 5-cards 自定义网格
