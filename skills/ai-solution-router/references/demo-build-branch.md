# Demo Build Branch

Use this when the selected route is **AI Coding Agent + product/demo build**. This branch is standalone: do not assume another skill is installed.

## When to Use

Use this branch when:

- The user wants a product, internal tool, dashboard, app, data tool, AI feature, or runnable demo.
- The task needs code, multiple files, local execution, sample data, scripts, or mock services.
- A vague business problem must become a PRD, technical design, and runnable prototype.
- The user already has a PRD or technical brief and wants to continue from that stage.

## Non-Negotiable Rules

- Ask one question at a time until reaching 95% confidence.
- Produce Chinese-facing artifacts unless the user asks otherwise.
- Mark inferred details as `【假设】`.
- Prefer local runnable demos over elegant but fragile architecture.
- Mock every external dependency unless the user has already verified access.
- Include sample data whenever uploads, imports, or seeded records are required.
- Verify before claiming completion, or state exactly what was not verified.

## Entry Routing

| User input | Start point |
| --- | --- |
| Vague product idea or business problem | Discovery |
| Transcript/interview notes | Requirement analysis |
| Product solution doc | PRD |
| PRD | Technical delivery docs |
| Technical docs | Implementation |
| Existing codebase with goal | Inspect codebase, then implementation plan |

If the entry is unclear, ask one question:

```text
你现在手里最完整的材料是哪一种：一句话想法、访谈记录、产品方案、PRD、技术文档，还是已有代码项目？
```

## Workflow

1. **Discovery**
   - Ask one question at a time.
   - Reach 95% confidence on goal, user, current workflow, MVP boundary, data, dependencies, risks, and demo success.
   - If the user provides a transcript, skip basic discovery and analyze the transcript.

2. **Requirement Analysis**
   - Read `references/product-demo-templates.md`, section "Requirement Analysis Templates".
   - Produce:
     - `01_访谈分析报告.md`
     - `02_追问补全分析报告.md`

3. **Product Documents**
   - Read `references/product-demo-templates.md`, section "Product Plan and PRD Templates".
   - Produce:
     - `产品方案文档.md`
     - `产品PRD.md`

4. **Technical Delivery Docs**
   - Read `references/product-demo-templates.md`, section "Technical Delivery Templates".
   - Produce:
     - `TECH_DESIGN.md`
     - `MOCK_SERVICES.md`
     - `FUTURE_INTEGRATION.md`
     - `ACCEPTANCE.md`
     - `README.md`
     - `DEMO_DATA/`

5. **Implementation**
   - Build the shortest complete demo path.
   - Use existing project conventions first.
   - If greenfield, choose a low-setup stack.
   - Mock all external dependencies by default.
   - Include a 3-5 minute demo script.

6. **Verification**
   - Run install/build/test commands when available.
   - Start the app if possible.
   - Complete the demo path using sample data.
   - Confirm no external account/key is required in mock mode.
   - State any unverified gaps.

## Default Artifact Structure

```text
project/
  docs/
    01_访谈分析报告.md
    02_追问补全分析报告.md
    产品方案文档.md
    产品PRD.md
    TECH_DESIGN.md
    MOCK_SERVICES.md
    FUTURE_INTEGRATION.md
    ACCEPTANCE.md
  DEMO_DATA/
    README.md
    sample_*.csv/xlsx/pdf/json
  README.md
  .env.example
  src/
```

Adapt paths to an existing repo's conventions.

## Coding Agent Handoff Prompt

Use this when a coding agent should implement the demo:

```text
You are in implementation mode. Turn the clarified business need and product documents into a runnable local demo.

Priorities:
1. Make the mock-mode demo run locally.
2. Implement the shortest complete user path from sample data/input to final output.
3. Mock every external dependency by default.
4. Keep architecture simple and consistent with the existing project.
5. Update README, sample data, and acceptance docs to match the actual run path.
6. Run verification before claiming completion.

Required outputs:
- Runnable code
- README with install/run/demo steps
- DEMO_DATA with realistic sample data
- Mock service or mock adapter docs
- Acceptance checklist and demo script
```
