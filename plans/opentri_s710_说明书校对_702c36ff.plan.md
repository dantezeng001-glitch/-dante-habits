---
name: OpenTri S710 说明书校对
overview: 以 OpenSwim Pro User Guide 为母本，对 OpenTri (S710) 英文线上说明书做全文校对——验证换名适配是否完整，同时覆盖两份文档共有的语言质量问题。
todos:
  - id: name-replacement-verify
    content: 验证所有 OpenSwim Pro → OpenTri 换名点是否完整且无遗漏
    status: pending
  - id: inherited-issues
    content: 标记母本自带的语言/格式问题（同时存在于两份文档）
    status: pending
  - id: target-only-issues
    content: 识别目标文件独有的问题（换名过程中引入）
    status: pending
  - id: output-table
    content: 按 skill 表格格式汇总输出，同根因聚合，附严重程度统计
    status: pending
isProject: false
---

# OpenTri (S710) 英文线上说明书校对方案

## 校对前提

- **母本/基准**: `OpenSwim_Pro_User_Guide.pdf`（39 页）——全文为唯一校对依据
- **目标文件**: `OpenTri(S710)线上说明书-英文 240905.pdf`（39 页）
- **源-目标关系**: 同语言换名适配。OpenTri 本质是 OpenSwim Pro，为渠道需求做了产品名、蓝牙显示名、USB 磁盘名、URL、包装清单名称的替换
- **范围**: 全文所有章节
- **预期差异**: 产品名 OpenSwim Pro → OpenTri, 蓝牙名 → OpenTri by Shokz, 磁盘名 SWIM PRO → TRI, URL openswimpro → opentri, 包装清单 OpenSwim Pro → OpenTri

## 校对原则

母本的角色是**换名同步的校验依据**，不是语言质量的免责盾牌。目标文件里的每一处英文问题都按客观标准判断和输出，不因"母本也有"而降级或跳过。"母本同样存在"仅作为根因溯源信息附在依据列。

## 校对维度（五维全开）

- **Accuracy**: 换名后功能描述、参数、步骤是否仍与母本一致；目标文件自身的事实/参数是否准确
- **Sync**: 除预期换名外，是否有内容被意外增删改
- **Consistency**: 产品名/术语/格式在目标文件内部是否统一
- **Tone**: 表达风格是否统一
- **Grammar / Spelling / Punctuation**: 按英文客观标准检测语法、拼写、标点——与母本无关，错了就是错了

## 逐行比对初步结论

### A. 换名替换点——全部完成，无遗漏

| 母本原文 | 目标替换为 | 出现位置 | 状态 |
|---|---|---|---|
| OpenSwim Pro (产品名) | OpenTri | p7/p13/p14/p32/p37 等 | 完整 |
| OpenSwim Pro by Shokz (蓝牙名) | OpenTri by Shokz | p7/p23/p24/p25 等 | 完整 |
| SWIM PRO (USB 磁盘名) | TRI | p13 共 4 处 | 完整 |
| userguide.shokz.net/openswimpro | userguide.shokz.net/opentri | p3 | 完整 |
| OpenSwim Pro Headphones/Bag/Box | OpenTri Headphones/Bag/Box | p37 | 完整 |

未发现残留的 "OpenSwim" 或 "Swim Pro" 字样。

### B. 换名过程引入的问题

| 位置 | 问题 | 根因 |
|---|---|---|
| p14 | "supported by OpenTri :" 冒号前多了空格，母本无此空格 | 换名时引入 |

### C. 目标文件中的英文质量问题（按客观标准，不论是否与母本共有）

所有问题均需在目标文件中修正。"母本同样存在"仅用于溯源，不影响严重程度判定。

**语法错误（高严重程度）**
- p21/p26/p28/p31 共 4 处: "Audrey say" → "Audrey says"（主谓一致）
- p35: "when you in the pool" → "when you are in the pool"（系动词缺失）
- p30: "so that to confirm if" → "to confirm whether"（错误不定式结构）
- p34: "thecorresponding" → "the corresponding"（缺空格）

**标点错误（中严重程度）**
- p35: "corrosion.Please" → "corrosion. Please"（句号后缺空格）
- p24/p25: "8.Turn" / "9.Turn" → "8. Turn" / "9. Turn"（编号后缺空格）
- p3: "countries.Google" → "countries. Google"（句号后缺空格）
- p21: "pairing"。→ 英文文档中混入中文句号

**术语/格式一致性问题（中严重程度）**
- p34: "headset" vs 全文其余均用 "headphones"——应统一
- p10: "Click once" vs "Click Once"——同一表格内大小写不统一

**PDF 渲染/字体问题（需确认）**
- p12/p15: 章节标题中 "MP3" 显示为 "MP�"——可能是 PDF 字体嵌入而非文案问题，需查看设计源文件确认

## 执行步骤

1. **输出正式校对表**: 所有问题按客观标准统一输出，不分"母本继承"和"目标独有"两类——依据列中注明"母本同样存在"即可
2. **每条 finding 标注**: 位置、原文、建议、维度、子类型、严重程度、置信度、依据（含母本对应位置溯源）
3. **同根因聚合**: "Audrey say" 等重复出现的问题合并为一条 + 位置列表
4. **汇总统计**: 按严重程度计数 + 下一步建议

## 输出格式

| 文件 | 位置 | 原文 | 建议/处理 | 维度 | 子类型 | 严重程度 | 置信度 | 依据 |
|---|---|---|---|---|---|---|---|---|

结尾附：严重程度统计、母本继承 vs 目标独有分类、下一步建议。
