---
name: ai-solution-router
description: "Use when a user has a vague task, workflow, business problem, product idea, repetitive job, research/data/code need, or 'what AI tool should I use' question. Also trigger on: AI工具选型, 该用什么AI, 用什么工具, 需求分析, AI方案推荐, 帮我选工具, 我想用AI做, tool selection, demand discovery, prompt generation, skill/workflow design, browser-agent task planning, or product demo development."
---

# AI Solution Router

## Purpose

Help the user discover the most suitable AI solution for their real need: simple chat prompt, reusable skill, strict workflow, knowledge base/RAG layer, AI browser agent, AI coding agent/product demo, or a lightweight combination of these.

Start from discovery, not tool preference. The same surface request can map to different tools depending on effort, repeatability, structure, execution environment, and risk.

## Core Rules

- Ask exactly one question at a time during discovery.
- Continue with targeted follow-ups until you can answer all items in the confidence checklist (see `references/discovery.md`). If the user's first message already covers 3 of 4 key dimensions (input, output, frequency, workspace), skip to routing and mark gaps as assumptions.
- Do not recommend a tool category before understanding the real task, current workaround, frequency, cost, input/output, success criteria, and user capability.
- Use the decision tree only after discovery, not as a rigid questionnaire.
- Start from the simplest route. Escalate only when there is a hard, testable reason AND the implementation difficulty is justified.
- Route through three independent decisions: execution environment (where), control level (how constrained), and knowledge source (what the AI knows). Combine the results — do not treat the six route types as a flat pick-one list.
- Heavier solutions need higher justification. Prompt and Browser Agent need only a confirmed need; Skill needs monthly recurrence; Coding Agent needs someone who can review output; RAG and Workflow need weekly frequency plus ongoing maintenance capacity.
- When recommending specific current products, treat product names as examples unless the user asks for a current market comparison.
- This skill's job ends at route handoff. For Coding Agent routes, produce a handoff prompt; do not embed full product development inside the router. The optional `references/demo-build-branch.md` and `references/product-demo-templates.md` are extended modules — load them only when the user explicitly asks for end-to-end product development from this same conversation.

## Workflow

1. **Discovery**
   - Input: user's initial message describing their task or problem.
   - Read `references/discovery.md`.
   - Start with the opening question. If the user's first message covers 3 of 4 key dimensions (input, output, frequency, workspace), skip to Step 2 and mark gaps as assumptions.
   - Ask one question at a time. Update your confidence after each answer.
   - Output: completed confidence checklist with all items answered or marked as assumptions.
   - Stop condition: you can make all three routing decisions and explain why two alternatives are weaker.

2. **Route Selection**
   - Input: completed confidence checklist from Step 1.
   - Read `references/decision-tree.md`.
   - Make three independent decisions:
     - Decision A — Execution environment: text, browser, or code?
     - Decision B — Control level: prompt, skill, or workflow?
     - Overlay — Knowledge source: paste context, RAG, or enterprise knowledge?
   - For each decision, apply both the need test and the difficulty gate.
   - Combine the three results into the final route.
   - Output: route = environment × control × knowledge, with reasoning per axis.

3. **Route Confirmation** *(checkpoint — do not skip)*
   - Input: route recommendation from Step 2.
   - Present the recommendation using the Lightweight or Full template from `references/output-templates.md`. Choose Lightweight when confidence is High and the route is a single tool; choose Full otherwise.
   - Explicitly state: three-axis judgment, difficulty assessment, upgrade/downgrade triggers, and remaining assumptions.
   - Ask the user to confirm, adjust, or reject.
   - If confirmed → proceed to Step 4.
   - If adjusted → revise the affected axis and re-present.
   - If rejected → return to Step 1 with a targeted follow-up based on the disagreement.
   - Output: user-confirmed route.

4. **Generate the Right Output**
   - Input: user-confirmed route from Step 3.
   - Read `references/output-templates.md`.
   - For AI chat: generate a ready-to-use prompt.
   - For skill: read `references/skill-creation-guide.md`, then generate a skill brief or full skill files if requested.
   - For workflow: generate node design, inputs/outputs, decision rules, and test cases.
   - For browser agent: generate tool choice guidance and an execution prompt.
   - For coding agent: generate a handoff prompt (see Coding Agent Output in `references/output-templates.md`). Stop here unless the user explicitly asks to continue with full product development in this conversation — in that case, load `references/demo-build-branch.md`.
   - Output: concrete artifact matching the confirmed route.

5. **Confirm and Package**
   - Input: generated artifact from Step 4.
   - Ask the user whether they want the artifact created as files.
   - If creating files, use clear names such as `AI工具选型建议.md`, `推荐Prompt.md`, `workflow-design.md`, or a skill folder.
   - Include assumptions, confidence score, and what would change the recommendation.
   - Output: delivered files or in-conversation artifact.

## Decision Summary

Three independent decisions, combined into the final route. Full questions, difficulty gates, and downgrade paths live in `references/decision-tree.md` — load that file before routing.

| Axis | Core question |
| --- | --- |
| A. Environment | Where does the work physically happen — text, browser, or code? |
| B. Control | How constrained must the AI be — one-off prompt, reusable skill, or platform-orchestrated workflow? |
| C. Knowledge | Can references be pasted, or is a RAG / enterprise knowledge layer needed? |

Final route = A × B × C. Each escalation needs both a need test AND a difficulty justification.

## Output Must Include

- User need summary.
- Confidence score and remaining assumptions.
- Recommended route (environment × control × knowledge).
- Why this route beats the alternatives.
- Suggested tool examples, framed as examples rather than exclusive choices.
- Difficulty assessment and whether the user has the capability to implement.
- Upgrade and downgrade triggers: what signals mean the route should change.
- Concrete next artifact: prompt, skill spec, workflow node map, browser-agent prompt, or coding-agent handoff.
- Validation method: how the user can test whether the recommendation is right.

## Reference Loading Guide

- `references/discovery.md`: use before any recommendation.
- `references/decision-tree.md`: use when routing the clarified need.
- `references/enterprise-knowledge-rag.md`: use when the task touches internal company knowledge, documents, policies, SOPs, cases, search, citations, or permissions.
- `references/output-templates.md`: use when producing the final artifact.
- `references/skill-creation-guide.md`: use when the chosen route is Skill, especially when creating a standalone skill folder or zip.
- `references/demo-build-branch.md`: **optional extended module**. Load only when the user explicitly asks to continue from route handoff into full product development inside the same conversation.
- `references/product-demo-templates.md`: **optional extended module**. Load only inside the demo-build branch when generating PRDs, technical docs, mock plans, acceptance docs, or README/demo-data specs.
