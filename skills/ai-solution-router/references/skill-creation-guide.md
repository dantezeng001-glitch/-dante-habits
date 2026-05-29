# Skill Creation Guide

Use this when the route recommendation is **Skill** and the user wants a reusable skill rather than a one-off prompt or strict workflow.

This guide makes `ai-solution-router` standalone: do not require a separate skill-creator skill.

## When a Skill Is the Right Output

Choose a skill when:

- The work repeats across sessions or people.
- The process has stable judgment rules, examples, style rules, domain context, or templates.
- The task benefits from AI reasoning but needs guardrails.
- The output does not need a strict deployed workflow engine.
- The user wants to package know-how for Codex, Cursor, Claude Code, or similar AI tools.

Do not choose a skill when:

- A one-off chat prompt is enough.
- Every step must be deterministic, audited, approved, or integrated with systems. Use workflow.
- The core output is runnable software. Use coding agent/demo branch.

## Creation Workflow

1. **Clarify use cases**
   - Ask one question at a time until the skill's trigger, inputs, outputs, and examples are clear.
   - Gather 2-3 realistic user prompts the skill should handle.

2. **Plan reusable contents**
   - Decide what belongs in `SKILL.md` and what should move to `references/`.
   - Add `scripts/` only when deterministic code is repeatedly needed.
   - Add `assets/` only when files/templates/images/fonts/boilerplate will be reused.

3. **Create the folder**
   - Use lowercase hyphen-case.
   - Keep the name under 64 characters.
   - Prefer action-oriented names such as `summarize-research`, `write-prd`, `route-ai-solution`.

4. **Write `SKILL.md`**
   - Frontmatter must contain only `name` and `description`.
   - Put trigger conditions in `description`, not in the body.
   - Keep the body focused on core workflow and reference loading.

5. **Add references**
   - Put long templates, domain rules, examples, or checklists in `references/`.
   - Link each reference directly from `SKILL.md`.
   - Avoid deep reference chains.

6. **Add `agents/openai.yaml` for Codex UI**
   - Include display name, short description, and default prompt.

7. **Validate and package**
   - Check frontmatter, naming, file structure, reference links, and sample prompts.
   - Package the folder as zip when sharing.

## Folder Structure

Use the minimal structure needed:

```text
skill-name/
  SKILL.md
  agents/
    openai.yaml
  references/
    guide.md
    templates.md
```

Optional:

```text
skill-name/
  scripts/
    helper.py
  assets/
    template.docx
```

Do not add extra README, install guide, changelog, or process notes unless the user explicitly asks. A skill should contain only what another AI needs to perform the task.

## SKILL.md Rules

### Frontmatter

```yaml
---
name: skill-name
description: Use when [specific trigger/context]. Trigger for [task types, artifacts, situations].
---
```

Rules:

- `name`: lowercase letters, digits, hyphens only.
- `description`: explain when to use the skill, including concrete triggers.
- Do not include process summaries that could cause the model to skip the body.
- Do not use angle brackets in description.
- Keep description under 1024 characters.

### Body

Recommended structure:

```markdown
# Skill Display Name

## Purpose
One or two sentences.

## Core Rules
- Rule 1
- Rule 2

## Workflow
1. Step
2. Step
3. Step

## Output Must Include
- Artifact 1
- Artifact 2

## Reference Loading Guide
- `references/x.md`: when to read it.
```

Keep `SKILL.md` short. Move long templates into references.

## Reference Design

Use progressive disclosure:

- `SKILL.md`: core workflow and when to load each reference.
- `references/`: long examples, prompt templates, output structures, domain rules.
- `scripts/`: executable deterministic helpers.
- `assets/`: files copied or reused in outputs.

Create references by job, not by random notes:

```text
references/
  discovery.md
  output-templates.md
  validation.md
```

For long references, add a table of contents near the top.

## agents/openai.yaml Template

```yaml
interface:
  display_name: "Human Friendly Name"
  short_description: "One short sentence describing value."
  default_prompt: "Use this skill to ..."
```

Keep it aligned with `SKILL.md`.

## Full Skill Skeleton

````markdown
---
name: [skill-name]
description: Use when [trigger conditions]. Trigger for [specific tasks, file types, workflows, or user phrases].
---

# [Skill Title]

## Purpose

[What this skill helps the agent do.]

## Core Rules

- [Rule]
- [Rule]
- [Rule]

## Workflow

1. **[Step]**
   - [Instruction]

2. **[Step]**
   - [Instruction]

3. **[Step]**
   - [Instruction]

## Output Must Include

- [Output]
- [Output]

## Reference Loading Guide

- `references/[file].md`: use when [condition].
````

## Quality Checklist

Before packaging:

- Skill name is lowercase hyphen-case and matches the folder.
- `SKILL.md` starts with valid YAML frontmatter.
- Frontmatter has `name` and `description`.
- Description includes clear triggers and no angle brackets.
- Body tells the AI what to do after the skill triggers.
- Long templates are in `references/`, not crammed into `SKILL.md`.
- Every reference mentioned in `SKILL.md` exists.
- `agents/openai.yaml` exists when sharing for Codex UI.
- No placeholder TODOs remain.
- If scripts exist, they have been run or their untested status is stated.

## Packaging

When creating files in a workspace:

1. Create the skill folder.
2. Add `SKILL.md`.
3. Add `agents/openai.yaml`.
4. Add only needed references/scripts/assets.
5. Zip the whole folder as `[skill-name].zip`.

On Windows PowerShell:

```powershell
Compress-Archive -Path "skill-name" -DestinationPath "skill-name.zip" -Force
```

## Output Contract for AI Solution Router

When this router recommends making a skill, output at least:

```markdown
## Skill Recommendation
- Skill name:
- Why skill instead of prompt/workflow/agent:
- Trigger examples:
- Inputs:
- Outputs:
- Core workflow:
- References needed:
- Validation examples:
```

If the user asks to create it, generate the actual folder and zip when file tools are available.
