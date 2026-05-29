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

3.5. **Surface persona weighting transparently before scoring.**

   The default weights (0.218/0.316/0.163/0.303) come from the 2026 北美品牌用户调研 (n=633, k=4 clustering) and reflect Shokz's overall North America user base. For channel-specific or scenario-specific evaluations, that baseline may not fit. Read `references/weight_presets.md` and follow these substeps:

   **Step A — Show the full weight-preset table to the user**, including data provenance:

   | 预设 | 4 维权重 | 数据来源 | 性质 |
   |---|---|---|---|
   | 默认（北美总盘） | 0.218 / 0.316 / 0.163 / 0.303 | 2026 北美品牌用户调研 n=633 | 调研直接来源 |
   | Costco 渠道 | 0.15 / 0.20 / 0.30 / 0.35 | Costco 用户画像研究（72% female shopper） | 我的判断 |
   | Target 渠道 | 0.13 / 0.20 / 0.35 / 0.32 | Target 客群洞察报告（事实校准版） | 我的判断 |
   | BOS DTC 渠道 | 0.25 / 0.50 / 0.05 / 0.20 | 26 年 3 月骨导运动线 IMC 信息通 | 我的判断 |
   | SEAL 游泳人群 | 0.20 / 0.35 / 0.15 / 0.30 | 26 年 3 月骨导运动线 IMC 信息通 | 我的判断 |
   | 自定义 | 用户输入 | sum = 1.00 ± 0.05 | 用户判断 |

   **Step B — Ask the user one calibration question**: "你这次评估的场景是？如果上述预设都不匹配，请描述目标人群，我会帮你推荐或自定义权重。"

   **Step C — Handle user response**:
   - 选中具体预设：使用对应权重，在最终报告中 cite 该预设的数据来源
   - 自定义：要求用户提供 4 个权重 + 调权理由 + 数据依据 + 关键假设；校验和并 normalize（sum = 1.00 ± 0.05）
   - 描述具体场景但没选预设（5 套预设都不匹配）：**默认走自定义路径**——先基于用户描述给出建议的 4 个权重值 + 调权理由 + 数据依据 + 关键假设。请用户从以下 3 个退出键中选择：
     - **(a) 接受**：使用 skill 建议的自定义权重
     - **(b) 修改**：用户提供自己的 4 个权重 + 理由
     - **(c) 退回预设**：用户明确说"用最近预设" → skill 映射到最近预设并附 "approximated; accuracy reduced" 标签
     不要在用户选择前自行映射或代为决定
   - 不响应或选默认：使用 0.218/0.316/0.163/0.303 并在报告中标注 "using default weights (Shokz 北美总盘)"

   **Step D — Cite the chosen weight's provenance in the final report header**, e.g.:
   - "本次评估使用 Costco 渠道权重，来源：Costco 用户画像研究报告 §1.1（72% female shopper）。本预设为我的判断，非调研直接结论。"
   - Default 预设无须附 "我的判断" disclaimer

4. If details are missing, make concise assumptions and label them.
5. Score every persona from 1 to 5 and assign a stance:
   - 5 = very interested / strong approval
   - 4 = interested / approval with minor caveats
   - 3 = neutral or conditional
   - 2 = low interest / meaningful doubts
   - 1 = rejection or mismatch
6. Compute the weighted overall interest score with the persona weights chosen in Step 3.5 (default or preset). The full score is 5.0 points. Optionally also show a 100-point conversion: `score / 5 * 100`.
7. Add a short evidence section using `references/core_research_findings.md`.

8. **Provide improvement suggestions if weighted_score < 4.0.**

   When the overall weighted score is below 4.0, the concept needs work. Before drafting suggestions, ask the user: "综合分 X.XX / 5.00，需要查看改进建议吗？默认 yes，输入 'skip' 跳过。" If user inputs 'skip', stop here and only output the scoring report.

   Otherwise: Identify the lowest-scoring persona, then:

   - Cross-reference that persona's "Concept Reaction Heuristics" in `personas.md`
   - Suggest 2-3 specific rewrites or additions that would lift that persona's score (e.g., "为科技老白男补一个可量化 proof point，如 '27g' 或 '9hr battery'")
   - For each suggestion, estimate the expected score lift as my judgment (e.g., "+0.3 expected")
   - Label all suggestions as "我的判断" per content-integrity rule; the lift estimate is not a precise prediction

   If multiple personas tie for the lowest score, prioritize the one with the highest cluster weight (largest commercial impact).

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

**Evidence quality flag**: After each persona's interest score, append one of these tags based on how the score was derived:

- `[evidence: high]` — 1+ direct survey finding supports the score (e.g., score for 骨传导跑男 backed by "Running/Jogging 60%" in core_research_findings.md)
- `[evidence: medium]` — Indirect inference from related findings (e.g., extrapolating from purchase drivers to a new use case)
- `[evidence: low]` — Mostly relies on persona Concept Reaction Heuristics with no direct survey evidence
- `[evidence: gap]` — No relevant survey coverage at all; score is hypothesis only

**Overall evidence verdict**: If 2+ persona scores carry `[evidence: gap]`, output a top-level warning `Overall evidence: insufficient — treat results as directional only, not for go/no-go decisions.` Do not force evidence; surfacing the gap is more useful than fabricating support.

## Calculation Helper

For deterministic math, use the helper script. It accepts three input modes:

```bash
# Mode 1: JSON string as argument (preferred on Windows to avoid encoded-path bugs)
python scripts/weighted_score.py '{"scores": {"科技老白男": 4.2, "骨传导跑男": 4.0, "日常颜值派": 3.6, "日常开放派": 3.8}}'

# Mode 2: File path argument
python scripts/weighted_score.py scores.json

# Mode 3: Stdin
echo '{"scores": {...}}' | python scripts/weighted_score.py
```

The input may be either a `scores` object or a plain object keyed by id, name, or persona label:

```json
{
  "scores": {
    "科技老白男": 4.2,
    "骨传导跑男": 4.0,
    "日常颜值派": 3.6,
    "日常开放派": 3.8
  },
  "weights": {
    "preset": "costco"
  }
}
```

If `weights.preset` is provided (one of `default`, `costco`, `target`, `bos_dtc`, `seal_swim`, `custom`), the helper applies that preset's weights. Otherwise it uses the default weights. Preset weight values are defined in `references/weight_presets.md` and mirrored in the script.

Use the helper when exact arithmetic matters, then include the resulting weighted score in the final answer.
