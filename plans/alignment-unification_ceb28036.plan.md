---
name: alignment-unification
overview: 把三个子工作（翻译对齐、PMKT术语库、DM&KOL术语库）收成一个概念池：一套记录契约、一份数据、一份总表产出；迁移时先出冲突清单人工裁定。方法论抽象成领域无关文档，为 mkt copilot 留机器可读契约入口。
todos:
  - id: schema
    content: 定义统一记录契约 record.schema.json（稳定 id / kind[产品表述|业务术语] / zh 锚点 / repr 白名单字典 / explain / provenance / category），无 domain 字段
    status: completed
  - id: dump-migrate
    content: 写一次性迁移脚本，直接 import 三处源数据结构（knowledge_base.json + 两个 py 的硬编码 dict）dump 成统一记录，禁止手抄
    status: pending
  - id: reconcile
    content: 聚合重复概念（IMC/KSP/Slogan/品类词等），产出冲突清单交人工裁定，裁定后合并成单一概念池 data/concepts.json
    status: completed
  - id: engine
    content: 写生成器 engine/generate.py（concepts.json → 一个工作簿两个 sheet，按 kind 分：产品表述 sheet 用 ZH/EN/FR/来源，业务术语 sheet 用 缩写/中文/英文/释义/场景/状态），并入改造后的 validate/extract
    status: completed
  - id: verify-migration
    content: 回放生成器，按概念条数与抽样内容比对，确保迁移无丢失无篡改
    status: pending
  - id: methodology
    content: 写 METHODOLOGY.md：align 方法论分层（核心三步对齐/解释/溯源必备 + 可选三步采集/抽取/机器校验，有源语料才上）
    status: completed
  - id: agent-entry
    content: 写 AGENT.md + record.schema.json，写明 copilot 核心用例（给一段文案 lookup+match 标出未对齐术语），预留接口签名仅描述
    status: completed
  - id: strip-sync
    content: 剥离 cursor_excel/excel_sync 同步链路（同步的是 WBS/GTM 项目表，与对齐无关）
    status: completed
isProject: false
---

# Alignment 体系归一化

## 目标

三个子工作不是三个领域，是**同一批概念的三个侧面**。收成**一个概念池 + 一份总表**：B/C 的硬编码数据迁出 Python，重复概念人工裁定后合并。方法论抽象成领域无关文档，为 copilot 留机器可读契约入口。剥离与对齐无关的 cursor_excel 同步链路。

本期不做分人群视图产出（翻译表/术语表分开渲染），留作后续开发功能。

## 统一记录契约（概念中心，无 domain）

一个概念携带多个侧面，侧面可空，`kind` 标性质：

```json
{
  "id": "ksp",                         // 稳定主键（slug/hash），不用 zh 当键
  "kind": "业务术语",                   // 产品表述 | 业务术语，决定列填法与分 sheet
  "zh": "核心卖点",                     // 锚点字段
  "category": "产品信息相关",
  "repr": { "abbr": "KSP", "en": "Key Selling Point", "fr": "—" },  // 对照轴，key 走白名单
  "explain": { "def": "产品最重要的差异化卖点…", "usage": "POP卖点贴…" },  // 解释，可空
  "provenance": { "source": "OpenRun MEET / …", "status": "confirmed" }  // 溯源+状态，可空
}
```

两类内容是同一 schema 的两种填法：

- `kind=产品表述`（≈A）= `repr` 装语言(en/fr) + `provenance` 满 + `explain` 空；对齐轴是语言。
- `kind=业务术语`（≈B+C）= `repr` 装形态(abbr/en) + `explain` 满 + `provenance` 弱（原"待@人确认"收进 `status: awaiting`）；对齐轴是形态+含义。
- 少数桥接概念（如品类词、Slogan）两侧面都填在**同一条记录**上。

`kind` 与已删的 `domain` 不同：`domain` 是"来自哪个文件"，`kind` 是"概念性质"——镭雕无论在哪都是业务术语，骨传导都是产品表述。列填法、分组、后续视图都由 `kind` 驱动。

设计要点（来自复盘的硬伤修正）：

- **主键用稳定 `id`，不用 `zh`**：A 有大量纯中文/同名多条，zh 做键会撞。
- `**repr` key 走白名单**（`en/fr/abbr/en_full/...`），开放但可校验，防 `en`→`eng` 拼错不报错。

## 目标目录结构

```
alignment/
  schema/record.schema.json   # 统一记录契约（copilot 也读这个）
  data/concepts.json          # 唯一概念池
  data/conflicts.md           # 迁移期冲突清单（人工裁定用，裁定后清空）
  engine/generate.py          # 生成器：concepts.json → 一份总表 Excel
  engine/migrate.py           # 一次性迁移脚本（import 三处源 dump）
  dist/                       # 产出物
  METHODOLOGY.md              # align 方法论（领域无关）
  AGENT.md                    # 给 copilot 的能力说明 + 契约入口
```

现有 `脚本/check_consistency.py`、`auto_extract.py`、`fix_no_source.py` 改造后并入 `engine/`（有源语料的概念可机器校验溯源，其余走 status 标注）。

## 数据迁移（脚本 dump，不手抄）

三处源直接读结构，避免手抄 600+ 条出错：

- A：`数据/knowledge_base.json` 9 个数组 → 记录，`{en,fr}` 进 `repr`，`source` 进 `provenance`。
- B：`专有名词解释库/generate_glossary.py` 的 `data` dict（5 大类）→ 记录，`(术语,中文,英文,释义,场景)` 映射到 `repr.abbr/zh/repr.en/explain.def/explain.usage`。
- C：`generate_dm_kol_glossary.py` 的 `SHEETS`（19 小类，含 `__SUB__`）→ 记录，小类落 `category`。

## 冲突裁定（先出清单，不自动合并）

真正重复几乎都在**业务术语内部**（B、C 都收了 GTM/IMC/KSP/Slogan 等）；产品表述（A）与业务术语基本不相交，少有冲突。迁移后按 `zh`/语义聚合，把**同一概念出现多次且 `repr`/`explain` 不一致**的项写进 `data/conflicts.md`（如 IMC 在 B、C 两版释义）。交你逐条裁定标准版本后，才合并成单条记录。这步是本次归一最有价值的产出——一次性消除跨库说法打架。

## 总表产出（一个工作簿，两个 sheet 按 kind 分）

`generate.py` 渲染**一份 Excel、两个 sheet**，列各自对得上：

- `产品表述` sheet：`分类 | ZH | EN | FR | 来源`
- `业务术语` sheet：`分类 | 缩写 | 中文 | 英文 | 释义 | 使用场景 | 状态`

仍是一份数据、一个文件，靠 `kind` 拆 sheet，避免半空的扁平表。不做"全部"合表 sheet（冗余且与 Excel 自带功能重复）；跨类搜索在使用说明里指引用 Excel"工作簿范围查找"。视觉样式沿用现有生成器（YaHei、表头深蓝、冻结首行、自动列宽）。旧三个产出物保留备查，不再作为维护入口。

## agent 入口（本期只交付契约，不写查询/校验代码）

- `record.schema.json`：机器可读统一契约。
- `AGENT.md`：写明 copilot 接入的**核心用例**——给一段文案，按概念池做 lookup+match，标出未对齐/用错的术语并给标准表达；以及按概念查对照、查解释、查溯源状态。后续 query/validate 工具的接口签名仅描述不实现。

## 剥离项

B/C 下 `cursor_excel/` + `tools/excel_sync.py` + `watch_excel.py` 同步的是 WBS/GTM 项目表，与对齐无关。移出 alignment 体系，物理移动位置执行时与你确认。

## 不做

- 不写 query/validate 可运行代码（spec_only）。
- 不做分人群视图渲染（留作后续功能）。
- 不动 `源文件/`、`历史版本/`。
- 不自动合并冲突概念（先出清单人工裁定）。

