---
name: 产品统一表述知识库Excel
overview: 基于现有17个产品的 Meet 和 Spec 文件内容，构建一个多 Sheet 的 Excel 产品统一表述知识库，AI 先自动提取填充，再由团队校对。
todos:
  - id: create-excel-template
    content: 创建 Excel 文件，建好 5 个 Sheet 的表头结构
    status: pending
  - id: fill-doc-tracker
    content: Sheet 5 文档追踪：根据文件夹内容自动填充每个产品的文档覆盖状态
    status: pending
  - id: extract-product-info
    content: 逐个读取 17 个产品的 Meet/Spec PDF/PPT，AI 提取信息填入 Sheet 1-4
    status: pending
  - id: review-output
    content: 输出最终 Excel，标注哪些字段是 AI 提取的，哪些需要人工确认
    status: pending
isProject: false
---

# 产品统一表述知识库 Excel 方案

## 背景

通过分析现有 Meet 和 Spec 文件，Meet 文件是多页营销画册（卖点故事、标语、价格、色卡、对比表），Spec 文件是 1-2 页参数单（技术规格、包装物流、功能要点）。当前信息散落在 40 个 PDF/PPT 中，需要整合为一个可查询、可对比的 Excel。

## Excel 结构设计（5 个 Sheet）

### Sheet 1: 产品总览

每行一个产品，横向快速对比基本面。

- 产品名称（标准英文名）
- 产品线（Sport / Communication / Lifestyle / Swimming）
- 定位标语（英文 Tagline）
- 建议零售价 RRP（USD）
- 可选颜色
- 核心卖点摘要（3-5 条，每条一句话）
- 产品状态（在售 / 停产 / 即将上市）

### Sheet 2: 技术规格

每行一个产品，列为统一的规格参数项，方便跨产品对比。

- 型号（Model Number）
- 骨传导/气传导类型
- 蓝牙版本、协议、频段
- 频响范围、灵敏度、阻抗
- 防水等级（IP Rating）
- 电池容量、续航时间、待机时间
- 充电方式、充电时间、快充参数
- 重量
- 无线距离
- 保修期
- 其他特有参数（如 OpenSwim 的存储容量、支持格式）

### Sheet 3: 营销文案库

每行一个"产品 x 卖点"组合，用于统一对外表述口径。

- 产品名称
- 卖点编号
- 卖点标题（Feature Title，如 "TurboPitch Technology"）
- 英文标准描述（从 Meet 提取的官方文案）
- 法语标准描述（如有）
- 适用场景标签（舒适 / 音质 / 安全 / 续航 / 防水 / 连接 等）

### Sheet 4: 包装与装箱

渠道和物流需要的信息。

- 产品名称
- What's in the Box（装箱清单）
- 单台包装尺寸 & 重量
- 整箱数量、尺寸 & 重量（如 Spec 中有）

### Sheet 5: 文档完成度追踪

管理各产品文档覆盖状态的看板。

- 产品名称
- Meet (EN): 有/无 + 文件名
- Meet (FR): 有/无 + 文件名
- Spec (EN): 有/无 + 文件名
- Spec (FR): 有/无 + 文件名
- POP: 有/无
- 备注（如"法语 Spec 缺失"）

## 执行方式：AI 提取 + 人工校对

1. 先创建 Excel 模板，Sheet 5（文档追踪）可立即根据现有文件夹自动填充
2. 逐个读取 17 个产品的 Meet/Spec 文件（PDF/PPT），AI 自动提取信息填入 Sheet 1-4
3. 生成的 Excel 标记"AI 提取"字段，团队校对确认后改为"已确认"

## 注意事项

- 部分 PDF 是扫描件/设计稿，文字提取可能不完整，需人工补充
- 不同产品的 Meet/Spec 模板不统一（有的 Meet 含规格表，有的不含），字段覆盖率会有差异
- 法语内容仅部分产品有，营销文案库中法语列可能大量为空

