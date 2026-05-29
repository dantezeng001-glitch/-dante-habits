---
name: 长文底稿中文翻译与改进
overview: 在 Shokz Insights 长文底稿的英文正文之后、"中文对照与核心设计意图"之前，新增"中文正文"章节，严格逐段直译；同时按前述改进建议小幅打磨英文正文（含 CTA 占位、hedge 词、结尾首尾呼应），孤证数字保留不改。
todos:
  - id: insert_zh_body
    content: 在第 58 行后、第 60 行前插入 `## 中文长文正文（内部对照参考）`，逐段直译英文正文，术语对齐批次 2/3 配文已落版措辞
    status: completed
  - id: polish_en_body
    content: 英文正文小幅打磨：删 `seemingly` 与 `remarkably`、拆分第 36 行一句三事、结尾补首尾呼应
    status: completed
  - id: sync_zh_edits
    content: 把英文打磨后的改动同步到新增的中文正文，保证两种语言一致
    status: completed
  - id: final_grep_check
    content: Grep 关键数字/术语，确认本文档中英文对齐、跨文档无漂移
    status: completed
isProject: false
---

## 目标文件

[Shokz_Insights_长文底稿(收束承接).md](04-营销传播/202604%20NT-AO/文案安排-领英/Shokz_Insights_长文底稿(收束承接).md)

## 变更一：新增"中文长文正文"章节

位置：在现有第 58 行 `---` 之后、第 60 行 `## 中文对照与核心设计意图（仅供内部参考）` 之前，插入新章节 `## 中文长文正文（内部对照参考）`。

- 严格逐段对照英文 Step 1/2/3 结构翻译，章节小标题与英文一一对应：
  - Step 1: Stepping Out of the Lab → 走出实验室：300+ 噪音源建模
  - Step 2: The Acoustic Null Point & The 1,000+ Ear Database → 声学零点与 1000+ 只人耳数据库
  - Step 3: Pushing Physical Limits with SuperBoost™ → 用 SuperBoost™ 挑战物理极限
  - Focus and Awareness Are No Longer Mutually Exclusive → 专注与感知不再互斥
- 技术术语采用已在批次 2/3 配文中落版的中文措辞，保证跨文档一致：`三麦克风阵列`（不用"三麦阵列"）、`千人千耳`、`田野调查` / `噪音源`（与 `LinkedIn配文初稿-批次2与3.md` 第 41/91/141 行一致）。
- 首段行业痛点、副标题一并译出；尾部 CTA 同步译出（链接占位沿用）。
- 孤证数字（`14 years` / `85%` / `up to 4kHz`）按用户选择直译，不加"待确认"标注。

## 变更二：英文正文小幅打磨（仅删词/换词，不改动数字与结构）

- 第 16 行：`a seemingly impossible question` → `an impossible question`（删 hedge 词）
- 第 44 行：`with remarkably low distortion` → `with low distortion`（删程度副词）
- 第 36 行：将 `This ensures that no matter your ear shape or size, the microphones capture the right signal from the start, delivering a consistent filtering experience for 85% of users without manual tuning.` 拆成两句，先讲"信号从源头就准确"，再讲"85% 用户免调校即可获得一致体验"——降低一句三事的堆积感。
- 结尾段落（第 46–52 行）补一句首尾呼应，把"自主权"落回开篇的 `the traffic on your run` / `a colleague in the office` 两个具体场景，中文版同步译出。

## 不在本次变更范围

- 不修改 Step 1/2/3 的章节顺序（当前"由软到硬"的主线保留）。
- 不扩写或删减现有"中文对照与核心设计意图（仅供内部参考）"章节。
- CTA 链接占位 `[Shokz.com](#)` 保持占位，仅在 plan 层面提示你之后替换为真实 UTM 链接。

## 落地后自检

改完后 Grep 一次 `300|1,?000|14|SuperBoost|PMI|4\s*kHz|85%`，确认中英文数字完全一致、与其他配文（批次 1/2/3、视频规划）也无漂移。