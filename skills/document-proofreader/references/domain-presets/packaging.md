# Domain Preset: Packaging and Physical-Product Copy

Load this preset when the task is packaging, instruction manuals, stickers, material copy, or GTM workbooks for physical products. It supplements the generic five-dimension model in `../proofreading-rules.md` with packaging-specific baselines, sub-types, and checks. The generic model still governs; this preset only adds domain detail.

## Typical baselines in this domain

- `Product Info` sheet: core factual baseline when the user confirms it (product name, category, features, selling points, technical explanations, usage conditions, packaging list, URLs, QR/SN info, safety limitations, change notes). Do not assume it is the baseline; the user must confirm it.
- `SPEC` sheet: auxiliary hard-parameter source only, when confirmed. Hard parameters include battery life, call time, music time, charging time, quick charge benefit, weight, dimensions, battery capacity, Bluetooth version, codec, frequency response, sensitivity, wireless range, and IP rating.
- Do not use Product Message House, FABE, GTM, or Marketing Claim sheets as baseline unless the user explicitly promotes them.

If `Product Info` and `SPEC` conflict, record `基准冲突` instead of deciding silently.

### Product Info vs SPEC reconciliation (run first)

In real GTM packages, the `Product Info` sheet is sometimes carried over from a previous product and not fully updated, while `SPEC` is regenerated per product. Before using `Product Info` as the factual baseline:

- Confirm `Product Info` and `SPEC` agree on the product identity (model/SKU, category, product form). The target packaging usually states the model (e.g. `SHOKZ E310`) and category — match it.
- Spot-check hard facts that frequently drift: Bluetooth version, IP rating, runtime (single vs. with-case), charging time, weight, wireless charging support, codec/Dolby support.
- If `Product Info` describes a different form (ear-hook vs. clip-on) or different parameters than `SPEC` and the target, treat `SPEC` (which matches the target model) as the factual baseline for parameters, mark the `Product Info` mismatch as `基准冲突` / `基准待确认`, and ask the user to confirm before proceeding.
- Watch for unverified strong claims that the package adds but no baseline supports (e.g. a 杜比/Dolby claim when `SPEC` codecs list only AAC/SBC). Mark `需确认`, do not pass it as confirmed.

## Domain sub-type mapping

The generic sub-types map onto these packaging labels for display:

| Dimension | Generic sub-type | Packaging label |
|---|---|---|
| Accuracy | factual mismatch | 产品事实不一致 |
| Accuracy | parameter mismatch | 参数不一致 |
| Sync | source not synchronized | 中文未同步 / 源文案未同步 |
| Consistency | terminology inconsistency | 术语不统一 |
| Tone | style difference | 风格差异 |
| Tone | expression-strength difference | 表达强度差异 |
| Tone | granularity difference | 信息颗粒度差异 |
| Scope | contextual difference | 语境差异 |
| Scope | baseline conflict | 基准冲突 |
| Scope | out-of-baseline-scope | 不在本轮基准范围 |

## Packaging-specific parameter checks

Report Accuracy / parameter mismatch when hard values, units, ranges, conditions, or subjects differ from confirmed Product Info or SPEC. Watch:

- Battery/runtime: `25 hours` vs `27 hours`, with-case vs without-case totals.
- Protection: `IP54` vs `fully waterproof` or `waterproof`.
- Charging: charge time, quick-charge benefit phrasing.
- Weight: per-earbud vs total vs with-case.
- Connectivity: Bluetooth version, codec, wireless range.

## Packaging-specific scope-gating

Pause with `不在本轮基准范围` when the confirmed baseline does not cover the target content. Common packaging cases:

- Baseline is a selling-point sheet, but target contains legal statements, safety warnings, importer addresses, warranty terms, certification marks, or bottom-sticker text.
- Baseline covers a regular product, but target contains Mini, special color, regional SKU, bundle, or accessory-specific wording.
- Baseline covers one panel/area, but target has side/back/bottom-panel copy not listed there.

## Packaging-specific terminology watchlist

Common inconsistency triggers in this domain: product-name capitalization, app name, technology names, acoustic feature names, `earbuds` vs `earphones` vs `headphones`, `charging case` vs `charger` vs `case`, and action names such as tap/press/hold. When context (front panel vs. manual) may justify different terms, use `语境差异` or `术语不统一，需确认`, not a confirmed error.

## Packaging-specific strong-claim watchlist

Treat as Tone / expression-strength difference at higher attention: `fully`, `ultimate`, `best`, `guaranteed`, `always`, `never`, `perfect`, `waterproof`. On packaging these can become compliance risk, so when a strong claim exceeds what Product Info or SPEC supports, escalate severity toward `高` and cite the baseline fragment that limits the claim.
