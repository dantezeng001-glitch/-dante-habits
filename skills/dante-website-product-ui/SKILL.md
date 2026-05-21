---
name: dante-website-product-ui
description: >-
  生成 6 种设计风格的产品官网 HTML 页面。按视觉设计语言分类：Shokz / Apple / Bold Contrast / Sensory Premium / Tech Premium / Data Spectacle，覆盖产品详情页和购买页。输出单 HTML 文件，含完整 CSS，可直接浏览器打开。当用户提到"做产品页"、"做 listing page"、"做购买页"、"做官网页面"、"product page"、"listing page"，或要制作产品 HTML 展示页面时使用。不适用于 PPT（走 dante-shokz-ppt）、邮件/EDM、App 界面。
---

# 产品官网页面制作（6 种设计风格）

> 把用户提供的产品资料拼装成一份指定设计风格的单 HTML 页面。

---

## 0. 风格选择（必须第一步完成）

问用户目标风格，或根据产品品牌/定位推荐：

| # | 风格 | 近似品牌 | 视觉调性 | 文案调性 | 页面类型 |
|---|------|---------|---------|---------|---------|
| 1 | **Shokz** | Shokz | 黑白灰主调，品牌橙点缀 | 技术短句 + 价值句，克制 | 详情页 + 购买页（分离） |
| 2 | **Apple** | Apple / Samsung / Google | 白底 #f5f5f7 为主，深黑段交替 | 诗意双关 + 文字游戏，无感叹号 | 营销页 + 购买页（分离） |
| 3 | **Bold Contrast** | Beats / Marshall | 暗底 + 产品色强对比，高反差 | 街头自信，口语化短句 | 合体页（购买+营销一体） |
| 4 | **Sensory Premium** | Bose / B&O / Jabra | 极简黑白克制，感官温暖 | 第二人称感官词，效果优先于参数 | 合体页 + sticky 购买条 |
| 5 | **Tech Premium** | Sony | 80%+ 深色段，tech premium | 三层叙事：情感→技术→量化对比 | 营销页 + 购买页（分离） |
| 6 | **Data Spectacle** | OPPO / Huawei / Soundcore / Oladance | 全暗沉浸，巨型数据 callout | 工程叙事 + 版本号体系，密集脚注 | 合体页（一功能一全屏） |

**选择后**，读取该风格对应的参考文件（见 §8 索引），按下方工作流执行。

---

## 1. 触发与边界

### 适用

- 用户要做某品牌风格的产品 HTML 页面
- 用户提到具体产品名并要求做页面
- 用户说"按 XX 风格做"、"做个 listing"、"做产品页"

### 不适用

- PPT / 演示文稿 → `dante-shokz-ppt`
- 邮件 / EDM → 通用 skill
- App 界面 / 小程序 → 通用 frontend skill

---

## 2. 工作流（6 步）

### Step 0 · 确认风格

从 §0 表格中选定风格。用户未指定时：
- Shokz 产品 → 默认 Shokz 风格
- 用户说"Apple 风格"/"像苹果官网" → Apple
- 运动/潮流产品 → 推荐 Bold Contrast
- 高端音频/静谧定位 → 推荐 Sensory Premium
- 科技硬核/媒体导向 → 推荐 Tech Premium
- 参数密集/工程叙事 → 推荐 Data Spectacle

### Step 1 · 确认页面类型

每个风格支持的页面类型不同（见 §0 表格）。问用户需要哪种：

| 风格 | 详情/营销页 | 购买页 | 合体页 |
|------|:---------:|:-----:|:-----:|
| Shokz | ✓ | ✓ | — |
| Apple | ✓ | ✓ | — |
| Bold Contrast | — | — | ✓ |
| Sensory Premium | — | — | ✓ |
| Tech Premium | ✓ | ✓ | — |
| Data Spectacle | — | — | ✓ |

### Step 2 · 收集输入

需要以下资料（至少一项）：

1. **Message House**（.md）— 产品定位、核心/辅助卖点、竞品对标
2. **FABE 卖点体系**（.md）— 每个卖点的 Feature / Advantage / Benefit / Evidence
3. **官网文案表**（Excel 同步的 .md）— 每个 section 的定稿文案
4. **SPEC 规格书** — 技术参数、续航数据、防水等级

如果用户只给 brief，先帮他整理成结构化的卖点列表，确认后再做页面。

### Step 3 · 拼装页面

1. 读取对应风格的骨架 HTML（从 `assets/` 目录复制）
2. 读取 `{style}-page-structures.md` 确认 section 选配
3. 读取 `{style}-design-tokens.md` 确认颜色/字体/间距
4. 读取 `{style}-components.md` 选取需要的组件
5. 读取 `{style}-copy-patterns.md` 确认文案写法
6. 逐 section 填入内容，图片用描述性占位符 `[Image: 描述]`

### Step 4 · Section 选配

根据产品层级决定 deep-dive section 数量。各风格有不同的 section 数量基准：

| 层级 | Shokz | Apple | Bold Contrast | Sensory Premium | Tech Premium | Data Spectacle |
|------|:-----:|:-----:|:-------------:|:---------------:|:------------:|:--------------:|
| 旗舰 | 12-15 | 10-12 | 12-14 | 10-14 | 10-12 | 15-20 |
| 中端 | 8-12 | 8-10 | 9-11 | 7-9 | 8-10 | 12-15 |
| 入门 | 5-8 | 6-8 | 6-8 | 5-7 | 6-8 | 8-12 |

具体 section 选配规则见各风格的 `page-structures.md`。

### Step 5 · 自检

**版面纪律（强制，优先于风格检查）**：

- [ ] **禁止溢出**：所有 section 内的元素不得超出其容器边界。绝对定位元素的 `top + height` 必须在父容器范围内；Flex/Grid 子项内容超长时必须通过缩减 padding、降低字号、精简文案解决，不得依赖 `overflow:hidden` 裁切
- [ ] **禁止大面积空白**：section 内内容区与下一个 section 之间的可见空白不得超过该 section 高度的 20%。内容不足时优先扩大元素间距/字号/padding，其次增加引用或辅助信息填充，最后考虑合并相邻 section
- [ ] **文字不重叠**：多行标题、副标题、正文之间必须有明确的垂直间距（最小 16px），不得因固定 `top` 值导致上下元素视觉叠压
- [ ] **Flex 子项高度均衡**：同一行的 Flex 子项高度差异不得超过 60px，否则调整内容量或 padding 使其视觉平衡

**通用检查项**（所有风格）：

- [ ] CSS 变量只用对应 `design-tokens.md` 定义的值
- [ ] 所有实验室数据带标注（`*` 或上标数字）
- [ ] Footnotes 区包含所有标注对应的免责声明
- [ ] 响应式断点生效
- [ ] 文件可独立在浏览器打开

**风格专属检查项**：

| 风格 | 额外检查 |
|------|---------|
| Shokz | 产品名全大写；headline 符合"短句+句号+价值句"；CTA 按钮胶囊型 30px 圆角 |
| Apple | Hero 区无 CTA 按钮；正文 max-width ≤700px 居中；深浅段交替；链接蓝 #0066CC |
| Bold Contrast | 购买区在首屏内联；"ADD TO BAG" 全大写；数据大字报带对比基准 |
| Sensory Premium | Sticky 购买条存在；叙事区块零 CTA；保修加购选项；感官词密集 |
| Tech Premium | Feature Badges 横排；媒体评价引用块；三层技术叙事完整；30+ 脚注 |
| Data Spectacle | 巨型数字 callout（64-120px）；版本号术语完整；与上代显性对比；15+ 脚注 |

---

## 3. 各风格核心设计规则速查

### Shokz

- **颜色**：黑白灰主调，品牌橙 `#e8491d` 仅做 badge 点缀
- **间距**：Section padding 80px，双栏 gap 60px，CTA 圆角 30px
- **图文交替**：奇数文左图右，偶数图左文右
- **CTA**：黑底白字胶囊按钮（Shop Now / Add to Cart）

### Apple

- **颜色**：白底 `#f5f5f7` + 深黑 `#1d1d1f` 段交替，链接蓝 `#0066CC`/`#2997ff`
- **字号**：Display 64-96px，正文 max-width 700px 居中
- **CTA**：蓝色文字链 "Learn more >" + "Buy"，Hero 区无按钮

### Bold Contrast（近似 Beats / Marshall）

- **颜色**：深色背景主导，产品色作强调色
- **购买区**：内联首屏，"ADD TO BAG" 全大写
- **数据大字报**：每个核心卖点配一个数字锚点，必带对比基准

### Sensory Premium（近似 Bose / B&O）

- **颜色**：极简黑白灰，无品牌强调色
- **结构**：三明治——购买 → 叙事（零 CTA）→ 购买
- **购买条**：Sticky 底部条贯穿全程；保修加购选项

### Tech Premium（近似 Sony）

- **颜色**：80%+ 深色段，仅 Specs/购买面板用白底
- **Feature Badges**：横向滚动徽章栏，8-10 个卖点
- **叙事**：三层——情感钩子 → 技术实体 → 量化对比（点名前代型号）

### Data Spectacle（近似 OPPO / Huawei / Soundcore / Oladance）

- **颜色**：全暗沉浸，产品本身是唯一色彩来源
- **数字**：巨型 callout（64-120px），对比型/绝对型/换算型
- **结构**：一功能一全屏，平均 12-18 sections
- **术语**：技术版本号体系 + 大量自创品牌术语

---

## 4. 文案硬规则（按风格）

### Shokz Headline

`[特性短语]. [价值短句].` — "Open-Ear Audio. Reimagined."

### Apple Headline

文字游戏必备（双关/押韵/引用）— "Unmake some noise." / "Charges fast. And lasts."

### Bold Contrast Headline

反差对比 + 口语化 — "Looks tiny. Sounds huge." / "Apple or Android? Yes."

### Sensory Premium Headline

感官祈使句 — "Sink deeper into sound" / "A hug for your ears"

### Tech Premium Headline

短句宣言对 — "Beyond quiet. Transcendent sound." / "7x faster. Flawless control."

### Data Spectacle Headline

技术名 + 感性承诺 — "Ultralight Diaphragms Immerse You in Deep Bass"

**通用禁用词**：不用感叹号（Bose 偶尔例外），不用 "revolutionary"（用 "reimagined"），数据不用 "approximately"（用 "up to" + footnote）。

---

## 5. 购买元素差异

| 维度 | Shokz | Apple | Bold Contrast | Sensory Premium | Tech Premium | Data Spectacle |
|------|-------|-------|---------------|-----------------|--------------|----------------|
| 主 CTA | Add to Cart | Buy | ADD TO BAG | Add to Cart | ADD TO CART | Buy Now |
| 价格位置 | Hero 面板 | 产品卡片 | Hero 面板 | Hero 面板 | 购买面板 | Hero 或顶部 |
| 色彩选择 | 色块 swatch | 色块圆点 | 色板 swatch | 色块 swatch | 色块+标签 | 色块 swatch |
| 保修加购 | — | — | — | 保修 3 档 | — | — |
| 分期信息 | — | 月供 + 分期 | — | Afterpay | Affirm 0% APR | — |

---

## 6. 对比表策略

| 风格 | 对比策略 | 列数 |
|------|---------|------|
| Shokz | 本品 vs 同系列次一级 | 2-3 |
| Apple | 同品类全线 + "Currently viewing" | 2-4 |
| Bold Contrast | 无内置对比表 | — |
| Sensory Premium | 同品类 2-3 款 + 行分组 | 2-3 |
| Tech Premium | 品类页三列对比，仅关键差异 | 3 |
| Data Spectacle | 自家产品线横向对比 | 4-6 |

---

## 7. 输出规范

- 单个 `.html` 文件，CSS 内联在 `<style>` 中
- 文件命名：`[ProductName]-[Style]-[PageType].html`，如 `OpenMeet2-Shokz-Listing.html`
- 图片用描述性占位符：`[Image: lifestyle shot — person wearing headset at desk]`
- 价格如未确认写 `$XXX.XX`，数据如未确认写 `XX` 并标注 `[awaiting confirmation]`

---

## 8. 参考文件索引

### Shokz（原始文件，无前缀）

| 文件 | 内容 | 何时读 |
|------|------|--------|
| [design-tokens.md](references/design-tokens.md) | 颜色/字体/间距 CSS 变量 | Step 3 写 CSS |
| [component-library.md](references/component-library.md) | 12 个 HTML+CSS 组件 | Step 3 拼装组件 |
| [copy-patterns.md](references/copy-patterns.md) | headline/正文/FAQ 文案规范 | Step 3 + Step 5 |
| [page-structures.md](references/page-structures.md) | 两类页面 section 模板 | Step 3 确认结构 |
| [product-page-skeleton.html](assets/product-page-skeleton.html) | 产品详情页骨架 | Step 3 起手 |
| [listing-page-skeleton.html](assets/listing-page-skeleton.html) | 购买页骨架 | Step 3 起手 |

### Apple

| 文件 | 内容 |
|------|------|
| [apple-design-tokens.md](references/apple-design-tokens.md) | 颜色/字体/间距（白底+深色交替，SF Pro 系统字体） |
| [apple-components.md](references/apple-components.md) | Hero / 深浅段 / 横滑 shelf / 对比表等组件 |
| [apple-copy-patterns.md](references/apple-copy-patterns.md) | 双关标题 / 三层定位句 / CTA 小写规范 |
| [apple-page-structures.md](references/apple-page-structures.md) | 单品营销页 + 购买页结构模板 |
| [apple-marketing-skeleton.html](assets/apple-marketing-skeleton.html) | 营销页骨架 |
| [apple-buy-skeleton.html](assets/apple-buy-skeleton.html) | 购买页骨架 |

### Bold Contrast（近似 Beats / Marshall）

| 文件 | 内容 |
|------|------|
| [bold-contrast-design-tokens.md](references/bold-contrast-design-tokens.md) | 深色主导配色 / 粗体字重系统 |
| [bold-contrast-components.md](references/bold-contrast-components.md) | 购买区 / 数据大字报 / 视频 Tab / 引用卡片 |
| [bold-contrast-copy-patterns.md](references/bold-contrast-copy-patterns.md) | 反差对比句 / 口语化语气 / 数据锚点 |
| [bold-contrast-page-structures.md](references/bold-contrast-page-structures.md) | 合体页结构（购买头 + 营销体） |
| [bold-contrast-product-page-skeleton.html](assets/bold-contrast-product-page-skeleton.html) | 合体页骨架 |

### Sensory Premium（近似 Bose / B&O）

| 文件 | 内容 |
|------|------|
| [sensory-premium-design-tokens.md](references/sensory-premium-design-tokens.md) | 极简黑白灰 / 几何无衬线体 |
| [sensory-premium-components.md](references/sensory-premium-components.md) | Feature Pills / Sticky Cart / 叙事长卷 / 保修加购 |
| [sensory-premium-copy-patterns.md](references/sensory-premium-copy-patterns.md) | 感官第二人称 / 效果优先 / 温暖技术语言 |
| [sensory-premium-page-structures.md](references/sensory-premium-page-structures.md) | 三明治结构（购买→叙事→购买） |
| [sensory-premium-product-page-skeleton.html](assets/sensory-premium-product-page-skeleton.html) | 合体页骨架 |

### Tech Premium（近似 Sony）

| 文件 | 内容 |
|------|------|
| [tech-premium-design-tokens.md](references/tech-premium-design-tokens.md) | 80%+ 深色 / SST 字体回退栈 |
| [tech-premium-components.md](references/tech-premium-components.md) | Feature Badges / 媒体引用 / 工程师证言 / 三层叙事 |
| [tech-premium-copy-patterns.md](references/tech-premium-copy-patterns.md) | 短句宣言对 / 技术三层叙事 / 媒体评价格式 |
| [tech-premium-page-structures.md](references/tech-premium-page-structures.md) | 营销页 + 购买页分离结构 |
| [tech-premium-marketing-skeleton.html](assets/tech-premium-marketing-skeleton.html) | 营销页骨架 |
| [tech-premium-buy-skeleton.html](assets/tech-premium-buy-skeleton.html) | 购买页骨架 |

### Data Spectacle（近似 OPPO / Huawei / Soundcore / Oladance）

| 文件 | 内容 |
|------|------|
| [data-spectacle-design-tokens.md](references/data-spectacle-design-tokens.md) | 全暗沉浸 / 巨型数字字号 / 全屏 section |
| [data-spectacle-components.md](references/data-spectacle-components.md) | 巨型 Callout / 对比条 / 版本徽章 / 认证栏 |
| [data-spectacle-copy-patterns.md](references/data-spectacle-copy-patterns.md) | 工程叙事 / 版本号命名 / 前代对比 / 密集脚注 |
| [data-spectacle-page-structures.md](references/data-spectacle-page-structures.md) | 一功能一全屏合体页结构 |
| [data-spectacle-product-page-skeleton.html](assets/data-spectacle-product-page-skeleton.html) | 合体页骨架 |
