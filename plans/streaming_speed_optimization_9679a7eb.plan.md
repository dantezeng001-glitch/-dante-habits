---
name: streaming speed optimization
overview: 让网页输出像 Cursor 一样逐字流式呈现(方向 A),并压低"点击到第一个字"的首字延迟(方向 B:text 字段前置 + 精简 prompt),在不牺牲品牌护栏的前提下显著改善体感速度。
todos:
  - id: live-text
    content: 改 extractStreaming:提取未闭合 text,逐字返回进行中文案(方向 A)
    status: completed
  - id: reorder-json
    content: buildUserPrompt 模板:text 字段前置、detectedSourceLang 挪到末尾(方向 B)
    status: completed
  - id: trim-prompt
    content: 砍 few-shot 范例 + 风格留5个 + 规则去重 + 压缩措辞 + 去 charCount(方向 B)
    status: completed
  - id: optional-cursor
    content: 可选:ResultCard 进行中卡片加闪烁光标(改前先读)
    status: completed
  - id: verify
    content: 脚本测首字时间+总耗时,确认逐字增长与护栏不回归(标准/专家各一次)
    status: completed
isProject: false
---

# 流式输出提速:逐字渲染 + 压低首字延迟

## 目标
- A:正文逐字出现(打字机效果),不再"整段 text 写完才出卡"。
- B:缩短"点下去 → 第一个可见字"的空窗(text 前置 + 精简 prompt)。
- 不削弱关键护栏(防杜撰、语言规则、合规)。

## 根因回顾(已确认)
- `extractStreaming`(见 [lib/parseStream.ts](lib/parseStream.ts) 第 95 行)用正则要求 text **闭合**才显示 → 写正文时屏幕静止。
- 输出 JSON 先吐 `detectedSourceLang` + `variants[` + `focus` 等脚手架,真正可见的 `text` 排在后面;system prompt 偏大(约 1.5–2k tokens)拉高 prefill。

## 改动一:A 逐字渲染(核心)
文件:[lib/parseStream.ts](lib/parseStream.ts)
- 在 `extractStreaming` 里新增"未闭合 text"的提取:定位当前在写对象里的 `"text":"` 后,逐字扫描(处理 `\` 转义)直到遇到未转义 `"`(已闭合)或缓冲区末尾(进行中),返回**当前已写出的部分文案**。
- 有至少 1 个非空字符就返回这张"进行中"的卡;`focus` 若还没写出用占位名,写出后自动补上。
- 复用 `unquote` 容错(半个转义字符时回退原串)。
- 结果:[app/page.tsx](app/page.tsx) 的流式循环每收到一块就 `setResult`,正文随之逐字增长——无需改循环本身。

## 改动二:B 首字延迟(挑性价比高的两项)
文件:[lib/prompt.ts](lib/prompt.ts) 的 `buildUserPrompt` 输出模板
- **text 前置**:把每个 variant 的字段顺序改成 `text` 在最前;`detectedSourceLang` 从开头挪到 JSON 末尾。这样模型几乎一开始就在写可见正文,首字大幅提前。解析不受影响(`extractDetectedLang` 全文匹配,complete/partial 解析与字段顺序无关)。
- **精简 system prompt(适中偏积极,质量我把控)**:
  1. **整段删掉 few-shot 范例**(第 76–79 行)——它是给已删除的弱模型 v1-8k 准备的拐杖,k2.5/k2.6 靠文字规则即可,这是最大一块且低风险。
  2. **瘦身风格注入**(第 42–47 行 `styleBlock`):没选风格时,从全量 10 个改为 5 个代表 + 短描述,减少每次注入体积。
  3. **规则去重**:`至少 2 个变体`、`focus/intent/reason 用中文`等在 system(第 73–74 行)与 user(第 101–102 行)重复,各只保留一处。
  4. **压缩措辞**:`brandFactsBlock` 与 5 条硬约束(尤其第 60 行防编造)压字数、**保语义**。
- **去掉 `charCount` 字段**:客户端已用 `[...text].length` 计算,schema 里不再要求模型吐。

## 不做(本轮)
- Moonshot 上下文缓存:改造量大、收益主要在重复前缀,列为后续。
- 换模型/基建:可控性低。

## 可选润色
- [components/ResultCard.tsx](components/ResultCard.tsx):给"进行中"的那张卡尾部加一个闪烁光标,更像 Cursor。改前先读当前内容,避免与并行 Agent 冲突。

## 验证
- 临时脚本测"首个可见字符时间"与总耗时,对比改前;确认逐字增长、最终变体数与护栏(risks)不回归。
- 标准/专家两档各跑一次(深度思考关)。

## 协作提醒
- 这些文件可能被另一个 Agent 同时编辑;每个文件改前先重读,避免覆盖(此前已撞车过一次)。建议改这几个文件时另一个 Agent 暂停。