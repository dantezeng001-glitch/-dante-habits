# Bold Contrast Style — Page Structures

> 近似品牌：Beats / Marshall

合体式单页面：购买入口在顶部，营销长卷紧跟其下，一个 URL 完成全部转化 + 叙事。

---

## 页面类型：Marketing + Purchase 合一

Beats 不拆"品牌故事页"和"购买页"。每个产品只有一个 URL：购物车头 + 长卷轴营销体 + 尾部信任模块。

---

## 完整区块序列

| 序号 | 区块 | 说明 |
|------|------|------|
| 1 | **Delivery Banner** | 顶部窄横幅："Choose two-hour courier or free delivery" |
| 2 | **Hero / Buy Panel** | 产品名(H1) + 标语 + 价格 + 色彩选择器 + ADD TO BAG |
| 3 | **Promise Bar** | 三项承诺条（免运费 / 到店取 / Apple Music 试用） |
| 4 | **Feature Icons Strip** | 4-6 个水平卡片：图标 + 关键卖点一行文字 + "View Tech Specs" 链接 |
| 5 | **Video Tabs** | 横向标签切换：Behind the Design / Unboxing / How to Use |
| 6 | **Expert Quotes**（可选） | 3 条引用卡片（@handle + 职衔）— 旗舰独有 |
| 7 | **Product Overview** | 一段话概括全部卖点 |
| 8-N | **Deep-Dive Sections ×6-12** | 每节：Category Tag + H2 + 正文 + 产品图/数据大字报 |
| N+1 | **In the Box** | 配件清单（bullet list） |
| N+2 | **Apple Music Promo** | "3 Months of Free Music For Your Beats" |
| N+3 | **FAQ Accordion** | 5-12 个问题，可展开 |
| N+4 | **Newsletter Signup** | "Join Our List" + email 输入 + Sign Up |

---

## Hero / Buy Panel 详细结构

```
┌──────────────────────────────────────────────────────┐
│  ┌─────────────────┐  ┌──────────────────────────┐   │
│  │  [产品图]        │  │  H1: Beats Studio Pro    │   │
│  │                  │  │  Iconic Sound             │   │
│  │                  │  │  Sale Price $349.99       │   │
│  │                  │  │                          │   │
│  │                  │  │  颜色: ● ● ● ● ●        │   │
│  │                  │  │  [ADD TO BAG]            │   │
│  └─────────────────┘  └──────────────────────────┘   │
│  ┌─ 三项承诺 ────────────────────────────────────┐   │
│  │ 🚚 Free Shipping │ 🏪 In-store │ 🎵 Apple Music │  │
│  └─────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────┘
```

**购买区位置**：顶部内联（above the fold），不是 sticky sidebar。

---

## Deep-Dive Section 内部模式

### 模式 A — 居中文图
标题居中 + 下方大产品图。用于声学、设计章节。

### 模式 B — 左右交替（Zigzag）
图文左右交替排列。用于 ANC/Transparency、佩戴章节。

### 模式 C — 数据大字报
超大数字 + 小字注释 + 对比基准。用于电池、性能提升。

### 模式 D — 编号功能列表
01 / 02 / 03 + 标题 + 正文。用于功能模式列表（ANC / Transparency / Adaptive EQ）。

### 模式 E — 引用卡片
引号 + @handle + 职衔，居中展示。旗舰独有。

---

## 章节典型顺序

```
声学 → 降噪/通透 → 空间音频 → 佩戴 → 电池
→ 连接 → 通话 → 控制 → 设计 → 兼容性
```

具体章节数量与产品定位正相关：

| 定位 | 产品 | 章节数 | 独有模块 |
|------|------|--------|----------|
| 旗舰 | Studio Pro | 14 | 设计师引用、专家评价、有线连接详解 |
| 运动旗舰 | Powerbeats Pro 2 | 11 | 心率监测、运动员测试数据 |
| 运动中端 | Powerbeats Fit | 13 | 翼尖设计深潜、编号功能列表 |
| 生活方式 | Solo 4 | 9 | 最简页面结构 |
| 降噪中端 | Studio Buds + | 11 | 专家评价、倍数对比 |
| 入门 | Solo Buds | 10 | 手机充电盒、"smallest case ever" |

**规律**：价格越高 → 页面越长 → 章节越多 → 技术细节越深。

---

## Feature Icons Strip 内容方向

运动产品首位放佩戴/防水，音质产品首位放降噪/音频特性。电池续航和兼容性几乎永远在列。

**固定 4-6 条**，每条格式：
```
[图标]  [≤8 词卖点文案]
```

---

## 深浅交替规则

- 深色 section（`--color-bg-dark`）↔ 浅色 section（`--color-bg-white`）强交替
- 对比度高于 Apple——Beats 用更多黑色背景，能量感更强
- 产品配色可渗透到 section 背景渐变中
