---
name: document-proofreader
description: interactive cross-document proofreading for any source-to-target comparison, including packaging, manuals, legal statements, stickers, material copy, gtm workbooks, software localization strings, web copy, and technical documentation. use when a user wants to compare uploaded or connected target files against a user-confirmed source-of-truth baseline such as a specific workbook, sheet, page, row range, column set, brand guide, legal text, localization source, or product information document. the skill pauses to confirm the baseline, scope, and source-target relationship before review, classifies every finding by a five-dimension model (accuracy, sync, consistency, tone, scope), clusters repeated issues into one finding, requires each finding to cite baseline evidence, reports separate severity and confidence, stops when target content falls outside the confirmed baseline, and handles batches by proofreading one file first before continuing after user feedback.
---

# Document Proofreader

## Purpose

Use this skill to proofread any target document against a user-confirmed source-of-truth baseline. The original focus was packaging, instruction, legal, sticker, material, and GTM copy, but the skill is domain-neutral: the same workflow handles software localization, marketing collateral, legal/compliance text, technical documentation, and e-commerce listings. The skill is interactive by default: first confirm the baseline, scope, and the source-target relationship, then compare only the target content covered by that scope.

## Non-negotiable defaults

- Do not edit, overwrite, or save changes into any source document.
- Do not assume `Product Info`, `SPEC`, `包装卖点文案`, or any other sheet, section, or file is the baseline unless the user explicitly confirms it or the current conversation already makes it unambiguous.
- Treat the user-confirmed baseline and its confirmed location as the highest authority. A baseline location may be a workbook sheet, document section, page range, row range, column set, SKU block, language block, named paragraph, or any other clearly bounded region.
- Keep the proofreading scope limited to the confirmed location. If target content falls outside that scope, stop and ask the user to provide or confirm the right baseline before judging it.
- Every reported finding must cite an exact baseline fragment and its location as evidence. **Exception**: Self-evident linguistic, grammatical, spelling, and typographical errors (such as subject-verb agreement, missing articles, spelling typos, CJK punctuation in English, and spacing issues) are governed by standard language rules and do not require a product-specific baseline fragment to be marked as confirmed errors (`高`置信度).
- Report differences, not only errors. Cover factual mismatches, untranslated/unsynced content, terminology inconsistency, style differences, expression-strength differences, information-granularity differences, and contextual differences.
- Cluster repeated issues. The same root problem appearing in multiple locations is one finding with an affected-location list, not many rows.
- Report severity and confidence as two separate dimensions. Severity is how bad it is if wrong; confidence is how sure you are that it is wrong.
- If multiple target files are provided, proofread one representative file first, output findings, and pause for user feedback before continuing with the rest. Only process all files in one pass if the user explicitly asks to do so.
- Default output is a concise table in the chat. Do not create a complex Excel report unless the user asks.

## Five-dimension issue model

Classify every finding into one of five dimensions. Each dimension has domain-neutral sub-types. When a domain preset is loaded (see Domain presets), use its sub-type names for display.

| Dimension | Meaning | Generic sub-types |
|---|---|---|
| **Accuracy** | Target conflicts with a baseline fact or hard parameter. | factual mismatch, parameter mismatch |
| **Sync** | Baseline or source has changed but target still reflects older or different content. | source not synchronized, old-version contamination |
| **Consistency** | The same concept appears with different wording or format inside the target or project. | terminology inconsistency, format inconsistency |
| **Tone** | Facts match, but expression differs in style, claim strength, or information granularity. | style difference, expression-strength difference, granularity difference |
| **Scope** | Target is outside the confirmed baseline, baselines conflict, context may justify the difference, or evidence is insufficient. | out-of-baseline-scope, baseline conflict, contextual difference, needs confirmation |

The dimension drives the judgment path. The sub-type is what the user sees in the report. A domain preset maps these generic sub-types onto domain-specific names (for packaging, see `references/domain-presets/packaging.md`).

## Intake checkpoint before proofreading

🔴 CHECKPOINT · 🛑 STOP: Do not start a real proofreading pass until the five items below are confirmed. If any item is missing, ask and wait. Do not assume a baseline to keep moving.

Before doing a real proofreading pass, confirm these five items unless they are already clear in the conversation:

1. **Baseline master**: which file/document is the source of truth.
2. **Baseline location and limits**: exact sheet/tab/page/section/row range/columns/SKU/language scope to use.
3. **Source-target relationship**: how source relates to target — translation (which language pair), same-language different version, spec vs. implementation, full draft vs. condensed copy, or other. This decides which judgment logic applies.
4. **Target content**: which uploaded or connected file(s) should be checked.
5. **Batch mode**: for multiple target files, whether to check one first and pause, or check all at once.

Use concise wording such as:

> 我会以你确认的【母本文件 + 具体位置/范围】为唯一校对依据。请确认：(1) 本轮依据是哪个文件、哪个 sheet/页面/行列/范围；(2) 源和目标是什么关系（翻译/同语言不同版本/规范 vs 实施等）；(3) 要先校对哪个目标文件。如果有多个目标文件，我会先输出一个文件的结果，等你反馈后再继续。

Skip this checkpoint only when the user has already specified the baseline, scope, and relationship clearly, for example: “以 NCE WBS 的《包装卖点文案》sheet 为依据，先校对包装封套，说明书和法律声明等我补充标准后再校对。”

## Baseline integrity check

🔴 CHECKPOINT · 🛑 STOP: Before trusting the user-named baseline, verify it actually matches the target product. A confirmed sheet name does not guarantee correct content. Run these checks and, if any fails, surface it and pause instead of proofreading mechanically.

1. **Product identity**: confirm the baseline and target refer to the same product. Match model/SKU, product name, and category. If the baseline states a different model, or describes a different product form (for example, ear-hook vs. clip-on), treat the named baseline as suspect and report it before judging the target.
2. **Cross-sheet consistency**: if the package has both a content sheet (e.g. `Product Info`) and a parameter sheet (e.g. `SPEC`), spot-check that they agree on hard facts (Bluetooth version, IP rating, runtime, charging). If they conflict, mark `基准冲突` and ask which one wins; do not silently pick one.
3. **Placeholder/unfilled cells**: if a baseline cell is a placeholder (`?`, `待确认`, `TBD`, empty), mark it `基准待确认` and do not judge the target against it.

If the named baseline fails the product-identity check but another sheet matches, say so explicitly and recommend the matching sheet as the factual baseline, then wait for the user to confirm.

## Standard workflow

1. Identify the confirmed baseline file and exact baseline location. If several possible baseline areas exist, ask the user to choose instead of silently selecting one.
2. Extract baseline copy and facts only from the confirmed location. Record location coordinates (sheet/section/page/row/column/language scope) and visible change notes when available.
3. Inspect the target file. Map its structure to a generic `section / location / unit` model, then translate that to the concrete units of the file type (see Document parsing).
4. Map target content to baseline locations. If a target item has no matching baseline within the confirmed scope, classify it as `Scope / out-of-baseline-scope` and pause for user confirmation rather than using another sheet or inventing a baseline.
5. Compare target units against the confirmed baseline, the source text (when the relationship is translation), and internal consistency within the target file.
6. Classify every finding by dimension and sub-type. Do not hide tone or scope differences merely because the facts are correct.
7. Run the judgment quality layer: cluster repeated findings, verify each finding cites baseline evidence, and assign severity and confidence.
8. If multiple target files were provided and batch-all was not explicitly requested, output the first file's findings and ask whether to continue with the next files using any corrected assumptions.

## Document parsing

Map every file type to a generic `section / location / unit` model so the workflow stays format-neutral. Use the concrete units below when reporting locations:

| File type | Location units | Parsing strategy |
|---|---|---|
| Excel workbook | sheet + row + column | Use `scripts/extract_workbook_outline.py` for a deterministic map. |
| PDF | page + area/paragraph | Use rendered pages/crops for visual location; parse text for content comparison. Prefer rendered crops when parsed text is garbled. |
| Word/DOCX | heading + paragraph | Split by heading hierarchy into sections. |
| Markdown | heading + line range | Map directly by heading hierarchy. |
| Web/HTML | section + selector | Locate by semantic block (header/hero/body/footer). |
| Plain text | line range | Locate by line number. |

The Excel helper only extracts structure; perform the actual proofreading reasoning yourself using `references/proofreading-rules.md`.

### Multi-language / matrix targets

Packaging copy is often a matrix: one row per content item, many columns for languages and versions (for example a 17-language sleeve, plus separate 简中 / 大中华 / 国际 versions). Handle it as follows:

1. **Find the source column** the user confirmed (often the earliest, e.g. `简体中文初版`). Every language column is checked against that source for synchronization, and against the baseline for facts.
2. **Read column headers as semantics**, not just language. Headers like `德语-初版-翻译公司产出` and `德语-内部校对` / `ChatGPT 4o校对` are a draft-vs-proofread pair for the same language. Compare the proofread column against both the draft and the source; flag where the proofread version still carries draft errors.
3. **Check cross-version consistency** for the same row: when 简中, 大中华, and 国际 give different category names, slogans, or claims for the same product, that is `术语不统一` or a positioning difference, not automatically an error — but report it.
4. **Do not silently rely on language keyword detection.** The heuristic tags cover only CN/EN/FR/NA. For other languages (de/it/es/pt/nl/ja/ko/...), read the header text or ask the user which column is which; never guess from a substring.
5. **Scope a matrix in passes.** If the user did not ask for all languages and versions at once, proofread one version (or one language) first, output it, and pause (see Batch-output checkpoint).

### Optional workbook helper

For Excel workbooks, use `scripts/extract_workbook_outline.py` when a deterministic workbook map is useful. It lists sheets, candidate header rows, detected Chinese/English/French/NA columns, styled/commented cells, and text rows without modifying the workbook.

```bash
python scripts/extract_workbook_outline.py input.xlsx --out workbook_outline.json --max-rows 5000
```

The language column tags it emits are heuristic hints only, not the baseline. Always defer to the user-confirmed source-target relationship from the intake checkpoint.

## Judgment quality layer

After classification and before output, run these three checks. They control the three main failure modes of AI proofreading: noise, false positives, and opaque certainty.

### Clustering

Aggregate findings by problem fingerprint. Two findings share a fingerprint when they have the same dimension, the same sub-type, and the same root cause (for example, the same term pair confused, or the same parameter value wrong). Report one finding with an affected-location list instead of one row per occurrence.

### Evidence sourcing

Every finding's evidence must quote the exact baseline fragment plus its location.

**Exception for Linguistic, Grammatical, Spelling, and Typographical Errors**:
Standard language grammar, spelling, punctuation, spacing, and typographical rules are self-evident authorities. When reporting a grammar error (e.g., subject-verb agreement, missing articles/copulas), spelling error, punctuation error (e.g., CJK punctuation in English), or spacing error (e.g., missing space after period), you do NOT need a product-specific baseline fragment to prove it. You can cite standard English grammar/typesetting rules as the authority, and mark it as a high-confidence error (`高`置信度).

If the issue is a product fact or parameter, you must quote a baseline fragment. If you cannot quote a baseline fragment that proves a product-specific issue, you may not call it an error; downgrade it to `Scope / needs confirmation`. This follows the same principle as the environment's content-integrity rule: you may offer a judgment, but you may not manufacture a standard.

### Severity and confidence

Report two independent dimensions:

- **Severity**: how bad the consequence is if the target is wrong. Values: `高 / 中 / 低 / 可接受差异`.
- **Confidence**: how sure you are that it is actually a problem. Values: `高 / 中 / 低`.

Do not collapse uncertainty into a single middle value. Assign confidence using the anchors in `references/proofreading-rules.md`; a high-severity, low-confidence finding should be surfaced for human review, not hidden or inflated.

## Failure handling

When something blocks a clean comparison, do not silently guess. Use this if-then table.

| Trigger | First-line handling | Final fallback if still blocked |
|---|---|---|
| Baseline, scope, or relationship not stated | Run the intake checkpoint and ask for the missing item | Stop; do not proofread against an assumed baseline |
| Named baseline describes a different product than the target | Run the baseline integrity check; report the mismatch | Recommend the matching sheet as baseline; wait for user confirmation |
| Baseline cell is a placeholder (`?` / `待确认` / `TBD` / empty) | Mark `基准待确认`; do not judge the target against it | Ask the user to fill or confirm the baseline value |
| Target is a multi-language / version matrix | Pick the confirmed source column; check each language/version against it in passes | Ask which columns are source vs. target when headers are ambiguous |
| Target content has no matching baseline in scope | Mark `不在本轮基准范围`, list it, pause | Ask the user for the matching baseline before judging it |
| You cannot quote a baseline fragment that proves the issue | Downgrade to `需确认` at `低` confidence | Report it as a question, never as a confirmed error |
| Two confirmed baselines conflict | Mark `基准冲突`, show both fragments | Ask the user which baseline wins before correcting |
| Target file unreadable or garbled (PDF/image) | Use rendered pages/crops instead of parsed text | Report which areas could not be read; do not invent content |
| Excel helper script errors | Read the workbook directly without the script | Report the sheets/rows you could not map deterministically |
| Multiple target files uploaded | Proofread the first file, then stop for feedback | Do not batch-all unless the user explicitly asked |
| No differences found | State which baseline location and target areas were checked | Do not fabricate findings to look thorough |

## Domain presets

When the user's scenario clearly belongs to a known domain, load the matching preset as a judgment supplement on top of the five-dimension model:

- Packaging / physical product copy: `references/domain-presets/packaging.md`.

If no preset matches the scenario, use only the generic five-dimension model and generic sub-types. Do not force domain-specific sub-types (such as packaging parameter checks) onto unrelated content.

## Issue sub-type reference

Bilingual display labels for the sub-types defined in the five-dimension table above. `references/proofreading-rules.md` is the single source of truth for what each one means; this list only fixes the wording shown in reports.

- `产品事实不一致` / factual mismatch
- `参数不一致` / parameter mismatch
- `源文案未同步` / source not synchronized
- `术语不统一` / terminology inconsistency
- `格式不统一` / format inconsistency
- `风格差异` / style difference
- `表达强度差异` / expression-strength difference
- `信息颗粒度差异` / granularity difference
- `语境差异` / contextual difference
- `基准冲突` / baseline conflict
- `不在本轮基准范围` / out-of-baseline-scope
- `需确认` / needs confirmation

## Severity

- `高`: factual, parameter, safety, compliance, URL, SKU/model, SN, packaging-list, legal, or strong-claim risk that should be corrected before production.
- `中`: unsynced language, terminology inconsistency, likely old-version contamination, meaningful omission/addition, or target content outside scope that needs a new baseline.
- `低`: factually correct style, tone, expression-strength, or information-granularity difference that needs attention but may be acceptable.
- `可接受差异`: context likely justifies the wording, but the difference should still be recorded for alignment.

## Confidence

- `高`: an exact baseline fragment directly proves the issue, and there is no plausible context that justifies the target wording.
- `中`: the baseline supports the issue, but some context, version ambiguity, or translation convention could still explain the target.
- `低`: the issue is suspected from internal patterns or weak signals, but no baseline fragment directly proves it. Pair this with `需确认` unless evidence improves.

## Chat output contract

Default to this table:

| 文件 | 位置 | 原文 | 建议/处理 | 维度 | 子类型 | 严重程度 | 置信度 | 依据 |
|---|---|---|---|---|---|---|---|---|

Guidelines:

- Keep each row traceable to the target file, the target location, and the baseline location it was checked against.
- For clustered findings, put the representative wording in `原文` and list all affected locations in `位置` (for example, `包装正面 row7 / 说明书 p3 / app 卡 row12，共 8 处`).
- Quote only the key original fragment needed to understand the issue.
- `依据` must quote the baseline fragment plus its location. If you cannot, set 子类型 to `需确认` and 置信度 to `低`.
- For factual errors, write `应改为...` or `建议同步为...`.
- For terminology issues, write `建议统一为...`; if no official term exists, say it is a consistency suggestion, not a final official translation.
- For tone or contextual differences, do not call them errors. Say `事实一致，但...，建议确认是否接受/是否统一`.
- If a target item is outside the confirmed baseline scope, write `本轮先暂停，需补充/确认对应母本位置`.
- If a baseline conflict exists, say `需先确认基准` and do not force a correction.
- If no differences are found, say so and state which baseline location and target file/areas were checked.

After the table, add a compact summary that counts findings by severity, lists `不在本轮基准范围` items, and states the next step for remaining files.

## Batch-output checkpoint

🔴 CHECKPOINT · 🛑 STOP: With multiple target files, output the first file only, then stop and wait for user feedback. Do not proofread the remaining files in the same turn unless the user explicitly asked for batch-all.

When several target files are uploaded:

1. Select the first relevant target file or the file the user named first.
2. Output only that file's proofreading table plus a short summary.
3. Add a brief checkpoint: `我先按上述判断校对了这个文件。请确认这些处理方式是否符合预期；确认后我再继续校对其余文件。`
4. Continue to more files only after the user confirms, corrects the baseline, or asks to proceed.

## Anti-patterns: do not do these

🔴 These are the failure modes that make this skill untrustworthy. Check against this list before sending any report.

- Do not edit, overwrite, or save into a source document. This skill is read-only.
- Do not assume a baseline (`Product Info`, `SPEC`, a "main" sheet) to avoid asking. An assumed baseline poisons every finding.
- Do not judge content that falls outside the confirmed scope. Mark `不在本轮基准范围` and pause instead.
- Do not call something an error when you cannot quote the baseline fragment that proves it. Downgrade to `需确认` (except for self-evident linguistic, grammatical, spelling, and typographical errors).
- Do not ignore micro-level text quality such as English grammar, spelling, punctuation, spacing, and capitalization consistency.
- Do not present your own translation as the official term. Without a glossary, it is a consistency suggestion only.
- Do not mark every finding `中` confidence to dodge a judgment. Use the high/medium/low anchors.
- Do not emit one row per occurrence of the same root problem. Cluster into one finding with an affected-location list.
- Do not collapse severity and confidence into one column. They are independent.
- Do not batch-proofread all uploaded files in one turn unless the user explicitly asked.
- Do not force packaging sub-types or parameter checks onto non-packaging content. Use the generic model when no preset matches.
- Do not fabricate findings to look thorough. "No differences found" is a valid result.

## Detailed rules

Read `references/proofreading-rules.md` when performing a real proofreading task. Read `references/report-template.md` when examples of final table wording are useful. Read `references/domain-presets/packaging.md` when the task is packaging or physical-product copy.
