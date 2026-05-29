---
name: md cleanup skill
overview: 创建输入源无关的通用 MD 可读性清洗 skill，把 file-sync 里"能力通用"的字符清洗和 AI 语义重排能力迁入，file-sync 瘦身到只保留抽取特有的后处理（OCR 重抽、PDF 断行合并、验证审计），通过脚本层和 SKILL.md 层双重联动让 file-sync 跑完自动衔接 cleanup。
todos:
  - id: scaffold
    content: 在 ~/.cursor/skills/md-cleanup/ 下 scaffold 目录结构（SKILL.md 空壳 + scripts/ + references/）
    status: completed
  - id: migrate-script
    content: 把 file-sync/scripts/md_cleanup.py 迁入 md-cleanup/scripts/ 并扩写 F2/F3/F4 规则（转义、富文本伪影、链接文案）
    status: completed
  - id: draft-skill-md
    content: 起草 md-cleanup/SKILL.md：按 F1–F6 伪影家族组织规则库，每条带触发条件、Before/After 示例
    status: completed
  - id: compile-references
    content: 整理 references/artifact-patterns.md：钉钉导出伪影清单（基于今天的清洗经验），预留飞书/Notion/Google Docs 占位
    status: completed
  - id: refactor-file-sync-md
    content: 改写 file-sync/SKILL.md：Part C 瘦身到只保留 Step 0 / 1.5 / 3，硬约束里点名指向 md-cleanup，删除 Step 1 / Step 2 正文描述
    status: completed
  - id: refactor-file-sync-py
    content: 改写 file-sync 的 Python 脚本（file_sync.py / document_sync.py / excel_sync.py）：Part A 结束后 subprocess 调 md-cleanup/scripts/md_cleanup.py，带路径检测兜底
    status: completed
  - id: regression-dingtalk
    content: 回归验证 1：用今天清洗的游泳 IMC 项目书作为样本，跑 md-cleanup 产出应接近手动清洗结果
    status: completed
  - id: regression-filesync
    content: 回归验证 2：挑一个 SwimPro 下的 PDF 跑 file-sync 一条龙，验证自动衔接 md-cleanup 后输出等价于改造前
    status: completed
  - id: regression-noop
    content: 反例验证：拿一份干净的手写 MD 跑 md-cleanup，应基本不改动（触发条件全不命中）
    status: completed
isProject: false
---

# MD Cleanup Skill 方案

## 一、核心判断

Cursor Skills 靠 description 和触发词激活，agent 看到一份 MD 分不出来源。所以新 skill 定位为**输入源无关的通用 MD 可读性清洗**，覆盖：PDF/PPT 抽取出的 MD、钉钉/飞书/Notion/Google Docs 导出的 MD、用户手写的 MD。

## 二、新 Skill 结构

路径：`C:\Users\016551\.cursor\skills\md-cleanup\`（**名称待定，见决策点 1**）

```
md-cleanup/
├── SKILL.md              # 主入口，按"伪影家族"组织规则库
├── scripts/
│   └── md_cleanup.py     # 从 file-sync 迁入 + 扩写
└── references/
    └── artifact-patterns.md   # 各家协作文档导出的伪影清单（钉钉优先，其他扩）
```

## 三、规则库按「伪影家族」组织（不按来源）

每家规则都带**触发条件**，不是每份文件都跑全部规则。

- **F1 字符级**（沿用 file-sync 现有逻辑）
  - 康熙部首 `⼀⽉⾊⾸` → `一月色首`（U+2F00 块映射）
  - CJK 补充 `⻚⻢⻓` → `页马长`（U+2E80 块映射）
  - NFKC 全/半角归一化
  - 传统字残留（`戶` → `户`等常见对）
  - 触发：字符匹配
- **F2 转义级**
  - `\-` `\`* `\_` `\|` 等冗余 MD 转义
  - 触发：正则匹配
- **F3 富文本导出伪影**
  - `$\color{#...}{@xxx(yyy)}$` LaTeX 提及 → `@xxx（yyy）`
  - `:::` 围栏容器 → 删除
  - 表格单元格内 `1.  xxx<br>    <br>2.  yyy` → 扁平化
  - `$\color{...}$` 着色包裹的其他内容 → 剥离
  - 触发：关键字符串检测
- **F4 链接文案级**
  - `请至钉钉文档查看附件《...》` → `《...》`
  - 其他冗余前缀按需追加
  - 触发：字面字符串
- **F5 结构级**
  - 全 `#` 一级标题 → 按语义重建 H1/H2/H3（AI 判断）
  - `## Page \d+` / `## Slide \d+:` → 按内容改为语义标题（AI 判断，继承 file-sync Step 2 逻辑）
  - 扁平 bullets（所有正文以 `-`  开头）→ 重组层级
  - 触发：标题分布统计
- **F6 噪音级**
  - 多重空行压缩（3+ 空行 → 2 行）
  - `[No text extracted]` 残留
  - 孤立的 `±` `°` 符号行
  - 触发：模式匹配

## 四、file-sync 改造

**保留不动：**

- Part A：所有抽取逻辑
- Part B：MD → DOCX / PDF
- Part C **Step 0**（空页 / 图片页 OCR 重抽）— 依赖 OCR pipeline，抽取特有
- Part C **Step 1.5**（`md_line_join.py` PDF 断行合并）— PDF 来源特有
- Part C **Step 3**（最终验证审计）— 抽取交付标准

**迁走：**

- Part C **Step 1**（`md_cleanup.py` 字符清洗）→ 并入 md-cleanup F1 + F2
- Part C **Step 2**（AI 语义重排）→ 并入 md-cleanup F5

**SKILL.md 重写要点**：`file-sync/SKILL.md` 顶部"交付前硬约束"从 5 步顺序 → Step 0 → **调 md-cleanup** → Step 1.5（PDF 来源必做） → Step 3。Part C 章节大幅瘦身，只保留 Step 0 / 1.5 / 3 的细节。

## 五、联动机制（双层）

**脚本层（自动化）：**

`file-sync/tools/file_sync.py`、`document_sync.py`、`excel_sync.py` 在 Part A 抽取完成后，自动 `subprocess.run` 调 `md-cleanup/scripts/md_cleanup.py` 处理所有输出 `.md` 文件。用户跑一次 `python tools/file_sync.py` 依旧一条龙。

```python
# file_sync.py 末尾伪代码
md_cleanup_script = Path(cursor_skills_dir) / "md-cleanup" / "scripts" / "md_cleanup.py"
subprocess.run([sys.executable, str(md_cleanup_script), *output_md_files, "--in-place"])
```

**SKILL.md 层（agent 推理任务）：**

`file-sync/SKILL.md` 硬约束里点名："字符清洗和 AI 语义重排由 md-cleanup skill 提供，agent 必须读 `~/.cursor/skills/md-cleanup/SKILL.md` 并按其执行"。这样 agent 在执行 file-sync 任务时自动装载 md-cleanup 规则，处理脚本搞不定的 AI 判断部分（如 F5 结构级的语义标题重建）。

## 六、验收场景

1. **回归样本 1（钉钉导出）**：把"2026 北美区域游泳 IMC 项目书"恢复到清洗前状态，跑 md-cleanup 应产出与我刚才手动清洗一致（或更好）的结果
2. **回归样本 2（PDF 抽取）**：随便拿一个 SwimPro 下的 PDF 跑 file-sync → 自动衔接 md-cleanup，输出应与改造前的 file-sync 五步流水等价
3. **回归样本 3（Excel 抽取）**：跑 `excel_sync.py`，产出的 per-sheet `.md` 也自动走 md-cleanup
4. **反例**：手写 MD 跑 md-cleanup，应该基本不动（触发条件不命中）

## 七、待决策点（需要你确认后再动手）

**决策点 1：skill 命名**

- A. `md-cleanup`（简洁，推荐）
- B. `markdown-readability`（语义明确，稍长）
- C. `md-polish`（偏营销向）

**决策点 2：`md_cleanup.py` 脚本物理位置**

- A. 随 skill 迁到 `md-cleanup/scripts/`，file-sync 的 Python 脚本跨 skill 硬编码路径调用它（**推荐**，边界清晰）
- B. 放公共位置 `~/.cursor/shared-scripts/`，两个 skill 各自引用（好处是解耦，坏处是 shared-scripts 这个目录还不存在，需要新约定）

**决策点 3：是否保留 file-sync/SKILL.md 里的 Part C 完整描述**

- A. 大幅瘦身，Part C 只保留 Step 0 / 1.5 / 3，其余指向 md-cleanup（**推荐**，避免同一份规则两边都写）
- B. 保留简版摘要 + 指向 md-cleanup 完整规则（稍冗余但 file-sync 可独立阅读）

## 八、风险与回滚

- **风险 1**：file-sync 脚本硬编码 md-cleanup 路径（`~/.cursor/skills/md-cleanup/scripts/md_cleanup.py`），如果 md-cleanup 目录改名，file-sync 脚本要同步改。**缓解**：加一个启动时的路径检测，找不到就回退到本地已打包的旧版 `md_cleanup.py`（迁移期保留一份兜底）。
- **风险 2**：agent 在 file-sync 任务里没有主动读 md-cleanup/SKILL.md。**缓解**：硬约束段落用"**agent MUST read**"措辞，并在文件顶部复述一次。
- **回滚**：如果方案不成立，把 `md_cleanup.py` 从 md-cleanup/scripts/ 复制回 file-sync/scripts/，恢复 file-sync/SKILL.md 旧版，删除 md-cleanup 目录即可。整个过程改动都在用户本地 `.cursor/skills/` 目录内，不涉及 cloud side effect。

