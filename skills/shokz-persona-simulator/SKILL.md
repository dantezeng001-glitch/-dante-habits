---
name: shokz-persona-simulator
description: Simulate Shokz product-user reactions using four survey-derived persona segments and core research findings from the 2026 Shokz user questionnaire. Use when evaluating Shokz product concepts, feature ideas, advertising ideas, slogans, taglines, campaign routes, creator/social content, or other marketing-material concepts; provide persona-by-persona stances, 1-5 interest scores, weighted overall interest score, and supporting/caution evidence from survey findings.
---

# Shokz Persona Simulator

Use this skill to estimate how four typical Shokz user persona segments may react to a product or marketing concept. The output is a structured simulation, not a replacement for live concept testing.

## Workflow

1. Read `references/personas.md` before scoring.
2. Read `references/core_research_findings.md` to identify survey evidence that supports, cautions against, or leaves gaps for the concept.
3. Parse the concept: product/feature, audience, occasion, message, proof points, tone, channel, price or offer if available.
4. If details are missing, make concise assumptions and label them.
5. Score every persona from 1 to 5 and assign a stance:
   - 5 = very interested / strong approval
   - 4 = interested / approval with minor caveats
   - 3 = neutral or conditional
   - 2 = low interest / meaningful doubts
   - 1 = rejection or mismatch
6. Compute the weighted overall interest score with the persona shares in `references/personas.md`. The full score is 5.0 points. Optionally also show a 100-point conversion: `score / 5 * 100`.
7. Add a short evidence section using `references/core_research_findings.md`.

## Scoring Priorities

Evaluate each concept on:

- relevance to the persona's core usage occasions
- clarity of the benefit and message
- credibility of proof, product claims, or reason-to-believe
- fit with Shokz equities: open-ear, comfort, safety/awareness, sports/active lifestyle, technology, design, quality
- fit with product category expectations: bone-conduction, ear-hook, and ear-clip
- likely friction: price, overclaiming, too much niche-athlete framing, too much abstract branding, lack of service reassurance

## Output Format

Return a compact table with:

- persona name
- cluster weight
- persona profile summary: include age, gender skew, race/ethnicity skew if relevant, product-category tendency, and core usage occasions in one short phrase
- stance: `赞成`, `有条件赞成`, `无感/观望`, `有疑虑`, or `不赞成`
- interest score, shown as `x/5`
- why it works
- concern or barrier
- likely user thought, written as a short first-person quote in that persona's voice

Then calculate:

```text
weighted_score = 0.218009 * score_科技老白男
               + 0.315956 * score_骨传导跑男
               + 0.162717 * score_日常颜值派
               + 0.303318 * score_日常开放派
```

Show:

- `综合兴趣得分：x.xx / 5.00（满分 5 分）`
- optional `折算百分制：xx / 100`
- one-line diagnosis: strongest audience, biggest risk, and highest-leverage improvement

Then add:

- `调研支持证据`: 1-3 bullets from `core_research_findings.md` that make the concept more plausible.
- `调研风险/不支持点`: 1-3 bullets from `core_research_findings.md` that weaken or complicate the concept.
- `证据缺口`: mention missing evidence when the concept depends on topics not directly covered, such as pricing, creator choice, retail conversion, or competitive claim testing.

Do not force evidence. If the reference does not speak to a concept, say that the survey offers limited direct evidence and keep the persona score as a hypothesis.

## Calculation Helper

For deterministic math, use:

```bash
python scripts/weighted_score.py scores.json
```

The input may be either a `scores` object or a plain object keyed by id, name, or persona label:

```json
{
  "scores": {
    "科技老白男": 4.2,
    "骨传导跑男": 4.0,
    "日常颜值派": 3.6,
    "日常开放派": 3.8
  }
}
```

Use the helper when exact arithmetic matters, then include the resulting weighted score in the final answer.
