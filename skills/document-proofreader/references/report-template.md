# Report Template

## Default chat table

| 文件 | 位置 | 原文 | 建议/处理 | 维度 | 子类型 | 严重程度 | 置信度 | 依据 |
|---|---|---|---|---|---|---|---|---|
| S610 包装封套 BK | 包装卖点文案 / Row 7 / 英文终版列 | Up to 10 Hours of Listening Time, and Quick Charge | 建议删除逗号，统一为 `Up to 10 Hours of Listening Time and Quick Charge`。 | Sync | 源文案未同步 | 中 | 高 | 母本《包装卖点文案》Row 7 终版英文为 `Up to 10 Hours of Listening Time and Quick Charge`（无逗号）。 |
| Settings.strings (zh→de 本地化) | key `battery_full` / Line 142 | „100% geladen in 2 Stunden“ | 源已改为 90 分钟，建议同步为 „90 Minuten“。 | Accuracy | 参数不一致 | 高 | 高 | 源文件 `battery_full` 当前值为「90 分钟充满」，德文仍为 2 小时。 |
| 用户协议 EN 版 | Section 8.2 / Para 1 | the Company may terminate at any time without notice | 母本中文为「提前 30 日通知后可终止」，英文遗漏通知期，建议补回。 | Accuracy | 产品事实不一致 | 高 | 中 | 母本《服务条款》第 8.2 条：「本公司提前三十日通知后可终止」。英文是否为法务确认终版需确认。 |
| S610 包装封套 BK | 正面 row7 / 说明书 p3 / app 卡 row12（共 8 处） | earbuds / earphones 混用 | 同一部件多处译法不一致；无官方译法时，建议统一为一种并确认。 | Consistency | 术语不统一 | 中 | 中 | 母本未指定官方译法；判定基于目标文件内部多译并存。 |
| S611 Mini 包装封套 BK | 正面 Mini 说明（母本无对应位置） | Mini version / shorter band copy | 本轮先暂停，需补充 Mini 版本对应母本位置后再判断。 | Scope | 不在本轮基准范围 | 中 | 高 | 用户确认的母本位置未包含 Mini 版本专属文案。 |
| 外包装标题 | 品类词区 / Row 2 | BONE CONDUCTION SPORTS HEADPHONES | 与母本 `Bone Conduction Sports Headphones` 仅大小写不同；若为包装视觉规范全大写，可接受。 | Scope | 语境差异 | 可接受差异 | 中 | 母本 Row 2 写作 `Bone Conduction Sports Headphones`；包装标题全大写通常为版式处理。 |

Notes on this table:

- The first three rows show different domains (packaging, software localization, legal) to demonstrate that the same nine columns work across scenarios.
- The fourth row shows a clustered finding: one row with all affected locations in `位置`, not eight separate rows.
- `依据` always quotes the baseline fragment and its location. When evidence is incomplete, the finding is marked with lower confidence or `需确认`.

## Intake confirmation wording

When the baseline is unclear, ask briefly before proofreading:

> 请先确认：(1) 本轮校对依据母本是哪个文件、哪个 sheet/页面/行列/范围；(2) 源和目标是什么关系（翻译/同语言不同版本/规范 vs 实施等）；(3) 要校对哪个目标文件。若有多个目标文件，我会先校对一个并输出结果，等你反馈处理方式后再继续其余文件。

When the baseline is already clear, acknowledge and proceed:

> 已确认：本轮以【文件 + 具体位置】为母本，源-目标关系为【关系】，只校对【目标范围】。其他不在母本范围内的内容我会先暂停，等你补充标准后再校。

## Short summary format

After the table, add a compact summary:

- `高`：x 条，建议优先修正。
- `中`：x 条，建议确认或统一。
- `低/可接受差异`：x 条，主要用于人工风格判断。
- `不在本轮基准范围`：x 条，已暂停，等待补充对应母本。
- `低置信度`：x 条，建议人工复核（证据不足以直接判错）。
- `下一步`：如果有多个文件，说明已先完成哪个文件，并等待用户确认后继续其余文件。

Do not add long explanations unless the user asks.
