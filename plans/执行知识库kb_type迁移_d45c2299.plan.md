---
name: 执行知识库kb_type迁移
overview: 按已确认的 7 类 kb_type 体系，执行阶段 4（迁移 84 篇文档 + 改写 frontmatter + 批量修复 source_docs 路径）和阶段 5（前端 formatKbType 加 3 个新值 + 治理文档同步），完成知识库重构。
todos:
  - id: stage4-script
    content: 写迁移脚本 migrate_kb_v2.py，内嵌 84 篇迁移映射表
    status: completed
  - id: stage4-dryrun
    content: 跑 --dry-run，贴出所有将执行动作，确认无意外
    status: completed
  - id: stage4-execute
    content: 跑真迁移：物理 move + frontmatter 改写 + source_docs 批量修复
    status: completed
  - id: stage4-cleanup
    content: 删除第九节列出的空旧子目录
    status: completed
  - id: stage4-smoke
    content: 启动 server.py 跑 facets 冲烟，确认 7 类 kb_type 在前端可见
    status: completed
  - id: stage5-formatKbType
    content: app.js 的 formatKbType 加 3 个新 kb_type 中文显示
    status: completed
  - id: stage5-governance
    content: 同步 README、治理看板、lint 文档与新规范一致
    status: completed
isProject: false
---

# 执行知识库 kb_type 迁移

## 前提

- 阶段 1（[元数据规范.md](知识库/运行域/治理文档/元数据规范.md)）、阶段 2（12 个新目录 + README）已完成。
- 阶段 3 清单 [迁移清单_kb_type_v2.md](知识库/运行域/治理文档/迁移清单_kb_type_v2.md) 用户已认可。
- 第八节 2 处 `[?]` 按默认判断处理：`Being 营销策略学习` → decision、`2026 科技树内容规划书` → decision。

## 执行思路：脚本化，不手工

84 篇文档 + 路径修复，手工不可控。我会写一个一次性 Python 脚本 [前端开发/data/migrate_kb_v2.py](前端开发/data/migrate_kb_v2.py)，做三件事：

1. **读"迁移映射表"**（脚本内嵌为 Python 字典，旧路径→新路径+新 kb_type）
2. **物理迁移**：`shutil.move` 旧路径到新路径，自动建中间目录
3. **frontmatter 改写**：用 regex 改 `kb_type` 字段，同步更新 `canonical_path`，按新规范补 `tech_analysis`/`market_research`/`plan` 的必填字段
4. **批量修复 source_docs**：扫全库所有 md，把 `source_docs:` 列表里指向旧路径的 line 重写为新路径

脚本结束打印：迁移文件数、改写 frontmatter 数、修复 source_docs 引用数、未匹配的旧路径警告。

## 阶段 4 步骤

### 4.1 写迁移脚本（一次性脚本，不留长期工程化）

文件位置：`前端开发/data/migrate_kb_v2.py`

核心数据结构：

```python
MIGRATIONS = [
    # (旧相对路径, 新相对路径, 新 kb_type, 补字段 dict)
    ("知识库/产品主张/OpenSwim Pro/OpenSwim Pro 水下使用场景与主观音质感受分析.md",
     "知识库/概念原理/产品技术分析/OpenSwim Pro 水下使用场景与主观音质感受分析.md",
     "tech_analysis",
     {"related_products": ["OpenSwim Pro"]}),
    # ... 共约 50 条非平凡迁移；27 篇 concept 留原 kb_type 但路径变化
    # ... 13 篇 source_summary 完全不动
]
```

完整映射严格按 [迁移清单_kb_type_v2.md](知识库/运行域/治理文档/迁移清单_kb_type_v2.md) 第一到第七节生成。

### 4.2 frontmatter 改写规则

- 所有迁移项：`kb_type` 改为新值；`canonical_path` 改为新路径；保留其他字段。
- `tech_analysis` 类（5 篇）：补 `related_products`（从文件名/原 frontmatter 推断）。
- `market_research` 类（14 篇）：补 `research_subject`（user/competitor/industry，按子目录决定）。
- `plan` 类（10 篇）：补 `status: active`、`due_date:`（留空待用户后续填）。
- `source_summary` 类（13 篇）：完全不动。

### 4.3 source_docs 路径修复

扫全库（含 `运行域/`）所有 md，对每行匹配 `^\s*-\s*知识域/(...).md` 的 source_docs 引用：

- 若旧路径在迁移映射表中 → 重写为新路径
- 若旧路径不在表中（说明引用的文件没动） → 不改
- 若旧路径在表中但新路径下文件不存在（异常） → 打印警告

### 4.4 删除空目录

迁移完成后扫 `知识库/知识域/`，按 [迁移清单_kb_type_v2.md](知识库/运行域/治理文档/迁移清单_kb_type_v2.md) 第九节列出的 6 个旧子目录，若已空则 `os.rmdir`。

`产品主张/OpenSwim Pro/` 等"按产品"目录保留为空（清单第九节脚注说明）。

### 4.5 跑前端冒烟

启动 [前端开发/server.py](前端开发/server.py) → `curl /api/documents?scope=knowledge&limit=200` → 确认 84 篇仍可读取且 facets.kbTypes 含 `tech_analysis / market_research / plan`。

## 阶段 5 步骤

### 5.1 [前端开发/static/app.js](前端开发/static/app.js) 加 3 个新 kb_type 中文显示

定位 `formatKbType` 函数（已知它把英文 kb_type 翻成中文），加 3 行：

```javascript
const KB_TYPE_LABELS = {
  // ...existing
  tech_analysis: "产品技术分析",
  market_research: "市场调研",
  plan: "项目计划",
};
```

### 5.2 治理文档同步

更新两份文档与新规范对齐：

- [前端开发/README.md](前端开发/README.md) 第 5/77 行的"按……负责人筛选"已经过时（负责人筛选器在前一个 plan 里被删了）+ 没提新 kb_type → 重写"页面能力"小节
- [知识库/运行域/治理文档/治理看板.md](知识库/运行域/治理文档/治理看板.md)、[知识库/运行域/治理文档/lint_kb_prompt.md](知识库/运行域/治理文档/lint_kb_prompt.md)（如存在）→ 把"4 类 kb_type"措辞同步为"7 类"

具体范围在执行时先 grep 定位，不预先列死。

## 风险与回滚

- **没有 git 仓**：你已确认承担风险。脚本以 `shutil.move` 而非 `copy + delete`，但**会先 dry-run 一次**打印所有动作，等用户在 Agent 模式下看到 dry-run 输出再执行真迁移。这是脚本的双阶段开关。
- **OneDrive 占用文件**：迁移可能因 OneDrive 同步而失败。脚本对单文件失败重试 3 次后跳过并记入失败列表。
- **source_docs 路径修复误伤**：只改"完全匹配旧路径"的行，不做模糊匹配。

## 不动的东西（明确写出防止扩散）

- [前端开发/kb_backend.py](前端开发/kb_backend.py)：frontmatter 解析是宽松字符串，不需要改枚举校验。
- [前端开发/server.py](前端开发/server.py)：API 不动。
- 知识库根目录其他位置（`运行域/同步文档/`、`收件箱/`）：内容不动；source_docs 修复时若引用了新路径才改。

## 完成标准

1. 84 篇文档物理位置与 [迁移清单_kb_type_v2.md](知识库/运行域/治理文档/迁移清单_kb_type_v2.md) 一致
2. 每篇文档 frontmatter 的 `kb_type` 与新规范一致
3. 全库 source_docs 引用零失效（脚本最终报告 0 条警告）
4. 浏览页 kbType 筛选下拉能看到 7 个值
5. 旧空目录已删除
6. todos 全部 completed

