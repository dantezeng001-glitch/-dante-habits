# Apple Product Page — Page Structures

两类页面模板：单品营销页（沉浸式长卷轴）和购买页（横滑卡片货架）。

---

## A. 单品营销页（/airpods-max/ 风格）— 讲故事、建欲望

电影感滚动叙事，深浅交替背景，Hero 区不放按钮。

### 完整区块序列

| 序号 | 区块 | 说明 |
|------|------|------|
| 1 | **Hero** | 全屏居中：深色背景 + 产品名(H1) + 标语(H2) + 产品图（无 CTA 按钮） |
| 2 | **Feature Ticker** | 5-6 个快速扫读项，纯文字垂直堆叠，无边框无背景 |
| 3 | **Color Showcase** | 产品外观展示 + 水平色块圆点选择器 |
| 4-9 | **Deep-Dive Sections ×4-6** | 每个核心卖点独占一个 section（H2 诗意标题 + H3 技术子标题 + 正文 + 子特性卡片） |
| 10 | **Convenience Summary** | 电池 / Siri / 连接 / 充电等便利功能汇总（Data Callout 模式） |
| 11 | **Purchase Guide** | 4-5 个服务模块（刻字 / 配送 / 分期 / 视频导购） |
| 12 | **Compare Table** | 2-4 列产品对比，"Currently viewing" 标记当前产品 |
| 13 | **Sustainability Trio** | 环保 / 隐私 / 无障碍三件套（可选，旗舰独有） |
| 14 | **Footnotes** | 上标编号对应的免责声明集中区 |

### Deep-Dive Section 内部结构

每个 section 使用以下模式之一：

**模式 A — 标签切换卡片**
- 顶部水平标签栏（3-4 个 tab）
- 每个 tab 页含 H4 标题 + 1-2 段正文

**模式 B — 堆叠子区块**
- H3 子标题 + 正文段落，垂直堆叠
- 无边框，靠间距和标题层级区分

**模式 C — 数据大字报**
- 超大号数字（"30 hrs"、"5 hrs"）水平排列
- 数字下方一行说明文字

### 深浅交替规则

- 奇数 section：深色背景（`--color-bg-dark`），白字
- 偶数 section：浅色背景（`--color-bg-light`），黑字
- 制造电影感视觉节奏

### 产品层级 → Section 数量

| 层级 | 示例 | Deep-Dive sections | 总 section 数 |
|------|------|-------|--------|
| 旗舰 | AirPods Max 2 / AirPods Pro 3 | 5-6 | ~12 |
| 标准 | AirPods 4 | 3-4 | ~8 |

---

## B. 购买页（/shop/buy-* 风格）— 横滑货架、促转化

全浅色背景，由 6-8 个横滑 shelf 模块组成。

### 完整区块序列

| 序号 | 区块 | 说明 |
|------|------|------|
| 1 | **Hero** | "Shop [Product]" + Specialist 链接（无标语） |
| 2 | **All Models Shelf** | 横滑产品卡片（产品图 + 名称 + 价格 + Buy 按钮） |
| 3 | **Shopping Guides Shelf** | 横滑引导卡片（对比 / 视频 / 选购建议） |
| 4 | **Ways to Save Shelf** | Trade In / Apple Card / 教育优惠 / 翻新机 |
| 5 | **Apple Store Difference** | 服务模块（刻字 / 配送 / 个性化设置） |
| 6 | **Accessories Shelf** | 配件横滑卡片 |
| 7 | **Setup & Support Shelf** | 设置帮助 / AppleCare / 支持链接 |
| 8 | **Compare Table**（AirPods 购买页特有） | 4 列完整对比，含价格 |
| 9 | **Footnotes** | 免责声明 |

### 横滑 Shelf 卡片结构

```
┌─────────────────────┐
│  [标签（大写）]      │  "COMPARE ALL MODELS" / "WATCH AND LEARN"
│  链接标题            │
│  描述文（可选）       │
│  CTA 链接            │
└─────────────────────┘
```

### 产品卡片（All Models shelf）

```
┌─────────────────────┐
│  [NEW] 徽章（可选）   │
│  产品图               │
│  H3: 产品名           │
│  "Take a closer look" │
│  "From $XXX or        │
│   $XX.XX/mo for       │
│   XX months"          │
│  [Buy] 按钮           │
└─────────────────────┘
```

**价格格式**："From $XXX or $XX.XX per month for XX months"

---

## C. 两类页面关键差异

| 维度 | 营销页 | 购买页 |
|------|--------|--------|
| 核心功能 | 品牌叙事 + 欲望建设 | 快速决策 + 转化 |
| Hero | 全屏深色 + 标语，无按钮 | 浅色 + "Shop" 标题 |
| 背景节奏 | 深→浅交替（电影感） | 全浅色 |
| 内容展示 | 全屏 section 垂直滚动 | 横滑 shelf 卡片 |
| CTA | "Learn more" 文字链 | "Buy" 蓝色按钮 |
| 技术深度 | 每个卖点独立 section | 仅 Compare Table |
| 篇幅 | 长（8-12 screens） | 中（5-8 shelves） |
