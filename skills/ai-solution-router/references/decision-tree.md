# Decision Tree

Use this after discovery to route the user to the simplest reliable AI solution.

## Core Principle: Minimum Sufficient Solution

Start from the simplest route. Escalate only when there is a hard, testable reason AND the implementation difficulty is justified. Heavier solutions need higher justification; lighter solutions need only a confirmed need.

Difficulty ordering:

```text
Prompt(★) < Browser Agent(★★) < Skill(★★★) < Coding Agent(★★★~★★★★) < RAG(★★★★) < Workflow(★★★★★)
```

## Model Structure

Three independent decisions, evaluated in parallel, results combined:

```text
Decision A: Execution Environment — "What capability does the AI need?"
Decision B: Control Level          — "How much should the AI be constrained?"
Overlay:    Knowledge Source        — "What knowledge does the AI need?"

Final route = Environment × Control × Knowledge
```

These are not sequential filters. Each decision is made independently, then the results are combined into the final route.

## Decision A: Execution Environment

Determines WHERE the work physically happens. This is a hard technical constraint with no subjective judgment, so evaluate it first.

### Boundary Questions

**Text ↔ Browser Agent**

```text
"任务所需的信息和操作，能通过粘贴文本给 AI 完成？还是 AI 必须打开网页点击/填写/抓取？"
```

- Can paste → Text environment
- Must interact with web pages → Browser Agent

**Text ↔ Coding Agent**

```text
"交付物是对话里的一段文字？还是必须生成文件/跑脚本/构建可运行的东西？"
```

- Conversation text is enough → Text environment
- Must produce files/code/runnable artifacts → Coding Agent

### Difficulty Gates

| Environment | Difficulty | Gate |
| --- | --- | --- |
| Text | ★ | None. Default starting point. |
| Browser Agent | ★★ | None. Low cost, use when the need is confirmed. |
| Coding Agent | ★★★~★★★★ | "有人能看懂 AI 生成的代码并验收吗？" NO → downgrade to Text + manual operation, note the capability gap. |

### Multi-Environment Tasks

When both boundary questions return YES (need both browser AND code):

- **Separable by handoff artifact**: split into sub-tasks. Sub-task A produces a file/data that sub-task B consumes. Route each sub-task independently.
- **Inseparable** (two environments alternate with no clean split): route to Coding Agent (most coding agents include browser capabilities) or Workflow platform for orchestration.

## Decision B: Control Level

Determines HOW MUCH the AI is constrained. This decision is made WITHIN whichever environment was selected in Decision A. It applies to all environments — text, browser, and coding.

### Three Levels

| Level | Core trait | Who executes |
| --- | --- | --- |
| Prompt | One-off instruction, use and discard | AI alone |
| Skill | Reusable rule package, AI has judgment room | AI alone (reads rules, executes autonomously) |
| Workflow | Platform orchestration, multiple actors | Platform coordinates AI + humans + external systems |

The boundary between Skill and Workflow is NOT "whether steps are fixed" — Skills can have fixed steps too. The boundary is "whether the AI is the sole executor."

### Boundary: Prompt ↔ Skill

| Test | Question | YES | NO |
| --- | --- | --- | --- |
| Need | "下次做同样的事，需要重新跟 AI 解释规则/标准/上下文吗？" | → check difficulty | → **Prompt** |
| Difficulty | "这件事 ≥ 每月做一次，且有明确的规则/案例可以固化？" | → **Skill** | → Prompt + save a template doc for manual pasting |

### Boundary: Skill ↔ Workflow

This is the largest difficulty gap (★★★ → ★★★★★), so the escalation gate is the strictest.

**Need tests** — hit ANY ONE to enter Workflow territory:

| # | Question | YES → continue | NO → Skill is enough |
| --- | --- | --- | --- |
| 1 | "过程中需要读写外部系统吗？"（写数据库/调 API/发通知/触发其他工具） | continue | Skill |
| 2 | "跳过某步的后果比'输出质量差'更严重吗？"（合规/数据不一致/钱花错/人没被通知到） | continue | Skill |
| 3 | "流程中有必须等人审批/确认才能继续的环节吗？" | continue | Skill |

**Difficulty tests** — must pass ALL to confirm Workflow:

| # | Question | YES → continue | NO → downgrade |
| --- | --- | --- | --- |
| 1 | "任务频率 ≥ 每周？" | continue | → Skill + humans handle approvals/integrations manually |
| 2 | "有人能搭建和持续维护这个工作流？" | → **Workflow** | → Skill + humans handle approvals/integrations manually |

Any need test YES + both difficulty tests YES → Workflow.
Otherwise → Skill + manual fallback for system interactions.

## Knowledge Overlay

Evaluated independently from environment and control. The result is layered on top of the main route.

### Boundary: No Layer ↔ RAG

```text
"AI 完成任务需要参考的内部资料，能一次性粘贴进对话吗？"
```

- Can paste (< a few pages) → No knowledge layer needed.
- Cannot paste (too many / too scattered / growing / permission-controlled) → check difficulty.

### Difficulty Gates for RAG (★★★★)

| # | Question | YES → continue | NO → downgrade |
| --- | --- | --- | --- |
| 1 | "查询频率 ≥ 每周？" | continue | → manually select key excerpts to paste |
| 2 | "文档会持续更新，不是一次性的？" | continue | → one-time summary document |
| 3 | "有人/有平台能维护知识库索引？" | → **RAG** | → Skill + manually updated summary docs |

All three YES → add RAG layer. Otherwise use the lower-cost alternative.

## Route Composition

The three decisions produce three independent results. Cross them to get the final route:

| Environment | Control | Knowledge | Final Route |
| --- | --- | --- | --- |
| Text | Prompt | None | Chat + Prompt |
| Text | Skill | None | Skill |
| Text | Skill | RAG | Skill + RAG |
| Text | Workflow | Enterprise knowledge | Workflow + Enterprise Knowledge Base |
| Browser | Prompt | None | Browser Agent + Execution Prompt |
| Browser | Skill | None | Skill + Browser Agent |
| Browser | Skill | RAG | Skill + Browser Agent + RAG |
| Coding | Prompt | None | Coding Agent + Handoff Prompt |
| Coding | Skill | None | Skill + Coding Agent |
| Coding | Skill | RAG | Skill + Coding Agent + RAG |
| Coding | Workflow | None | Workflow + Code Nodes |

Combinations emerge naturally from independent decisions. No separate "should I combine?" judgment is needed.

## Recommendation Confidence

| Label | Meaning |
| --- | --- |
| High | One route clearly wins. All boundary questions have unambiguous answers. |
| Medium | One route wins, but one detail could change the environment or control level. |
| Low | Ask another question before recommending. |

Always state what would change the recommendation.

## Upgrade and Downgrade Triggers

Recommendations are not final. Include these signals in the output so the user knows when to re-evaluate.

### Upgrade Signals

| From | To | Trigger |
| --- | --- | --- |
| Prompt | Skill | Same context copy-pasted ≥ 3 times; output quality varies too much across sessions |
| Skill | Workflow | Real approval/integration/notification needs emerge; skipping a step causes an incident |
| Text route | Browser Agent | User frequently operates web pages manually then pastes results to AI |
| Text route | Coding Agent | Data exceeds paste capacity; deliverable must be runnable files |
| Paste context | RAG | User spends significant time finding and pasting excerpts every time; document corpus keeps growing |

### Downgrade Signals

| From | To | Trigger |
| --- | --- | --- |
| Workflow | Skill + manual | No actual approval/integration need; "having steps" was mistaken for needing enforcement |
| RAG | Paste context | Only a few documents are actually used; corpus is not growing |
| Coding Agent | Chat | Generated scripts were used once and never again |
| Skill | Prompt | Packaged rules change every time; no stable pattern to reuse |
