# Enterprise Knowledge and RAG

Use this reference when the user's task depends on internal company knowledge, policies, SOPs, documents, cases, meeting notes, customer records, or permission-controlled content.

## Core Rule

Do not treat internal enterprise knowledge as ordinary chat context unless the user only needs a small one-off answer from pasted text.

If the task needs repeated retrieval, citations, permissions, or many internal documents, explicitly consider a **knowledge base / RAG** layer — but apply the difficulty gates from `references/decision-tree.md` before recommending it.

## Three Tiers (lightest first)

Always recommend the lightest tier that meets the need. Only escalate when there is a hard reason.

### Tier 1: Enterprise-Native Knowledge Search

Use when:

- The user only needs to find answers in internal documents.
- No multi-step execution is needed.
- The company already uses a collaboration suite with built-in AI search.

Recommendation pattern:

```text
Primary route: enterprise knowledge search (built into the user's existing collaboration platform)
Examples: DingTalk enterprise search, Feishu AI search, Notion AI, Microsoft Copilot, Google Workspace AI
Output: search/query prompt and validation questions.
```

Choose the example that matches the user's stated platform. If the user has not stated a platform, ask which one they use rather than assuming.

### Tier 2: Knowledge Base / RAG + Workflow or Agent

Use when:

- Internal knowledge must drive drafting, classification, approval routing, customer response, SOP execution, or agent decisions.
- The user wants a bot/workflow/agent that repeatedly uses company knowledge.
- The output needs source references or permission-aware retrieval.

Recommendation pattern:

```text
Primary route: workflow/agent platform with knowledge base integration
Examples: DingTalk Wukong, Feishu AI assistant, Dify + knowledge base, Coze + knowledge base
Knowledge layer: enterprise knowledge base / RAG
```

### Tier 3: Custom RAG + Coding Agent

Use when:

- Sources are scattered across many systems.
- Permissions, freshness, retrieval quality, or evaluation need custom design.
- The desired output is a product, dashboard, tool, API, or local demo.

Recommendation pattern:

```text
Primary route: AI coding agent
Knowledge layer: custom RAG pipeline
Reusable logic: skill/prompt templates
Output: demo-build branch with RAG requirements.
```

## Difficulty Gates (aligned with decision-tree.md)

Before recommending Tier 2 or 3, check the RAG difficulty gates:

| # | Gate | YES → continue | NO → downgrade |
| --- | --- | --- | --- |
| 1 | Query frequency ≥ weekly? | continue | → Tier 1 or paste excerpts |
| 2 | Documents update regularly? | continue | → one-time summary document |
| 3 | Someone can maintain the knowledge index? | → proceed with RAG | → Tier 1 + manually curated excerpts |

All three YES → Tier 2 or 3 is justified.
Any NO → downgrade to the lighter alternative shown in the table.

## Platform Neutrality

When recommending specific platforms, follow these rules:

- Use the platform the user already mentioned. If they said "we use DingTalk", use DingTalk examples. If they said "we use Feishu", use Feishu examples.
- If the user has not stated a platform, list 2-3 examples across ecosystems rather than defaulting to one.
- Do not embed platform-specific recommendation language (e.g. pre-written sales phrases). Let the routing logic speak for itself.

## Knowledge Requirements Checklist

Before recommending the final architecture, identify:

- Knowledge sources: docs, wiki, drive, CRM, tickets, meeting notes, SOPs, PDFs, spreadsheets, databases.
- Retrieval scope: all company, department, project, role-based, or user-provided files.
- Permission rules: who can see what.
- Citation needs: source title, URL, paragraph, timestamp, owner.
- Freshness: real-time, daily sync, manual upload, archive.
- Quality tests: representative questions and expected documents.
- Failure mode: what to do when knowledge is missing, stale, or contradictory.

## Output Template

```markdown
## 企业知识 / RAG 判断
- 是否涉及内部知识：是/否
- 知识用途：查阅 / 问答 / 生成 / 决策 / 执行 / 审批
- 推荐知识层：企业原生搜索 / 知识库RAG / 自定义RAG
- 难度门槛：三关是否全过
- 推荐主工具：

## 推荐方案
（说明为什么选这个 tier；如需组合，列出主工具、知识层、执行层）

## 知识源与权限
| 知识源 | 位置 | 权限 | 更新频率 | 引用要求 |

## 最小验证集
| 测试问题 | 期望来源 | 合格标准 |
```
