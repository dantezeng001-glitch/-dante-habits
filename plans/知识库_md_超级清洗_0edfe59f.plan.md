---
name: 知识库 MD 超级清洗
overview: 按 md-cleanup skill 的强制两段式流程（脚本段 F1/F2/F3/F4/F6 + AI 段 F5 语义重排），对同步文档、技术、产品、竞品、脚本 5 个文件夹下全部 MD 做一次彻底清洗，并补一轮跨文件夹的扫读友好度自检与审计日志。
todos:
  - id: t0
    content: Phase 0：读 md_cleanup.py 源码确认脚本能力；新建 cleanup_audit_2026-04-22.md 底稿
    status: completed
  - id: t1
    content: Phase 1：对 同步文档 / 技术 / 产品 / 竞品 / 脚本 5 批分别跑 md_cleanup.py --in-place，收集 Changed/OK 清单
    status: completed
  - id: t2
    content: Phase 2：对全部 ~86 个 MD 跑 skill 的扫读友好度 4 问自检，输出 F5 待重排清单
    status: completed
  - id: t3
    content: Phase 3-A：PPT 抽取 MD（~4 个）做 Slide 标题语义化、去重复首行、bullet 分组重排
    status: completed
  - id: t4
    content: Phase 3-B：Excel 抽取 MD（~11 个 FABE+科技树 Sheet）裁末尾空行、重排 Notes Before Header
    status: completed
  - id: t5
    content: Phase 3-C：BOS 月银白钉钉导出做 F3 残余清理（++_**..**_++、emoji 标签、空缩进行）
    status: completed
  - id: t6
    content: Phase 3-D/E/F：PDF/DOCX/手写 MD 按扫读自检结果决定是否 F5，默认不动
    status: completed
  - id: t7
    content: Phase 4：完成 cleanup_audit_2026-04-22.md 审计日志；附后续建议（stale 清理、命名违规、file-sync 覆盖风险）
    status: completed
isProject: false
---

## 范围盘点

实际待清洗 MD 总数（已核对，stale / _tmp_sync 目录均为空壳）：

- `同步文档/`：24 个（PPT/Excel/PDF/DOCX 抽取产物 + 2 个 index/README）
- `技术/`：41 个（含至少 1 个 PPT 抽取脏样本 `NT-开放式技术学习/OpenFit_Pro_技术解析.md`）
- `产品/`：9 个（含典型钉钉导出脏样本 `BOS/BOS  月银白 新色上市计划书 (1).md`）
- `竞品/`：10 个（手写为主，抽样看多数干净）
- `脚本/`：2 个 MD（`README.md`、`lint_kb_prompt.md`，手写；`.py` 不在清洗对象内）

**合计约 86 个 MD。** stale 目录为空壳不处理。

## 发现的脏样本家族（决定 F5 是否触发）

- **A 类：PPT 抽取**（命中 F5.2 / F5.3） — 同步文档下 `【NT技术卖点培训】-OpenFit_Pro-0211/document.md`、`北美2025年战略启动会250513/document.md`、`科技树思路梳理——加工中/document.md`；以及 [知识库/技术/NT-开放式技术学习/OpenFit_Pro_技术解析.md](知识库/技术/NT-开放式技术学习/OpenFit_Pro_技术解析.md)。症状：`## Slide N: XXX` 机械标题、slide 标题在正文首行重复、`● 第X章` 目录符号、全 `-` bullets、中英文句号混用为逗号。
- **B 类：Excel 抽取**（命中 F5.6 延伸 + 新规则"末尾幽灵空行"） — `同步文档/*FABE*/*.md`（NCE 从第 26 行起 ~80 行 `| | | ... |` 幽灵行，XS 类似）、`同步文档/韶音科技树总览（可传播，持续更新）(2)_82cf51f8/*.md` 10 张。症状：表格末尾几十行全空行、`## Notes Before Header` 挤成一段看不清、列头英文副标题用 `<br>` 挤在一起。
- **C 类：钉钉/飞书富文本导出**（命中 F3.1 / F4 + 新规则"下划线嵌套粗斜体") — [知识库/产品/BOS/BOS  月银白 新色上市计划书 (1).md](知识库/产品/BOS/BOS  月银白 新色上市计划书 (1).md)。症状：`$\color{#0089FF}{@...}$`、`请至钉钉文档查看附件《...》`、`[时间] [灯泡] [文档]` emoji 标签被抽成文本、`++_**...**_++` 飞书下划线+粗+斜体组合、每个 `*` bullet 下空缩进行。
- **D 类：PDF 抽取** — `OpenSound_Pro_技术平台手册/document.md`、`骨导耳机发展/document.md`。这两个同步文档目录里已经生成了 `cleaned.md`，说明之前跑过 file-sync 的清洗链路，本轮以 `cleaned.md` 为准，`document.md` 只做轻量脚本段。
- **E 类：DOCX 抽取** — 华为折叠屏、骨传导耳机先天弊端。抽样看已较干净，多半只需脚本段。
- **F 类：手写 MD** — `竞品/` 全部、`技术/骨传导声学/` 大部分、`产品/README.md`、`脚本/*.md`。脚本段应全部幂等 `OK`；F5 按触发条件判断，**不触发就不改动**（skill 硬约束）。

## Phase 0｜前置

- 读 [C:\Users\016551cursor\skills\md-cleanup\scripts\md_cleanup.py](C:\Users\016551.cursor\skills\md-cleanup\scripts\md_cleanup.py) 确认脚本参数与现有正则范围。
- 新增 `knowledge-base-cleanup-YYYY-MM-DD` 文件夹下的 [知识库/脚本/cleanup_audit_2026-04-22.md](知识库/脚本/cleanup_audit_2026-04-22.md) 作为审计日志底稿（记录每个文件：是否改动 / 触发哪些家族 / 改动摘要）。

## Phase 1｜脚本段（F1 / F2 / F3.1–F3.3 / F4 / F6，自动）

对 5 个文件夹分 5 批跑：

```powershell
python "C:\Users\016551\.cursor\skills\md-cleanup\scripts\md_cleanup.py" `
  "C:\Users\016551\OneDrive\Desktop\科技树\知识库\同步文档\**\*.md" --in-place
```

其余 4 个文件夹同理，`技术`、`产品`、`竞品`、`脚本`。收集脚本输出，把 `Changed` 与 `OK` 的文件名分列抄到审计日志。

**风险控制**：脚本段对"本来就干净"的文件是幂等的（报 `OK` 不改内容）。但 NFKC 会把全角半角英文标点归一化——竞品/的几篇手写文档如果作者刻意保留某种风格，需要脚本跑完扫读验收。

## Phase 2｜交付前扫读友好度自检（强制）

脚本段跑完后，**所有文件**用 skill 的 4 题自检过一遍：

1. 有 3+ 个 `### 第 N 行` / `## Slide N` 机械标题？（A / B 类必命中）
2. MD 表格行跨多个物理行？（B 类 FABE 文件有可能）
3. 行数 ÷ 原始数据行数 > 3？（Excel 抽取红灯）
4. 正文 90%+ 是 `-`  或全是 `#`？（A 类 PPT 抽取必命中）

输出"需要 F5 重排的文件清单"（预计 14–18 个）和"只跑脚本段即可交付的文件清单"。

## Phase 3｜F5 语义重排（按家族分批，人工/AI 手动）

只对 Phase 2 命中的文件动，且**不编造原文没有的内容**：

- **A 类 PPT**（约 4 个）：`## Slide N: XXX` → 用 slide 实际主题重写语义标题（必要时合并相邻同主题 slide）；slide 标题在首行 bullet 重复的删 bullet 保标题；`● 第X章` 改 `##`；扁平 `-` 列表按逻辑分组做 H3 + 嵌套 bullet。
- **B 类 Excel**（约 11 个）：裁末尾全空表格行、`## Notes Before Header` 重排为正常段落或小表；超宽列头 `中文<br>English` 检查是否需要保留英文。
- **C 类 钉钉**（1 个 BOS 计划书）：脚本段处理后再手工把 `++_**...**_++` 改 `**粗体`**；`[时间] [灯泡] [文档]` 这类 emoji 标签改成正常段落小标题；bullet 之间空缩进行压掉。
- **D 类 PDF**：`document.md` 不触碰结构（保留 file-sync 原样），仅脚本段；`cleaned.md` 做 F5 判断，有必要才重排。
- **E/F 类**：正常情况脚本段后不再需要 F5。若有意外脏点记录到审计日志"待人工复查"段。

**F5 边界硬约束**（复述 skill）：不合并看似重复的章节；不删"看起来空"的列除非全表扫完确认；不编数字/结论。

## Phase 4｜审计日志与交付

- 把每个文件改动摘要写进 [知识库/脚本/cleanup_audit_2026-04-22.md](知识库/脚本/cleanup_audit_2026-04-22.md)：文件路径 / 脚本段是否 Changed / F5 家族 / F5 动作摘要 / 数据完整性自查结论。
- 报告里单列"可选后续"：建议 purge `同步文档/*__stale_`* 空目录、提醒 file-sync 下次跑会重建 `document.md` 覆盖清洗（即 A / B 类的 F5 修改不持久，最好把成果反哺到非同步目录或写回源文件）。
- 附一句：`产品/BOS/BOS  月银白 新色上市计划书 (1).md` 文件名命中 `lint_kb_prompt` 的"命名违规"（两个空格 + `(1)` 尾缀），本轮只整理内容，文件名重命名需要单独确认。

## 不改范围（硬边界）

- `脚本/*.py`：Python 源码不在 md-cleanup 范围，不动。
- `同步文档/*/manifest.json`、`document.json`：file-sync 元数据，不动。
- `同步文档/*__stale_`* / `_tmp_sync_*`：空目录，不动。
- 不会覆盖现成的 `cleaned.md`（file-sync 链路产物）。

