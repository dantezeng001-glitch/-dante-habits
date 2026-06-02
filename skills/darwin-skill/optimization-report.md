# Darwin 批量优化报告（2026-04-23）

运行模式：`dry_run`（无子 agent 双跑，逐项结构+推演评估）
日志：[results.tsv](results.tsv) · 基线排序：[baseline-ranking.md](baseline-ranking.md)
未创建 git 分支：`.codex` 与工作区均非 git 仓库；`.cursor` 是 git 仓库但本轮未被要求提交，统一走时间戳日志做回滚面。

## 总览

- 优化资产：`21`（15 skills + 6 rules）
- 保留改进：`21`（全部 keep，含 2 项经二轮补丁从 revert 修回）
- 回滚次数：`0`（最终口径）
- 平均分：`78.6 → 85.4`，Δ `+6.8`

## 分数变化（按 delta 从大到小）

| Asset | Type | Before | After | Δ | 改进维度 |
|---|---|---:|---:|---:|---|
| `pua-motivator` | skill | 59.7 | 74.7 | +15.0 | 3 边界条件覆盖 |
| `no-redundant-writing` | rule | 69.9 | 85.3 | +15.4 | 2 工作流清晰度 |
| `writing-quality` | rule | 68.9 | 83.7 | +14.8 | 2 工作流清晰度 |
| `update-cursor-settings` | skill | 67.2 | 81.3 | +14.1 | 4 检查点设计 |
| `create-subagent` | skill | 70.9 | 82.3 | +11.4 | 4 检查点设计 |
| `ai-product-manager` | skill | 79.8 | 88.6 | +8.8 | 3 边界条件覆盖 |
| `content-integrity` | rule | 80.6 | 89.1 | +8.5 | 4 检查点设计 |
| `file-sync` | skill | 79.1 | 87.1 | +8.0 | 6 资源整合度 |
| `md-cleanup` | skill | 84.4 | 92.3 | +7.9 | 4 检查点设计 |
| `create-rule` | skill | 76.6 | 82.1 | +5.5 | 3 边界条件覆盖 |
| `openai-docs` | skill | 84.7 | 90.1 | +5.4 | 6 资源整合度 |
| `darwin-skill` | skill | 88.7 | 93.0 | +4.3 | 6 资源整合度 |
| `content-integrity-guard` | skill | 82.4 | 86.6 | +4.2 | 4 检查点设计 |
| `create-skill` | skill | 83.1 | 87.3 | +4.2 | 4 检查点设计 |
| `ai-coding-discipline` | rule | 88.0 | 91.8 | +3.8 | 2 工作流清晰度 |
| `plugin-creator` | skill | 78.7 | 81.3 | +2.6 | 5 指令具体性 |
| `rule-file-sync` | rule | 78.3 | 80.5 | +2.2 | 7 整体架构 |
| `work-in-layers` | rule | 88.6 | 89.2 | +0.6 | 3 边界条件覆盖 |
| `migrate-to-skills` | skill | 81.7 | 82.2 | +0.5 | 5 指令具体性 |
| `skill-creator` | skill | 85.8 | 86.0 | +0.2 | 6 资源整合度 |
| `skill-installer` | skill | 79.9 | 80.0 | +0.1 | 3 边界条件覆盖 |

## 每资产改动摘要

### Skills

- `darwin-skill`：把目标从「只优化 skills」扩展成「skill + rule 两类 prompt 资产」；`results.tsv` 位置从 `.claude/...` 修正到当前技能目录；约束规则补「未要求 commit 时不创建 commit」。
- `ai-product-manager`：在「应对模糊回答」后加边界与分流矩阵，覆盖用户要直接初稿、未识别品牌、多品牌、仅要工具、信息过少这 5 种分流。
- `content-integrity-guard`：Remediate 环节加多文件硬停点（tier 分布 + top 3 改动 + 未决问题），区分「只审计」和「允许改文」两种授权。
- `file-sync`：新增 Resource Map（统一 `document_sync.py` / `excel_sync.py` / `FILE_SYNC_README.md` 的真源）+ Preflight 三项确认；`Subagent` 命名同步。
- `md-cleanup`：F5 硬约束里新增「多个合理重组方案先停一下」，让语义级重排不会替用户做不可逆的结构选择。
- `pua-motivator`：frontmatter 改成默认 neutral-owner、PUA 话术是升级层；正文补启用边界（连续失败 + 用户明确要求）与禁用场景（敏感沟通、正式文案、高共情任务）。
- `create-rule`：补 Edge Cases（已有规则冲突、`alwaysApply` vs `globs`、命名冲突、矛盾规则）；统一篇幅指标（≤150 行为正常上限）。
- `create-skill`：Discovery 后显式加 Confirmation Gate（location / trigger / deliverable / resources 四项）。
- `create-subagent`：Step 1 补四项锁定（scope / trigger / output contract / name collision）+ Troubleshooting 补 Name Collision 分支。
- `migrate-to-skills`：Locations 表补 Destination 列；工作流里把删除原文件改成「先确认再删」；`Task` 命名换成 `Subagent`。
- `update-cursor-settings`：写前先判 user/workspace scope；Step 1 改成按 OS 解析路径；Workflow 6 步结构。
- `openai-docs`：MCP 自动安装前先征求用户授权；fallback 浏览前也加确认。
- `plugin-creator`：正文开头新增 Preflight 四项（parent dir / marketplace / optional folders / overwrite intent）。
- `skill-creator`：Step 2 规划结束后补「资源计划确认」检查点，再进入 `init_skill.py`。
- `skill-installer`：联网/提权脚本前加 Approval Gate；public/private repo 分叉说明。

### Rules

- `writing-quality`：frontmatter 补完整触发词；新增 5 步精修执行顺序，强调先删填充词再改具体再补基准最后控版式。
- `no-redundant-writing`：frontmatter 补触发词；新增 4 步去重顺序与跟 `writing-quality` 的分工说明。
- `content-integrity`：在 Dimension 3 后新增 Hard Stop 段，强制对 `>=2` 文件冲突与无出处权威表述先产 3 项冲突摘要。
- `work-in-layers`：description 前置触发词；「直接做」跳过条件补「不覆盖 ai-coding-discipline 对多文件/接口/数据结构的方案确认门槛」。
- `ai-coding-discipline`：四层控制后新增「统一执行模板」6 步，把认知/复杂度/变更/验证四层变成可照着走的线性动作。
- 工作区 `file-sync.mdc`：改写成 Knowledge → Run-domain trace → Raw sync 三层入口优先级，明确每层的使用边界与新鲜度比较。

## 跨资产回归检查

| 组合 | 结论 | 主要说明 |
|---|---|---|
| `file-sync` + `md-cleanup` | ok | 边界更清楚；残留风险是 F5/Excel 指标在两侧重复，可后续收敛到 canonical 文档。 |
| `content-integrity` + `writing-quality` + `no-redundant-writing` | ok | 三者分工已分层：真实性 → 去重 → 精修；建议在 `content-integrity` 里补一句显式指向。 |
| `work-in-layers` + `ai-coding-discipline` + `pua-motivator` | warn→ok | 本轮已在 `work-in-layers` 里写明「直接做跳过条件不覆盖代码任务的方案门槛」；`pua-motivator` 默认 neutral 后，三者不再打架。 |
| 工作区 `file-sync.mdc` + 工作区 `知识库/运行域/同步文档/` | warn→ok | 本轮规则改写为三层入口优先级；知识层优先分析、运行域追溯抽取、原始层仅用于校验。 |

## 仍建议人工复核的点

- `migrate-to-skills` 仍然依赖外部 subagent 命名一致性；如果后续 Cursor 再改工具名，需要同步更新。
- `rule-file-sync` 和工作区 `同步文档/README.md` 最好再比对一次措辞，确认两处都认同新的三层分工。
- `darwin-skill` 自身建议在下一次真跑 `full_test` 时补 `results.tsv` 的 full_test 行，替换本轮的 dry_run 基线。

## 回滚面

- 所有资产都在 `.cursor` / `.codex` / 工作区磁盘上直接修改，未创建 git 分支或 commit。
- 如需回滚，可按 [results.tsv](results.tsv) 中的 `target_path` 精确定位文件，并参照本报告里的「每资产改动摘要」逆向还原关键段落。
- 如果之后要走 git 路线：`C:\Users\016551\.cursor` 目录本身是 git 仓库，可以从这一层 `git diff` 查看本轮所有改动；`.codex` 与工作区则没有仓库，只能基于本报告做人工对照。
