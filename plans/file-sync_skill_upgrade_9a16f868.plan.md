---
name: file-sync skill upgrade
overview: 将 MD 提取后清理和可读性优化的通用能力融入现有 file-sync skill，新增 Part C（MD Post-Processing）模块，包含一个通用清洗脚本和 SKILL.md 的 AI 格式优化指引。
todos:
  - id: create-cleanup-script
    content: 新建 scripts/md_cleanup.py：通用 MD 字符清洗脚本（NFKC + 康熙部首 + 部首补充 + 繁简 + 空行压缩）
    status: completed
  - id: update-skill-md
    content: 在 SKILL.md 中新增 Part C 章节（后处理规则 + AI 格式优化指引）
    status: completed
  - id: upgrade-sync-template
    content: 升级 template_document_sync.py：normalize_text 加 NFKC，PDF 提取优先 pymupdf
    status: completed
  - id: update-reference
    content: 更新 reference.md：新增依赖说明和 cleanup 脚本说明
    status: completed
isProject: false
---

# file-sync skill 增强：MD 后处理与可读性优化

## 现状分析

现有 file-sync skill 分两部分：

- **Part A**: 二进制 -> MD（PDF/PPT/PPTX -> `cursor_docs/`）
- **Part B**: MD -> DOCX/PDF（反向导出）

当前 Part A 的 `template_document_sync.py` 使用 `pypdf` 提取 PDF，对中文 PDF 效果较差（CJK 部首字符、Type3 字体编码问题），且提取后的 MD 是扁平的 Page/Slide 格式，可读性差。

## 增强方案

新增 **Part C: MD Post-Processing（提取后处理）**，包含两个层次：

### 层次一：自动化字符清洗（脚本）

在 `scripts/` 目录下新增 `md_cleanup.py`，作为**技能内置脚本**（类似 `md_to_docx.py`），可直接调用：

```
python "<skill-dir>/scripts/md_cleanup.py" "<input.md>" [--in-place]
```

从 `clean_md.py` 中提取的**通用能力**（非业务相关）：

- **NFKC 规范化**：`unicodedata.normalize("NFKC", text)` 统一全半角
- **CJK 康熙部首映射**：完整 U+2F00-U+2FD5 共 214 项 -> 标准 CJK 字符
- **CJK 部首补充映射**：U+2E80-U+2EFF 常见简体子集（车/长/页/马/骨/齐等）
- **繁简转换子集**：`用戶->用户` 等 PDF 常见繁体残留
- **多余空行压缩**：`\n{3,}` -> `\n\n`

**不纳入**的项目特定内容：

- Type3 字体 ASCII->汉字映射（`N->上`、`O->下` 等）——高度语料相关
- 句末 `2->。` 的替换——仅适用于特定 PDF
- 特定拉丁字符映射（`ÿ->（` 等）——字体相关

### 层次二：AI 格式优化指引（写入 SKILL.md）

在 SKILL.md 的 Part C 中加入**操作规则**，指导 AI（Cursor）在提取 MD 后自动判断并优化格式。这是通用知识，不绑定"复盘文件"格式：

**识别与触发**：

- 当 MD 文件包含 `## Page X` 或 `## Slide X:` 等自动提取标记时，判断为"需要格式优化"
- 用户主动要求"整理格式"或"提高可读性"时触发

**通用格式优化规则**（从实操中提取的知识）：

1. `## Page/Slide X` 标题 -> 基于内容的语义化标题
2. 散落的结构化数据行 -> Markdown 表格
3. 扁平文本 -> 层级列表（bullet/numbered）
4. 关键指标/结论 -> 加粗标记
5. 同主题多页内容 -> 合并到同一章节
6. 重复的分隔页/目录页/空白页 -> 删除
7. 保留所有原始数据，不添加不存在的内容

### 层次三：增强 `template_document_sync.py`

在模板同步脚本的 `normalize_text` 函数中增加 NFKC 规范化，并在 PDF 提取流程中优先使用 `pymupdf`（如已安装），回退到 `pypdf`。

## 文件变更清单


| 文件                                                                                                                                      | 操作  | 说明                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --- | ---------------------------------------------- |
| `[SKILL.md](C:\Users\016551\.cursor\skills\file-sync\SKILL.md)`                                                                         | 修改  | 新增 Part C 章节（MD Post-Processing 规则）            |
| `[scripts/md_cleanup.py](C:\Users\016551\.cursor\skills\file-sync\scripts\md_cleanup.py)`                                               | 新建  | 通用 MD 字符清洗脚本（~150行）                            |
| `[templates/document/template_document_sync.py](C:\Users\016551\.cursor\skills\file-sync\templates\document\template_document_sync.py)` | 修改  | `normalize_text` 增加 NFKC；PDF 提取增加 pymupdf 优先逻辑 |
| `[templates/document/reference.md](C:\Users\016551\.cursor\skills\file-sync\templates\document\reference.md)`                           | 修改  | 依赖列表新增 `pymupdf` 说明、新增 cleanup 脚本说明            |


## SKILL.md Part C 章节结构草案

```markdown
## Part C: MD Post-Processing (Readability Enhancement)

### Automatic Character Cleanup
- Run: `python "<skill-dir>/scripts/md_cleanup.py" "<input.md>" --in-place`
- Handles: NFKC normalization, CJK Kangxi radical replacement, 
  CJK Radicals Supplement, common traditional-to-simplified, 
  excess blank lines

### AI-Guided Format Optimization (Operating Rules)
When a synced MD file contains `## Page` or `## Slide` headings 
(indicating raw extraction output), apply these restructuring rules:

1. Replace extraction headings with semantic headings based on content
2. Reconstruct scattered data lines into Markdown tables
3. Convert flat text into hierarchical lists
4. Bold key metrics and conclusions
5. Merge multi-page/slide content under unified topic headings
6. Remove empty pages, separator slides, and redundant TOC slides
7. NEVER add content not present in the original
8. ALWAYS run md_cleanup.py first to fix encoding artifacts
```

