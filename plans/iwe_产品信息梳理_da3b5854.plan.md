---
name: IWE 产品信息梳理
overview: 将散落在 3 份 Excel（产品信息包、POP文案、传播内容文案合集）中的 IWE (Shokz OpenMeet2) 产品信息，整合输出两份中英双语 Markdown 文档：MSG House（营销信息架构）和 FABE（卖点体系表）。
todos:
  - id: msg-house
    content: 创建 docs/IWE-MSG-House.md：合并 4 版 MSG House + 官网文案 + POP 文案，输出 5 个 Section 的中英双语营销信息架构
    status: completed
  - id: fabe
    content: 创建 docs/IWE-FABE.md：从 Product Info V3 + SPEC + 官网 listing + Brochure 提取信息，输出 10 行 FABE 大表（中英双语）
    status: completed
  - id: conflict-check
    content: 交叉校验两份文档的数字/术语一致性，标注所有 awaiting confirmation 项
    status: completed
isProject: false
---

# IWE 产品信息梳理方案

## 输入源与信息分布

信息散落在以下位置，多个版本共存、数据有冲突：

- [3.Message House](cursor_excel/【IWE】产品信息包-20260428_a25ed579/3.Message House（20260326更新）.md) — 4 个版本重复堆叠，卖点排序、人群描述各版本略有差异；含竞品列（Jabra/Poly/Logitech）
- [2.Product Info](cursor_excel/【IWE】产品信息包-20260428_a25ed579/2.Product Info（20260409更新）.md) — 3 个版本（V1/V2/V3），FABE 最详尽的原始来源，含技术原理、证据、竞品对比
- [4.SPEC](cursor_excel/【IWE】产品信息包-20260428_a25ed579/4.SPEC（20260428更新）.md) — 规格参数权威来源
- [POP文案](cursor_excel/IWE-POP文案-20260430_1269da07/Sheet1.md) — 6 卖点 / 4 卖点两套面向零售的精炼文案（多语言）
- [官网 listing](cursor_excel/IWE_传播内容文案_合集/官网_website_上线listing.md) — 英文官网文案，含技术命名（GlideFit、DualPitch、PremiumPitch 3.0、LeakSlayer 3.0）
- [Brochure](cursor_excel/IWE_传播内容文案_合集/Brochure.md) — 英文手册文案

## 已确认的数据口径

| 项目 | 采用值 | 来源 |
|---|---|---|
| 重量 | 77.9 ±1 g | SPEC 20260428 |
| 音乐续航 | 16 h | SPEC 20260428（待 5.20 实测更新） |
| 通话续航 | 12 h | SPEC 20260428（待 5.20 实测更新） |
| 快充 | 充电 5 min → 通话 2 h | SPEC 20260428（待 5.20 实测更新） |

其余规格一律以 SPEC 20260428 为准。

## 文档 1：MSG House（营销信息架构）

**输出路径**：`docs/IWE-MSG-House.md`

**结构**：

### Section 1 — Product Identity（产品身份）
- 产品名：Shokz OpenMeet2 / OpenMeet2 UC
- 品类定位：头戴式骨传导蓝牙办公耳机
- 一句话定位 slogan（取官网 KV "Comfort Empowers Innovation"）

### Section 2 — Target Audience（目标人群）
- 合并 MSG House 4 个版本的人群描述，去重后保留：核心画像 + 痛点 + 行为特征
- 从 Product Info V3 补充"高势能人群"定义

### Section 3 — Use Scenarios（使用场景）
- 开放/半开放办公室、居家办公、远程会议、电话会议

### Section 4 — Messaging Hierarchy（信息层级）
按 **Brand Promise → Key Messages → Proof Points** 三层组织：

- **Brand Promise**：一句核心承诺
- **Core Messages**（核心卖点 x4，与 FABE 前 4 条对齐）：
  1. 全天舒适佩戴 — 轻量 + 开放式 + 稳固 + 兼容眼镜
  2. AI 通话降噪麦克风 — 双麦棍咪 + ML cVc 算法
  3. 专业音效体验 — DualPitch 骨气双单元 + 低漏音
  4. 专业通讯软件认证 — Zoom + Webex
- **Supporting Messages**（辅助卖点 x6）：
  5. 续航 + 快充 + 有线
  6. 便捷操作与智能指示
  7. 开放双耳 / 环境音感知
  8. 蓝牙 Dongle 稳定连接
  9. 商务外观
  10. 软件生态（App / Connect / Command Center）

每条 Message 包含：中文要点 + English tagline（取自官网/POP已有文案）

### Section 5 — Competitive Landscape（竞品对标）
保留 Jabra Evolve2 55 / Poly Voyager Focus 2 / Logitech Zone Wireless 2 三栏，按核心卖点维度逐行对比，数据来源于 MSG House 第一版本区块。

---

## 文档 2：FABE 卖点体系表

**输出路径**：`docs/IWE-FABE.md`

**结构**：一张大表，每行一个卖点，列定义如下：

| 列 | 说明 | 主要信息来源 |
|---|---|---|
| 卖点编号 | 1-10 | MSG House 卖点排序 |
| Feature（产品特性） | 客观技术描述 | Product Info V3「卖点说明」列 |
| Advantage（产品优势） | 相对竞品/前代的差异化 | Product Info V3「对比竞品」列 + MSG House 竞品列 |
| Benefit（用户价值） | 对目标用户的直接好处 | 官网 listing / Brochure / POP 文案中的用户导向表述 |
| Evidence（证据支撑） | 专利、认证、测试数据、技术原理 | Product Info V3「证据」列 + SPEC |
| ToC Benefit 参考 | 同一 Feature 在消费者（居家办公）视角下的价值表述差异 | 我的判断，基于 ToB 内容改写，标注 `[ToC ref]` |

**10 行卖点顺序**（与 MSG House Section 4 保持一致）：
1. 全天舒适佩戴（轻量 + 开放 + GlideFit 稳固 + 兼容眼镜）
2. AI 通话降噪麦克风（ML cVc + 双麦棍咪 + 波束成形）
3. 专业音效（DualPitch + PremiumPitch 3.0 + LeakSlayer 3.0）
4. Zoom & Webex 认证
5. 续航 + 快充 + 有线模式
6. 便捷操作（旋钮 + 抬棍静音 + Busylight）
7. 开放双耳 / 环境音感知
8. 蓝牙 6.0 + Loop120 Dongle
9. 商务外观设计
10. 软件生态（Shokz App / Connect / Command Center）

每行 FABE 双语呈现：中文为主体，英文取官网/POP 已有定稿文案，未定稿处标注 `[draft]`。

额外增加一列 **ToC Benefit 参考**：主体仍为 ToB 视角，但对核心卖点补充消费者（居家办公场景）视角下的价值表述差异，供跨场景复用时参考。此列内容为我的改写判断，统一标注 `[ToC ref]`。

---

## 信息冲突处理原则

- 规格数字：以 SPEC 20260428 为唯一权威来源，标注"待 5.20 实测更新"的项目保留当前值并加脚注
- 营销文案措辞：优先取官网 listing 已定稿英文 + POP 已翻译中文
- 卖点排序：以 MSG House 第一版本区块（最详细、含竞品）为基准，V2/V3 仅补充缺失细节
- 技术描述：以 Product Info V3 为准（最新版本），V1/V2 仅在 V3 缺失时回溯
- 标注 `awaiting confirmation` 的项目：续航实测数据（5.20 后更新）、重量微调、Webex 认证状态

## 执行方式

两份文档独立成文，放在 `docs/` 目录下。MSG House 是叙述式 + 表格混排，FABE 是结构化大表。两份文档的核心 4 卖点保持完全一致（编号、顺序、命名）。
