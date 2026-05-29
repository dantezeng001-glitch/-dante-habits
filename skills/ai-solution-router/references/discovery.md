# Discovery

Use this before recommending tools. The goal is to understand the user's real job well enough to make all three routing decisions (environment, control, knowledge) with confidence.

## Opening Question

Ask:

```text
你先用一个具体例子讲讲：这件事现在通常怎么发生，从你拿到什么输入开始，到你希望得到什么结果结束？
```

Then ask one follow-up at a time.

## Fast Track

If the user's first message already covers 3 of 4 key dimensions (input, output, frequency, workspace), skip discovery and go directly to routing. Mark missing details as assumptions.

The 4 key dimensions:

- **Input**: what the user starts with.
- **Output**: what counts as success.
- **Frequency**: how often the job happens.
- **Workspace**: where the work physically happens (chat, browser, code, multiple systems).

## Confidence Checklist

Proceed to routing when you can answer all of the following (mark remaining unknowns as assumptions):

- What exact job is the user trying to finish?
- What input does the user start with?
- What output counts as success?
- How often does the job happen?
- How much time, attention, or frustration does it currently cost?
- Are there SOPs, templates, examples, or past cases the AI should follow?
- Does the work happen mostly in chat, documents, spreadsheets, browser/web apps, code, local files, or multiple systems?
- Does the task require the AI to interact with web pages, read/write files, or run code?
- Does the task depend on internal company knowledge, policies, documents, or permission-controlled content?
- What risks matter: accuracy, privacy, compliance, cost, external dependencies, user confirmation?
- Does the process need system integration, human approval gates, or notifications that cannot be skipped?
- What is the user's (or team's) technical capability and available tools?

If only one or two low-risk details remain unclear, proceed and mark them as assumptions.

## Follow-Up Question Pool

Use these as a pool, not a questionnaire. Pick the most informative question for the current gap.

### Environment (feeds Decision A)

- "这件事主要在哪儿发生：聊天框、文档/表格、网页后台、浏览器搜索、代码项目，还是多个系统之间？"
- "需要 AI 真正点击网页、登录系统、下载资料、改文件或跑代码吗？"
- "交付物是一段文字，还是文件/代码/可运行的东西？"

### Control (feeds Decision B)

- "这件事有没有固定步骤、模板、SOP 或以前做过的优秀案例？"
- "下次再做，你需要重新跟 AI 解释一遍规则吗？还是规则可以固化下来？"
- "如果 AI 跳过某步、不通知某人、不写入某系统，会怎样？只是质量差一点，还是会出事？"
- "过程中有没有必须等人审批/确认才能继续的环节？"
- "它是偶尔做，还是每天/每周反复做？"

### Knowledge (feeds Knowledge Overlay)

- "这件事需要引用公司内部文档、制度、历史案例、客户资料或知识库吗？"
- "需要参考的资料能一次性粘贴进对话吗？还是太多/太散/会持续增长？"
- "输出需要标明引用来源吗？是否有权限隔离或保密要求？"

### Capability and Difficulty (feeds difficulty gates)

- "你们团队有没有能搭建/维护工作流平台（如 Dify、扣子、n8n）的人？"
- "如果推荐用 AI 编程工具生成代码，有人能看懂输出并验收吗？"
- "如果推荐搭建知识库/RAG，有人能持续维护文档索引吗？"

### Risk and Boundary

- "AI 输出之后，你希望它只给建议，还是直接执行？哪些地方必须你确认？"
- "这个任务如果做错，代价是什么？只是返工，还是会影响客户、合规或业务决策？"

## Stop Conditions

Proceed to routing when:

- You can make all three independent decisions (environment, control, knowledge) with confidence.
- You can explain why at least two other routes are less suitable.
- You have assessed the user's implementation capability for the likely route.
- You can generate a concrete next artifact, not just name a tool.

If the user says "不要问太多，先给判断", ask one final high-leverage question, then produce a provisional recommendation with assumptions.

## Edge Cases

### User changes requirements mid-discovery

If the user introduces a fundamentally different task during discovery, restart the confidence checklist for the new task. Do not carry over assumptions from the old task. Briefly acknowledge: "理解，我们换到新需求重新判断。"

### User rejects the route at confirmation

1. Ask which axis they disagree with (environment, control, or knowledge).
2. Ask one targeted question about that axis.
3. Re-evaluate only the disputed axis, keep the other two.
4. Re-present the updated route.

Do not restart full discovery unless the objection reveals the underlying task was misunderstood.

### Insufficient information after 5 questions

Produce a provisional recommendation. Mark all uncertain items as assumptions with their impact. State: "以下是基于当前信息的初步判断，标注了X处假设。确认或纠正后我可以更新。"

### User states a tool preference upfront

If the user names a specific tool (e.g. "我想用 Dify 搭个工作流"), do not ignore their preference:

1. Complete discovery as normal.
2. At route confirmation, present both: the skill's recommendation AND the user's preferred tool.
3. If they differ, explain the trade-off and let the user decide.
