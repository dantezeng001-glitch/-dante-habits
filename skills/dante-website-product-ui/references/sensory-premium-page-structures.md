# Sensory Premium Style — Page Structures

> 近似品牌：Bose / B&O / Jabra

合一页面的"三明治"结构：购买区（上）→ 品牌叙事（中，零 CTA）→ 对比+评论（下），sticky 购买条贯穿全程。

---

## 页面类型：Purchase + Narrative 合一

三个 Bose 产品页共享完全相同的模板。购买面板在上，滚动后变为 sticky 底部条；品牌叙事长卷在中；信任收口在下。

---

## 完整区块序列

| 序号 | 区块 | 功能定位 |
|------|------|----------|
| 1 | **Feature Icons Bar** | 8 个水平卖点标签（图标 + 短文案），可点击展开 |
| 2 | **Product Title + Rating** | H1 产品名 + 星级评分（rated X/5 by N） |
| 3 | **Product Intro**（折叠） | 1-2 句定位文案 + "Read more" 展开完整版 |
| 4 | **Purchase Panel** | 颜色选择 + 价格 + 数量 + BoseCare 保修 + Gift Box + Add to Cart |
| 5 | **Trust Bar** | "Benefits of buying direct from Bose" — 4 条权益 |
| 6 | **Accessories** | 关联配件推荐 |
| 7 | **Sticky Buy Bar**（滚动后激活） | 精简版：产品名 + 颜色 + 价格 + Add to Cart |
| 8 | **Product Details** | What's in the Box / 充电说明 / Technical Specs 表 |
| 9 | **FAQ** | 10-12 个问题，手风琴展开 |
| 10 | **Support** | App 下载 / Owner's Guide / Quick Start Guide |
| 11-N | **Narrative Sections ×7-14** | 品牌叙事长卷：每个区块 = H2 + 1-3 句 + 全幅意境图，零 CTA |
| N+1 | **Feature Card Grid** | 2×3 卡片汇总功能（图标 + 标题 + 1 句话） |
| N+2 | **Why Buy from Bose** | 4 条权益卡片（信任收口） |
| N+3 | **Compare Table** | 同产品线 2-3 列横向对比 |
| N+4 | **Accessories**（底部二次推荐） | 关联销售 |
| N+5 | **Ratings & Reviews** | 总评分 + 5 条好评 + 分页 |

---

## Purchase Panel 详细结构

```
┌──────────────────────────────────────────────────────┐
│  ┌──────────────────┐  ┌───────────────────────────┐ │
│  │ [产品图库]        │  │ Color: Driftwood Sand     │ │
│  │ 可滑动 5+ 张图    │  │ ● ● ● ● ●               │ │
│  │                   │  │ $449.00                   │ │
│  │                   │  │ Quantity: [1-10]          │ │
│  │                   │  │                           │ │
│  │                   │  │ BoseCare:                 │ │
│  │                   │  │ ○ Accident Plan $99.95 ★  │ │
│  │                   │  │ ○ Protection $59.95       │ │
│  │                   │  │ ○ No warranty             │ │
│  │                   │  │                           │ │
│  │                   │  │ Gift Box: [$9.95] / No    │ │
│  │                   │  │                           │ │
│  │                   │  │ [ Add to Cart ]           │ │
│  └──────────────────┘  └───────────────────────────┘ │
│  ┌─ Trust Bar ──────────────────────────────────────┐ │
│  │ 90-day returns │ Price match │ Free ship │ Afterpay│ │
│  └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

---

## Sticky Buy Bar（滚动后激活）

滚动进入叙事区后，购买面板收起为固定底部条：

```
┌──────────────────────────────────────────────────────┐
│  产品名   ● ● ● 颜色选择   $449   [ Add to Cart ]   │
└──────────────────────────────────────────────────────┘
```

---

## Narrative Section 内部模式

### 模式 A — 全宽文图
H2 居中 + 1-3 句描述 + 全幅产品意境图。最常见。

### 模式 B — 左右交替（Zigzag）
图文左右交替，用于模式对比（Quiet vs Aware）。

### 模式 C — 居中纯文字
仅 H2 + 正文段落，无图片。用于产品定义类区块。

**关键约束**：叙事区块内**不放任何转化按钮**——保持品牌沉浸感。

---

## 叙事区块典型顺序

```
总领升级 → ANC/核心技术 → 空间音频 → 设计/材质 → 便捷功能
→ 模式总览 → 模式对比深潜 → 空间音频深潜 → 个性化音质
→ 设计美学 → 舒适性 → 工艺细节 → Bose App 引导（最后一个）
```

### 产品 → 叙事区块数量

| 产品 | 叙事区块数 | 页面重点 |
|------|------------|----------|
| QC Ultra Headphones 2nd Gen | 14 | 降噪 + 空间音频 + 设计多维展开 |
| QC Ultra Earbuds 2nd Gen | 9 | 连接 + 通话 + 充电升级 |
| Ultra Open Earbuds | 7 | 开放式定义 + 全天佩戴场景 |

**最后一个叙事区块统一为 Bose App 引导**（App Store + Google Play 链接）。

---

## Compare Table 结构

| 属性 | 模式 |
|------|------|
| 列数 | 2-3 列（同产品线内对比） |
| 分组 | Audio Technology / Controls / Design |
| 数据呈现 | Yes/No / 简短描述 / 数字 |
| 每列 | 产品图 + 产品名链接 + 价格 |
| 底部 | 测试条件注释（小字 footnotes） |

### 对比策略

| 页面 | 对比产品 | 策略 |
|------|----------|------|
| QC Ultra Headphones | vs QC Headphones | 旗舰 vs 标准款 |
| QC Ultra Earbuds | vs Ultra Open vs QC Earbuds | 三档品类全景 |
| Ultra Open Earbuds | vs QC Ultra Earbuds vs QC Earbuds | 同上，视角不同 |

---

## "三明治"转化结构

页面核心策略——转化元素包裹叙事：

1. **顶部**：购买面板（先给转化入口）
2. **中间**：品牌叙事长卷（零 CTA，纯沉浸）
3. **底部**：对比表 + 评论（理性决策收口）
4. **全程**：Sticky 购买条（滚动到任何位置都能买）
