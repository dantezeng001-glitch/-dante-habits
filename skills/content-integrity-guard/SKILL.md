---
name: content-integrity-guard
description: Audits long-form content and multi-document deliverables for three integrity risks — (1) unsupported assertions masquerading as rules (措辞升格 / 添油加醋), (2) cross-document contradictions and factual drift (信息失真 / 交叉矛盾), (3) bloat and lack of concision (信息不凝练 / 堆砌冗余). Outputs a three-tier (green/yellow/red) classification, proposes remediation in place, and sinks findings into a reusable audit log. Use proactively when the user is drafting, updating, or reviewing interlinked long-form documents — marketing briefs, PRDs, content series, white papers, campaign plans, technical narratives — or when the user mentions 长篇内容 / 多篇开发 / 多文档 / 初稿 / brief / 方案 / 评审 / 审计 / 一致性 / 信息凝练 / 信息失真 / 添油加醋 / content audit / cross-document check.
---

# Content Integrity Guard

## What this skill does

Audits long-form, multi-document deliverables for three specific failure modes that AI assistants are prone to when producing a lot of content in one session:

1. **不添油加醋（assertion integrity）** — Catching unsupported claims that have been worded as if they were rules: "按规范 / 必须 / 不得 / 行业通行 / 标准做法 / LinkedIn 受众会 / 算法会" when no external source actually says so.
2. **信息不失真（cross-document fidelity）** — Catching numbers, names, quotes, terminology, and concepts that drift or contradict each other across files: the same product spec written 3 different ways, a figure cited as "3 years" in one doc and "two-and-a-half years" in another, terms translated inconsistently.
3. **信息凝练（concision）** — Catching bloat: redundant hedging, meta-narration, empty emphasis words, paragraphs that add no new information on top of their first sentence.

**Core principle**: *AI 助手可以提出判断，但不能制造规范。* Judgments invite challenge ("this is my view"); rules foreclose it ("this is the standard"). When the source is unclear, prefer the former.

## When to apply this skill

Trigger automatically when **any** of the following is true:

- The user has asked you to draft, update, or review **long-form content** (any single deliverable > ~300 words in a structured doc)
- The session has produced **2 or more interlinked documents** that cross-reference each other
- The user mentions any of: `长篇内容`, `多篇开发`, `多文档`, `初稿`, `brief`, `方案`, `评审`, `审计`, `一致性`, `凝练`, `失真`, `添油加醋`, `content audit`, `cross-document check`, `consistency review`
- **Before declaring a writing task "done"** if that task touched ≥ 2 files in the same project directory

Also apply it **during drafting**, not just after — by following the Self-check before submitting section at the end of each file you write.

## Workflow

### Step 1. Scan

Run `Grep` against the target directory with the patterns from `reference.md` (section "Scan keyword pack"). At minimum run these three groups:

1. **Rule-masquerading words**: `按.*规范|按.*纪律|必须|不得|一律|行业通行|标准做法|天然抗性|免疫度|最佳实践|惯例|约定俗成`
2. **Audience / algorithm claims**: `LinkedIn.*受众会|观众.*会|读者.*会|算法.*会|算法.*压制|算法.*推`
3. **Cross-document drift candidates**: any number (years, countries, sample sizes), any product name, any trademark term — surface all occurrences across files and compare.

### Step 2. Classify each hit into one of three tiers

| Tier | Criterion | Action |
|---|---|---|
| 🟢 **Green** | The assertion has a **verifiable external source** (an official spec doc, a peer-reviewed study, a user-approved brief, an industry publication with URL). | Keep as-is. Optionally add an inline citation. |
| 🟡 **Yellow** | The source exists but is **my own earlier draft** in the same session, OR the wording is too absolute ("must / never / always"). | Soften to "I suggest / my judgment / based on X document in this session". Acknowledge the source is internal. |
| 🔴 **Red** | **No external source at all.** The assertion is pure inference or stylistic preference. | Prepend "**This is my judgment, not backed by data**" (or equivalent in the user's language). Never delete silently — preserve the insight, just relabel its epistemic status. |

### Step 3. Remediate in place

Use the available edit tool to modify each hit per its tier. For multi-file changes, batch them and produce a diff summary.

Before applying in-place fixes across `>= 2` files, stop once and show:

- tier breakdown (`green/yellow/red`)
- the top 3 proposed wording changes
- any unresolved source or ownership question

If the user has only asked for an audit, do not silently remediate. In that case stop at the report and ask whether to apply fixes.

Remediation phrasing templates (with exact examples) are in `reference.md` under "Remediation phrasing pack".

### Step 4. Log

Maintain a single audit log per project directory, named `文档一致性审计报告_v{N}.md` (or `content-integrity-audit-v{N}.md` if the project is English). The log records:

- Scan date and scope
- Number of hits found, broken down by tier
- Full table of hits: file · line · original phrasing · new phrasing · tier
- Any recurring patterns the user should know about
- A 7-item self-check list (reuse the one at end of this SKILL.md) so future writing can be pre-screened

If the log already exists, **append a new version** (v2, v3, ...) rather than overwriting. Each audit is a historical record.

### Step 5. Report to user concisely

Do **not** read the full audit log back to the user. Report:

- How many hits, broken down by tier
- The 1-3 most consequential changes (usually red-tier fixes that affected user-facing wording)
- Any open decisions the user needs to make (often: "who owns this rule — you, IMC, legal, product?")

---

## The three dimensions in detail

### Dimension 1: Assertion integrity (不添油加醋)

**The pattern**: The assistant has a reasonable writing instinct, converts it into authoritative-sounding prose, and over successive revisions upgrades it further ("a suggestion" → "a rule" → "the standard"). By the time the user reads the final draft, the original judgment is invisible and the "rule" is treated as given.

**The test**: For every `必须 / 应该 / 不得 / 按规范 / 符合节奏 / 行业通行 / 标准做法`, ask:

1. Can I name the external document and section where this is stated? If not → not green.
2. If the source is one of my own earlier drafts in this session → yellow.
3. If there's no document at all and this is my inference → red.

**The fix**: Relabel epistemic status. Never delete the insight. "I suggest / my judgment is / based on my reading of X document in this session, which itself is a draft".

### Dimension 2: Cross-document fidelity (信息不失真)

**The pattern**: When producing many interlinked documents, quantitative claims (years, countries, sample sizes, percentages) tend to drift across files. The same source text says "3 years of recording" in one draft and "approximately three years" in another and "2022–2025" in a third. All three are plausible, but they expose the user to risk when someone externally compares the docs.

**The test**: For every quantitative claim or proper noun (product name, trademark, spec), grep **across all touched files** and confirm consistency. A single word difference is a flag.

**The fix**: Standardize to the form the user or the authoritative source has approved. If no authoritative source exists yet → flag as "awaiting confirmation" and **do not propagate** the draft phrasing further.

### Dimension 3: Concision (信息凝练)

**The pattern**: Long-form content tends to accumulate padding:
- **Redundant hedging**: "可能 / 或许 / 一般来说 / 在某种程度上" stacked in the same sentence
- **Empty emphasis**: "非常 / 极其 / 实际上 / 事实上 / 说白了"
- **Meta-narration**: "在下面这一节里我们将讨论" immediately followed by that section
- **Restatement**: paragraph 2 restates paragraph 1 in different words with no new information
- **List inflation**: items in a list that all say "please note / it's worth emphasizing that / importantly"

**The test**: For each paragraph, ask "what fact or argument did this paragraph add on top of the previous one?" If the answer is "it restates the previous one with softer / stronger emphasis" → delete or collapse.

**The fix**: Prefer deletion over rewriting. If two sentences say the same thing, keep the shorter one. If a paragraph's only job is to transition, often the transition can be a single phrase.

Bloat keyword grep patterns are in `reference.md` under "Bloat detectors".

---

## Self-check before submitting

Before you tell the user a writing task is "done" (especially one that touched ≥ 2 files), pass these 7 questions:

1. **Every `应该 / 必须 / 不得 / 一律` answers "which document, which section?"** If not → change to `我建议 / 我判断`.
2. **Every claim about `受众会 / 算法会 / 读者会` has a citation or study.** If not → mark as "my judgment, no data".
3. **Every number** (years, countries, samples, percentages) comes from an approved source. If not → mark as "awaiting confirmation" and do not propagate to other files.
4. **Every `标准做法 / 行业通行 / 最佳实践`** is actually an industry norm, not a personal habit. If not → change to `我的写作习惯`.
5. **Every `节奏 / 规范 / 纪律`** is in an existing planning document. If not → change to `我建议的节奏` and surface it as a decision point for the user.
6. **Every `我们`** has a clear antecedent — is it "I (the assistant)", "营销侧", "the brand", or "the whole project"?
7. **Run the scan in Step 1** one final time. Any new hits introduced by recent edits?

Only when all 7 are green should the task be declared complete.

---

## Additional resources

- Full scan keyword pack (grouped by risk category): [reference.md](reference.md) → "Scan keyword pack"
- Remediation phrasing templates with before/after examples: [reference.md](reference.md) → "Remediation phrasing pack"
- Bloat detectors (Dimension 3 keyword list): [reference.md](reference.md) → "Bloat detectors"
- Audit log template: [reference.md](reference.md) → "Audit log template"
