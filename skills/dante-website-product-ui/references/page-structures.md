# Shokz Product Page — Page Structures

两类页面的完整 section 结构模板。根据产品层级选择 section 数量。

---

## A. 产品详情页（/pages/）— 讲故事、建认知

长滚动叙事页面，按卖点逐层展开。不含购买功能和 FAQ。

### 固定区块（所有产品必有）

| 序号 | 区块 | 说明 |
|------|------|------|
| 1 | **Sticky Sub-Nav** | Details / Compare / Reviews / Support 四个锚点 tab |
| 2 | **Hero** | 产品名（全大写）+ tagline + 价格 + "Shop Now" CTA |
| 3 | **Feature Overview** | 5-8 个核心卖点卡片（图 + 2-3 词短文案），快速建立第一印象 |

### 可选区块（按产品层级选配）

| 区块 | 旗舰 | 中端 | 入门 | 办公 |
|------|:----:|:----:|:----:|:----:|
| Awards/Badges（CES 等） | Y | 有则加 | — | — |
| Video Highlight | Y | Y | — | — |
| Deep-Dive: 音质/技术 | Y（2-3 节） | Y（1-2 节） | Y（1 节） | Y（1 节） |
| Deep-Dive: 降噪/漏音 | Y | 有则加 | — | — |
| Deep-Dive: 佩戴舒适 | Y | Y | Y | Y |
| Deep-Dive: 运动稳定性 | Y | Y | — | — |
| Deep-Dive: 防水 | Y | Y | Y | — |
| Battery Section (stat cards) | Y | Y | Y | Y |
| Call Quality / 麦克风 | Y | 有则加 | — | Y |
| Designed Around You (6-grid) | Y | Y | — | Y |
| App Section | Y | Y | — | Y |
| 软件生态 / 认证 | — | — | — | Y |
| Compare Table | Y | Y | Y | Y |
| Footnotes | Y | Y | Y | Y |

### 产品层级参考

- **旗舰**：OpenFit Pro / OpenRun Pro 2（12-15 sections）
- **中端**：OpenFit 2 Series / OpenDots ONE（8-12 sections）
- **入门**：OpenFit Air / OpenMove / OpenRun / OpenSwim（5-8 sections）
- **办公**：OpenMeet / OpenMeet2 / OpenComm2（8-10 sections，增加认证 + 软件生态）

办公产品的 Software Ecosystem section 包含三层：
1. **Shokz App**（iOS / Android）— 手机端 EQ、提示音
2. **Shokz Connect**（Windows / macOS）— PC 端设备管理、Focus Mode
3. **Shokz Command Center**（IT 管理中台）— 企业集中部署

### Deep-Dive Section 排列规则

1. 图文交替：奇数 section 文左图右，偶数 section 图左文右
2. 奇偶背景交替：奇数 `--white`，偶数 `--light-gray`
3. 卖点排序：按 Message House / FABE 的核心卖点优先级排列
4. 每个 deep-dive section 对应 1 个核心卖点

---

## B. 购买页（/products/）— 促转化、辅决策

信息密度高的购物页面，所有区块均固定存在。

### 完整区块序列

| 序号 | 区块 | 说明 |
|------|------|------|
| 1 | **Sticky Sub-Nav** | Purchase / Details / Compare / Reviews / Support |
| 2 | **Product Hero** | 左：产品图轮播（5 张） / 右：产品名 + 价格 + 4 条 USP bullets + 选色/选码 + Add to Cart |
| 3 | **Trust Badges** | "Why Buy from Shokz.com" — 四项保障（措辞固定不可改） |
| 4 | **Feature Highlight Strip** | 黑底白字横条，6-7 个核心数据/卖点缩写 |
| 5-8 | **Condensed Features** | 3-4 个核心卖点的精简版（比 /pages/ 短，每个 = headline + 1 段 + 1 图） |
| 9 | **Designed Around You** | 6-card grid：辅助功能/卖点 |
| 10 | **What's in the Box** | 配件展示 grid |
| 11 | **Compare Table** | 本品 vs 同系列次一级产品 |
| 12 | **FAQ** | 4 类手风琴：Product Info / Comparisons / User Guide / Shokz App |
| 13 | **Social CTA** | "Follow us" + #ShokzSquad |
| 14 | **Footnotes** | 所有 * 标注的免责声明 |

### /products/ Hero 区详细结构

```
┌──────────────────────────────────────────────┐
│ ┌───────────────┐  ┌─────────────────────┐   │
│ │               │  │ PRODUCT NAME        │   │
│ │  [Product     │  │ Tagline sentence.   │   │
│ │   Image       │  │ $XX.XX              │   │
│ │   Gallery]    │  │                     │   │
│ │               │  │ • USP bullet 1      │   │
│ │  1/5  2/5 ... │  │ • USP bullet 2      │   │
│ │               │  │ • USP bullet 3      │   │
│ └───────────────┘  │ • USP bullet 4      │   │
│                    │                     │   │
│                    │ Color: ● ● ●        │   │
│                    │ [Add to Cart]       │   │
│                    └─────────────────────┘   │
└──────────────────────────────────────────────┘
```

### USP Bullets 内容方向（固定 4 条）

| 条序 | 方向 |
|------|------|
| 1 | 核心音质/技术差异点 |
| 2 | 佩戴舒适/设计特色 |
| 3 | 开放式设计/环境感知/安全 |
| 4 | 续航 + 充电方式 |

### Trust Badges（固定措辞，不可修改）

1. Fast & Free Delivery
2. 45-Day Price Match Promise
3. 45-Day Free Returns
4. 2-Year Warranty

---

## C. 两类页面的关键差异总结

| 维度 | /pages/ | /products/ |
|------|---------|------------|
| 核心功能 | 品牌叙事 + 技术深度 | 购买转化 + 快速决策 |
| Hero | 居中：产品名 + tagline + CTA | 双栏：左图右购买面板 |
| 卖点展示 | 每个独立 section，大篇幅 | 压缩为精简段落 |
| 技术细节 | 展开解释原理 | 只提技术名 |
| FAQ | 无 | 4 类手风琴 |
| What's In The Box | 无 | 有 |
| 购买保障 | 顶部横幅（简） | 详细 Trust Badges |
| CTA | "Shop Now" / "Watch the video" | "Add to Cart" |
| 内容篇幅 | 长（5000-8000 词） | 中等（2000-4000 词） |
