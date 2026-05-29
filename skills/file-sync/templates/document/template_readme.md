# 文档自动同步说明

这个项目已经配置好一套给 Cursor 使用的文档自动同步链路：

- 原始文档：项目内任意 `.pdf`、`.pptx`、`.ppt`
- 自动输出目录：`cursor_docs/`
- 输出格式：`.md`、`.txt`、`.json`
- 总索引：`cursor_docs/index.md`
- 自动监听脚本：`tools/watch_documents.py`
- 单次同步脚本：`tools/document_sync.py`

## 当前工作方式

1. 打开这个项目时，Cursor 会尝试自动启动 `Docs: watch sync` 任务。
2. 监听器会定期检查项目内文档是否有变化。
3. 一旦发现新增、修改、删除，就会重新生成 `cursor_docs/` 下的文本产物。
4. Cursor 规则会优先读取 `cursor_docs/index.md` 和相关 `.md/.txt/.json`，而不是直接依赖原始二进制文档。

## 文档类型说明

- `PPTX`：直接解析每一页幻灯片文本内容
- `PPT`：优先尝试调用 Windows PowerPoint 自动转换为 `PPTX`
- `PDF`：优先做直接文本提取；遇到扫描版页面时，尝试 OCR 回退

## 如果自动监听没有启动

1. `Terminal > Run Task`
2. 选择 `Docs: watch sync`

如果只是想立刻刷新一次，也可以运行：

1. `Terminal > Run Task`
2. 选择 `Docs: sync once`

## 依赖

基础解析常用 Python 包：

- `pypdf`
- `python-pptx`

OCR 相关可选依赖：

- `pymupdf`
- `pytesseract`
- `Pillow`

另外，OCR 还需要本机安装 `Tesseract OCR`。

## 建议使用方式

以后你直接对 Cursor 说：

- “总结这个 PDF 的重点”
- “读取这份 PPT 的每页内容”
- “把这份提案 deck 转成文案提纲”
- “分析扫描版 PDF 的核心信息”

它会优先读 `cursor_docs/` 里的同步结果，不需要你每次手动打开文档。
