---
name: Shokz Product Page Skill
overview: 基于 Shokz 官网全线产品页面的系统分析，创建一个个人 Cursor Skill，用于生成 Shokz 风格的产品详情页（/pages/）和购买页（/products/）的单 HTML 文件。
todos:
  - id: fetch-all-products
    content: 等后台 agent 返回所有产品页面数据，交叉验证页面结构的一致性与差异
    status: completed
  - id: extract-patterns
    content: 提取跨产品的共性模式 + 品类差异，完善 page-structures.md
    status: completed
  - id: build-design-tokens
    content: 汇总设计 token 并写入 references/design-tokens.md
    status: completed
  - id: build-component-lib
    content: 提取可复用 HTML 组件片段，写入 references/component-library.md
    status: completed
  - id: build-copy-patterns
    content: 归纳文案模式规范，写入 references/copy-patterns.md
    status: completed
  - id: write-skeletons
    content: 创建两个页面骨架 HTML 文件
    status: completed
  - id: write-skill-md
    content: 编写 SKILL.md 主文件（<500 行）
    status: completed
  - id: validate
    content: 用 OpenMeet2 数据做一次模拟验证，确认 skill 可正确指导页面生成
    status: completed
isProject: false
---

# Shokz 产品官网页面制作 Skill

## 已完成的分析

已抓取并分析的页面：
- [OpenFit Pro /pages/](uploads/openfit-pro-0.md) + [/products/](uploads/openfit-pro-1.md)
- [OpenMeet2 已有 HTML](OpenMeet2-Listing-Page.html)（你的产出）
- [OpenMeet2 Message House](IWE-MSG-House.md)、[FABE](IWE-FABE.md)、[官网 listing 文案](cursor_excel/IWE_传播内容文案_合集/官网_website_上线listing.md)
- 后台正在并行抓取 OpenRun Pro 2 / OpenDots One / OpenFit 2 / OpenFit Air / OpenSwim Pro / OpenRun / OpenMeet / OpenComm2 / OpenMove / OpenSwim 的两类页面做交叉验证

已参考的 Shokz 内部 skill：[dante-shokz-ppt](~/.cursor/skills/dante-shokz-ppt/SKILL.md)（品牌色 / 视觉规范）

---

## Skill 结构

```
~/.cursor/skills/dante-website-product-ui/
├── SKILL.md                    # 主指令（<500 行）
├── references/
│   ├── page-structures.md      # 两类页面的完整 section 结构模板
│   ├── design-tokens.md        # 颜色/字体/间距/圆角等全部 CSS 变量
│   ├── component-library.md    # 可复用的 HTML 组件片段（hero/feature/compare/FAQ 等）
│   └── copy-patterns.md        # 文案逻辑、措辞模式、footnote 规范
└── assets/
    ├── product-page-skeleton.html   # /pages/ 空白骨架
    └── listing-page-skeleton.html   # /products/ 空白骨架
```

---

## SKILL.md 核心内容（提纲）

### 1. 触发与边界
- 触发：用户要做 Shokz 产品的"产品页"或"购买页/listing page" HTML
- 边界：不做 PPT（那是 dante-shokz-ppt）、不做邮件/EDM、不做 App 界面

### 2. 两类页面的结构公式

**A. 产品详情页（/pages/）** — 讲故事、建认知

| 区块序号 | 名称 | 作用 |
|---------|------|------|
| 1 | Sticky Sub-Nav | Details / Compare / Reviews / Support 四个锚点 |
| 2 | Hero | 产品名（全大写）+ 一句话 tagline + 价格 + Shop Now CTA |
| 3 | Awards/Badges | CES / 媒体奖项横排展示 |
| 4 | Feature Overview Grid | 5-6 个核心卖点卡片（图 + 短文案），形成第一印象 |
| 5-N | Deep-Dive Sections | 每个核心卖点展开为独立 section，图文交替排列 |
| N+1 | Battery Section | 大数字 stat cards（续航/快充/无线充电） |
| N+2 | Call Quality | 麦克风降噪效果对比（含音频试听 UI） |
| N+3 | Designed Around You | 6-card grid 放辅助卖点 |
| N+4 | App Section | Shokz App 功能展示 |
| N+5 | Compare Table | 本品 vs 最近竞品，双列对比表 |
| N+6 | Footnotes | 所有 * 标注的免责声明 |

**B. 购买页（/products/）** — 促转化、辅决策

| 区块序号 | 名称 | 作用 |
|---------|------|------|
| 1 | Sticky Sub-Nav | Purchase / Details / Compare / Reviews / Support |
| 2 | Product Hero | 左：5 图轮播 / 右：产品名 + 价格 + 核心 bullets + 选色 + Add to Cart |
| 3 | Trust Badges | "Why Buy from Shokz.com" 四项保障 |
| 4 | Feature Highlight Strip | 横向滚动条/marquee，6-7 个核心卖点缩写 |
| 5-8 | Condensed Features | 3-4 个核心卖点（比 /pages/ 更精简，每个 1 段文字 + 1 张图） |
| 9 | Designed Around You | 6-card grid |
| 10 | What's in the Box | 配件展示 grid |
| 11 | Compare Table | 本品 vs 竞品/前代 |
| 12 | FAQ | 分类手风琴：Product Info / Comparisons / User Guide / App |
| 13 | Social CTA | "Follow us" + #ShokzSquad |
| 14 | Footnotes | 免责声明 |

### 3. 设计 Token（从 Shokz 官网提取）

**颜色体系**
- `--black: #1a1a1a`（主文字 + CTA 按钮底色）
- `--dark-gray: #2d2d2d`
- `--mid-gray: #666`（二级文字、说明文）
- `--light-gray: #f5f5f5`（交替 section 背景）
- `--white: #ffffff`
- `--accent: #e8491d`（高亮/badge，Shokz 品牌橙的偏深变体）
- 产品页以黑白灰为主调，极少用彩色——让产品图成为唯一色彩来源

**字体体系**
- Font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- H1: `36px / weight 700`
- H2: `32px / weight 700 / line-height 1.2`
- Body: `16px / line-height 1.7`
- Stat 大数字: `48px / weight 800`
- 小字/标签: `13-14px`
- 按钮文字: `16px / weight 600`

**间距与布局**
- `max-width: 1200px`，居中，左右 `padding: 24px`
- Section 间距: `80px 0`
- 双栏 grid gap: `60px`
- 卡片圆角: `16px`（大卡）/ `12px`（中卡）/ `8px`（小元素如 FAQ item）
- CTA 按钮圆角: `30px`（全圆角胶囊型）
- Feature section 图文交替：奇数节图左文右，偶数节文左图右（`direction: rtl` 技巧）

### 4. 组件库（HTML 片段）

将提取以下可复用组件，每个含完整 HTML + CSS：

- **Hero-Detail**：产品详情页 hero（全宽背景图 + 产品名 + tagline + CTA）
- **Hero-Purchase**：购买页 hero（左图轮播 + 右信息面板）
- **Highlight-Strip**：黑底白字横条，6-7 个核心数据
- **Feature-Section**：图文双栏（含交替方向）
- **Feature-Section-with-Stats**：图文双栏 + 下方 3 列 stat cards
- **Feature-Grid-6**："Designed Around You" 3x2 卡片网格
- **Battery-Section**：大数字 stat cards 专用
- **Compare-Table**：双列产品对比表（含 NEW badge）
- **FAQ-Accordion**：分类手风琴 FAQ
- **Box-Grid**："What's in the Box" 配件展示
- **Trust-Badges**：四项保障横排
- **Footnotes**：底部免责声明区

### 5. 文案模式规范

**标题公式**
- 产品名始终全大写：`OPENFIT PRO`、`OPENMEET2 UC`
- 核心 headline 格式：`[特性名词短语].\n[价值句/情感句].`
  - "Open-Ear Audio. Reimagined."
  - "Your Voice. Crystal Clear."
  - "Wireless power. All day long."
- 副标题用 sentence case，不超过 2 行

**正文公式**
- 每个 feature section 的正文 = 1-2 段 x 2-3 句
- 第一句：技术/特性陈述（what）
- 第二句：用户价值（so what）
- 可选第三句：差异化点或场景

**数据展示**
- 关键数字独立展示为 stat card（48px 大字 + 13px 标签）
- 数字后跟单位和说明（"Up to 50 hours of total playtime with charging case"）
- 所有实验室数据加 `*` 标注，底部 footnote 写完整免责

**对比表文案**
- 表头：`Which Product Is Right For You?`
- 新品列加 `NEW` badge
- 对比维度：Technology / Battery / Quick Charge / Charging / Water Resistance / Weight
- 底部可加 `Buy now` CTA

**FAQ 文案**
- 分类标签：Product Info / Comparisons / User Guide / Shokz App
- Q 用自然语言提问格式
- A 结构化回答：先直接答（Yes/No），再展开说明

### 6. 工作流（用户调用 skill 后的执行步骤）

1. **确认页面类型**：产品详情页 or 购买页
2. **收集输入**：Message House / FABE / 官网文案表 / SPEC 规格书
3. **选骨架**：复制对应的 skeleton.html
4. **填充内容**：按结构公式逐 section 填入文案 + 图片占位符
5. **自检清单**：颜色是否只用 token / 间距是否一致 / footnote 是否齐全 / 响应式断点是否生效

---

## 跨产品交叉验证结果（已确认）

基于 OpenFit Pro / OpenRun Pro 2 / OpenDots ONE / OpenFit 2 Series / OpenComm2 / OpenMove / OpenSwim 共 7 个产品线、14+ 个页面的对比分析：

### 结构一致性

两类页面的区块模板在所有产品上保持一致，差异仅在内容密度：

- 旗舰产品（OpenFit Pro / OpenRun Pro 2）：/pages/ 有 12-15 个 deep-dive sections
- 中端产品（OpenFit 2 / OpenDots ONE）：/pages/ 有 8-12 个 sections
- 入门产品（OpenFit Air / OpenMove）：/pages/ 有 5-8 个 sections
- 办公产品（OpenMeet / OpenComm2）：结构与消费线一致，但增加"软件生态"和"认证"section

### 颜色一致性

所有产品均使用同一套黑白灰主色调，无产品专属 accent color。品牌橙（`#e8491d`）仅用于 NEW badge 和个别高亮元素。产品图是页面唯一的色彩来源。

### 文案模式确认

跨产品验证的 headline 句式：
- "Dual Drivers, Double the Sound." (OpenRun Pro 2)
- "Light Clip, Powerful Sound." (OpenDots ONE)
- "Open-Ear Comfort Ultimate Sound." (OpenFit 2)
- "Open-Ear Audio. Reimagined." (OpenFit Pro)
- "Mighty sound, mini size." (OpenDots ONE)
- "Music On, Still Connected." (OpenRun Pro 2)

规律：**短句断句 + 句号分隔 + 前半特性后半价值**，无一例外。

### 对比表规律

所有 /products/ 的对比表均遵循"本品 vs 同系列次一级产品"策略：
- OpenFit Pro vs OpenFit 2 Series
- OpenRun Pro 2 vs OpenRun vs OpenSwim Pro
- OpenDots ONE vs OpenFit 2
- OpenFit 2 vs OpenFit Air

对比维度固定 6-8 项：Technology / Battery / Quick Charge / Charging / Water Resistance / Weight / Material / Launch Date

### FAQ 分类确认

所有 /products/ 的 FAQ 均分 4 类：Product Info / Comparisons / User Guide (Using Guide) / Shokz App。Q 始终用自然语言提问（Is/Does/How/What/Can），A 先直接作答再展开。

### 购买区 USP 条确认

所有 /products/ 的 USP 条始终为 4 条，格式统一：
- 条 1：核心音质技术
- 条 2：佩戴舒适/设计差异点
- 条 3：开放式设计/安全感知
- 条 4：续航 + 充电

### Trust Badges 确认

所有 /products/ 均使用同一套 4 项保障，措辞完全一致：
- Fast & Free Delivery
- 45-Day Price Match Promise
- 45-Day Free Returns
- 2-Year Warranty
