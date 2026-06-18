# Proofreading Rules

These rules are domain-neutral. When the task belongs to a known domain, also load the matching preset under `domain-presets/` for domain-specific sub-types and checks.

## Baseline hierarchy

1. User-explicit baseline instructions from the current conversation.
2. The user-confirmed baseline master and exact location/scope, such as a specific workbook sheet, page range, row range, column set, product/SKU block, language block, legal section, localization source file, or named paragraph.
3. Any user-confirmed auxiliary source, limited to the role the user assigned it. For example, a SPEC sheet can support only hard parameters if the user says so; a brand glossary can support only terminology.
4. Target document source text, only for synchronization analysis when the relationship is translation and the source is inside the confirmed scope.
5. Existing target wording only for internal consistency analysis, not as official truth.

Never silently expand the baseline to other sheets, sections, or documents. If a visible target item is not covered by the confirmed scope, pause and ask for the matching baseline instead of guessing.

## Baseline confirmation

Before proofreading, check whether the conversation clearly specifies all of these:

- Baseline master file/document.
- Exact baseline location and limits: sheet, tab, page, row range, columns, SKU/version, languages, or section.
- Source-target relationship: translation (with the language pair), same-language different version, spec vs. implementation, full vs. condensed, or other. This decides which judgment logic applies.
- Target file(s) to check.
- Batch behavior for multiple target files.

If any item is missing, ask for it. If the user has already specified something like “use the NCE WBS document’s `包装卖点文案` sheet and check only packaging sleeves,” proceed without asking again.

## Baseline integrity (run before mechanical proofreading)

A confirmed sheet name does not guarantee the sheet describes the target product. Verify integrity first:

1. Product identity: match model/SKU, product name, and category between baseline and target. If the baseline states a different model or describes a different product form (ear-hook vs. clip-on, over-ear vs. in-ear), the named baseline is suspect; report it and ask before judging the target.
2. Cross-sheet consistency: when a package has both a content sheet and a parameter sheet, spot-check hard facts (Bluetooth version, IP rating, runtime, charging time, weight). On conflict, mark `基准冲突`; do not silently choose.
3. Placeholder cells: a baseline value of `?`, `待确认`, `TBD`, or empty is `基准待确认`. Do not judge the target against an unfilled baseline.

If the named baseline fails identity but another sheet matches the target product, recommend the matching sheet and wait for user confirmation. Proofreading against a mismatched baseline produces confident but wrong findings.

## Multi-language / matrix targets

When the target has many language/version columns:

- Check every language column against the user-confirmed source column for synchronization, and against the baseline for facts.
- Treat draft/proofread column pairs (e.g. `德语-初版-翻译公司产出` vs `德语-内部校对` / `ChatGPT 4o校对`) as draft-vs-proofread; report where the proofread column still carries draft errors.
- Cross-version differences for the same row (简中 vs 大中华 vs 国际) are `术语不统一` or positioning differences to report, not automatic errors.
- Language keyword detection covers only CN/EN/FR/NA. For other languages, read the header text or ask; never guess from a substring.

## Five-dimension model

Classify every finding into exactly one dimension, then pick a sub-type for display.

### Accuracy

Target conflicts with a baseline fact or hard parameter, or violates standard language rules.

- Factual mismatch: target changes a function, feature presence/absence, usage scenario, packaging/inclusion list, name/SKU/model, URL, QR, SN location, safety limitation, claim condition, or risk wording compared with the confirmed baseline.
- Parameter mismatch: hard values, units, ranges, conditions, or subjects differ from the confirmed baseline or a confirmed auxiliary parameter source. Examples: `25 hours` vs `27 hours`, `IP54` vs `fully waterproof`, different charge time, missing `with charging case`, per-unit vs total quantity.
- Grammar & Spelling Error (语法与拼写错误): Violations of standard English grammar, spelling, and syntax. Examples:
  - Subject-verb agreement (e.g., `Audrey say` -> `Audrey says`).
  - Missing articles (e.g., `first device` -> `the first device`, `Answer call` -> `Answer a call`).
  - Missing copulas/auxiliaries (e.g., `you in the pool` -> `you are in the pool`, `headphones powered off` -> `headphones are powered off`).
  - Spelling typos (e.g., `paring` -> `pairing`).
  - Incorrect prepositions (e.g., `Double-click on the button` -> `Double-click the button`).
  - Incorrect conjunction structures (e.g., `so that to confirm` -> `to confirm` or `and confirm`).

### Sync

Baseline or source has changed but target still reflects older or different content.

- Source not synchronized: when the relationship is translation, the source row changed but the target language copy still reflects older content. Compare subject, value, scope, limitation, conditional phrase, action, object, and claim strength.
- Old-version contamination: the target still carries wording that the baseline change notes mark as replaced or removed.

### Consistency

The same concept appears with different wording or format inside the target or project.

- Terminology inconsistency: the same product, feature, accessory, app, technology, or action appears with multiple translations or formats. Examples: name capitalization, app name, technology names, `earbuds` vs `earphones` vs `headphones`, `charging case` vs `charger` vs `case`, action names such as tap/press/hold.
  - **UI & Button Capitalization Consistency**: Physical button names (e.g., `Multifunction Button`, `Power/Volume + Button`, `Volume - Button`) and UI indicators (e.g., `LED Indicator`) must be strictly capitalized (Title Case) and consistent. Lowercase button names (e.g., `multifunction button` or `Volume + button`) are errors.
- Format inconsistency: dates, units, punctuation, capitalization style, or number formatting differ across the target where they should match.
  - **Typographical & Spacing Standards**: Standard typesetting requires:
    - Exactly one space after a sentence-ending period (e.g., `countries. Google`, not `countries.Google`).
    - Spaces around operators in button names (e.g., `Volume + Button`, not `Volume+ Button`).
    - Spaces after list numbering (e.g., `8. Turn`, not `8.Turn`).
    - Standard half-width English colons (`:`) with no space before them (e.g., `Audrey will say:`, not `Audrey will say :`).
    - No CJK full-width punctuation (e.g., `：`, `。`) in English text.
    - Missing sentence-ending periods must be flagged.
    - Number formatting in body text (numbers under 10 should be spelled out, e.g., `2 EQ modes` -> `two EQ modes`).
    - Chapter headings consistency (e.g., `Check Battery Status` -> `Checking Battery Status` to match other gerund headings).

If context may justify different terms, record it as `语境差异` or `术语不统一，需确认`, not a confirmed error.

### Tone

Facts match, but expression differs materially.

- Style difference: more marketing-oriented, more technical, more formal, more casual, more consumer-facing, or more engineering-facing than the baseline pattern. Not an error by default.
- Expression-strength difference: the target strengthens or weakens a claim. Watch words like `fully`, `ultimate`, `best`, `guaranteed`, `always`, `never`, `perfect`, `waterproof`, and similar absolute or broad terms.
- Granularity difference: broadly true but missing or adding conditions, ranges, examples, limitations, steps, subjects, paths, or measurement context.

### Scope

Target is outside the confirmed baseline, baselines conflict, context may justify the difference, or evidence is insufficient.

- Out-of-baseline-scope: target content is visible but not covered by the confirmed baseline location. Use this and ask for the matching baseline; do not mark it wrong.
- Baseline conflict: two confirmed baseline sources conflict, or the confirmed baseline conflicts with the source text. Record it; do not silently choose one.
- Contextual difference: a reasonable difference caused by usage context (front-of-pack short copy vs. manual instructions, heading vs. body, e-commerce vs. safety copy, regional English variants, French vs. English convention). Mark severity `可接受差异` when likely reasonable.
- Needs confirmation: evidence is insufficient to determine a correction.

## Scope-gating rules

Report and pause for confirmation when target content is outside the confirmed baseline scope. Common examples:

- The baseline is a selling-point sheet, but the target contains legal statements, safety warnings, importer addresses, warranty terms, certification marks, or bottom-sticker text.
- The baseline covers a regular product, but the target contains Mini, special color, regional SKU, bundle, or accessory-specific wording not present in that baseline.
- The baseline covers one language version, but the target contains additional languages, manual instructions, app QR copy, or regulatory symbols not in scope.
- The baseline covers only one area (such as a front panel), but the target has other-area copy not listed there.

Use sub-type `不在本轮基准范围`; do not mark it wrong unless a confirmed baseline exists.

## User-confirmed auxiliary sources

Use auxiliary sources only within their confirmed role:

- A parameter sheet (such as `SPEC`): hard parameters only, and only if the user confirms it.
- Brand glossary or legal guide: official terminology and mandated legal phrasing only.
- Prior final artwork: layout/context reference, not factual authority unless the user says it is final copy.

If two confirmed baseline sources conflict, record `基准冲突` instead of silently choosing one.

## Official translation handling

When the relationship is translation, assume no official translation exists unless one of these is provided or clearly marked:

- User-provided terminology glossary.
- Brand or legal translation guide.
- Confirmed final target-language copy.
- A baseline term explicitly labeled as the official target-language name.
- Parameter-sheet target wording for a hard parameter, limited to that parameter.

If there is no official translation, still record differences in terminology, tone, style, strength, and granularity. Do not present your own translation as official.

## Change-note handling

Prioritize baseline change traces such as dates, comments, colored text, highlights, red text, notes like `待确认`, `已修改`, `更新为`, `从 x 改为 y`, side-by-side old/new content, strikethrough, and replacement wording. When a target column still reflects older wording, classify it as old-version contamination or source not synchronized.

If the baseline says a point is pending or uncertain, do not mark the target copy as definitely wrong. Classify as `需确认` or `基准待确认`.

## Source and target detection

Identify which content is source and which is target from the user-confirmed relationship first. Do not infer from column headers when the user has already told you the mapping.

When the relationship is translation and the user has not specified columns, you may use these keywords as heuristic hints only (not the baseline):

- English: `英文`, `english`, `en`, `us english`.
- North America: `北美`, `na`, `north america`, `us`, `canada`.
- French: `法文`, `french`, `fr`, `fr-ca`, `canadian french`.
- Chinese/source: `中文`, `cn`, `chinese`, `原文`, `源文案`.

For other language pairs, ask the user which columns/sections are source and target rather than guessing.

Avoid false positives:

- `n/a` does not mean North America.
- `name` does not mean `na`.
- `en` inside a word does not mean English.
- Empty columns, notes-only columns, version columns, and status columns are not copy columns unless their content clearly contains target copy and the user included them in scope.

## Judgment quality layer

### Clustering

Aggregate findings by problem fingerprint: same dimension + same sub-type + same root cause = one finding. Put the representative wording in the original-text field and list all affected locations. Do not emit one row per occurrence of the same root problem.

A root cause is the same when the underlying correction is identical, for example the same term pair confused everywhere, or the same parameter value wrong everywhere. If two occurrences would need different corrections, keep them separate.

### Evidence sourcing

Every finding's evidence field must quote the exact baseline fragment plus its location.

**Exception for Linguistic, Grammatical, Spelling, and Typographical Errors**:
Standard language grammar, spelling, punctuation, spacing, and typographical rules are self-evident authorities. When reporting a grammar error (e.g., subject-verb agreement, missing articles/copulas), spelling error, punctuation error (e.g., CJK punctuation in English), or spacing error (e.g., missing space after period), you do NOT need a product-specific baseline fragment to prove it. You can cite standard English grammar/typesetting rules as the authority, and mark it as a high-confidence error (`高`置信度).

If the issue is a product fact or parameter, you must quote a baseline fragment. If you cannot quote a baseline fragment that proves a product-specific issue:

- Do not call it an error.
- Set the sub-type to `需确认` and confidence to `低`.
- Explain what evidence would resolve it.

This mirrors the content-integrity principle: offer a judgment, but never manufacture a standard.

### Severity and confidence

Report two independent dimensions for every finding.

Severity (consequence if wrong):

- `高`: factual, parameter, safety, legal/compliance, URL, SKU/model, SN, packaging-list, or strong-claim risk.
- `中`: likely unsynced copy, terminology inconsistency, old-version wording, meaningful omission/addition, or content outside the confirmed scope that needs a new baseline.
- `低`: factually correct style, tone, strength, or granularity difference.
- `可接受差异`: context likely explains the variation.

Confidence (certainty it is a real problem):

- `高`: an exact baseline fragment directly proves it, and no plausible context justifies the target wording.
- `中`: the baseline supports it, but some context, version ambiguity, or translation convention could still explain the target.
- `低`: suspected from internal patterns or weak signals, with no baseline fragment that directly proves it.

Do not default every finding to `中` confidence. If you find yourself marking most findings `中`, recheck whether the evidence actually supports `高`, or whether the finding should be downgraded to `需确认` at `低`.

## Batch handling

When several target files are provided and the user has not explicitly asked to process all at once:

1. Choose the first relevant target file, or the one named first by the user.
2. Output findings for that file only.
3. Pause for user feedback before continuing.
4. Apply the user's feedback to the remaining files.

Do not promise background work. Continue only within the current conversation turn or after the user replies.

## Reporting discipline

Every finding must include: target file/location, baseline location, original text, suggested handling, dimension, sub-type, severity, confidence, and evidence (a quoted baseline fragment). If evidence is ambiguous, say `需确认` and explain the ambiguity. If a correction is only a consistency suggestion, label it as such.
