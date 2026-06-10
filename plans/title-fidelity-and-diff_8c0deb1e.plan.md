---
name: title-fidelity-and-diff
overview: 让美化输出的标题跟随输入（输入无标题就不加），并在同语言润色时于美化句子内联高亮改动处。
todos:
  - id: prompt
    content: 在 lib/prompt.ts buildSystemPrompt 硬约束块新增'格式/标题跟随原文'规则
    status: completed
  - id: diff-util
    content: 新建 lib/diff.ts:中英兼容的词/字级 LCS diff,标记 added 片段,不加依赖
    status: completed
  - id: resultcard
    content: ResultCard 增加 original/sameLanguage props,同语言非流式时内联高亮 added 片段,加对比/纯净开关,复制保持干净正文
    status: completed
  - id: page
    content: app/page.tsx 计算 sameLanguage 并向 ResultCard 传 original 与 sameLanguage
    status: completed
  - id: verify
    content: 手测四个场景 + npm run build 通过
    status: completed
isProject: false
---

# 标题跟随输入 + 美化句内联高亮改动

## 背景与根因
- 卡片顶部加粗的"方向名"(`variant.focus`)不是问题，保留不动。
- 问题 1：原文是纯句子时，模型会在 `text` 正文里凭空加标题。根因在 [lib/prompt.ts](lib/prompt.ts) 的系统提示词缺少"格式跟随原文"的硬约束。
- 问题 2："改了哪里"目前完全没呈现。[components/ResultCard.tsx](components/ResultCard.tsx) 第 91-96 行的"改动"字段(`variant.changes`)是死代码——[lib/prompt.ts](lib/prompt.ts) 第 88 行的输出 schema 根本没要求模型返回它。需求是改成在正文内联高亮，不走这个文字字段。

## 改动 1：标题跟随输入（改 prompt）
在 [lib/prompt.ts](lib/prompt.ts) `buildSystemPrompt` 的【硬约束】块（第 54-59 行附近）新增一条结构保真规则，大意：
- 输出版式必须跟随原文：原文是纯句子/纯段落，就只输出句子/段落，不得新增标题、小标题、列表等原文没有的结构。
- 原文自带标题，则保留并美化该标题，不删不改其层级。

仅加一条规则，不动其它逻辑。

## 改动 2：同语言润色内联高亮改动
- 新建 [lib/diff.ts](lib/diff.ts)：轻量词/字级 diff（LCS），不引入新依赖。
  - 分词器：CJK 按单字切，非 CJK 连续字母数字按词切，空白/标点单独成 token，兼顾中英。
  - 输出 token 序列，每个标记 `equal | added`（新增/改写部分）；删除片段不在正文展示，避免噪音。
- 改 [components/ResultCard.tsx](components/ResultCard.tsx)：
  - 新增 props：`original`(原文) 与 `sameLanguage`(是否同语言)。
  - 当 `sameLanguage && !streaming` 时，用 diff 结果渲染正文：`added` 片段加底色/下划线高亮；否则按现状渲染纯文本（流式中、跨语言均不高亮）。
  - 复制仍复制 `variant.text` 干净正文（高亮只是展示），现有 `copy()` 不动。
  - 加一个小开关"对比原文 / 纯净"，默认对比（高亮）；重写较重时用户可切回纯净查看。
- 改 [app/page.tsx](app/page.tsx)：
  - 计算 `sameLanguage = target === "same" || target === source`。
  - 给 `ResultCard` 传 `original={input}` 与 `sameLanguage`。

## 验证
- 输入一个无标题英文句子 → 美化结果正文不出现标题行。
- 输入带标题的文案 → 标题保留并被美化。
- 同语言（目标=与原文相同）→ 美化句中改动处高亮；跨语言（中译英）→ 不高亮，正常显示。
- 复制按钮复制的是干净正文，无高亮标记残留。
- 跑 `npm run build` 确认类型与构建通过。