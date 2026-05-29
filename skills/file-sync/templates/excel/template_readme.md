# Excel 自动同步说明

这个项目已经配置好一套给 Cursor 使用的 Excel 自动同步链路：

- 原始 Excel：项目内任意 `.xlsx` / `.xlsm`
- 自动输出目录：`cursor_excel/`
- 输出格式：每个工作表都会生成 `.csv`、`.json`、`.md`
- 总索引：`cursor_excel/index.md`
- 自动监听脚本：`tools/watch_excel.py`
- 单次同步脚本：`tools/excel_sync.py`

## 当前工作方式

1. 打开这个项目时，Cursor 会尝试自动启动 `Excel: watch sync` 任务。
2. 监听器会每 5 秒检查一次项目内 Excel 文件是否有变化。
3. 一旦发现新增、修改、删除，就会重新生成 `cursor_excel/` 下的文本产物。
4. Cursor 规则会优先读取 `cursor_excel/index.md` 和相关 `.md/.csv/.json`，而不是直接依赖 `.xlsx`。

## 如果自动监听没有启动

有些环境第一次打开项目时，会要求你允许自动任务。若未自动启动，可以手动执行：

1. `Terminal > Run Task`
2. 选择 `Excel: watch sync`

如果只是想立刻刷新一次，也可以运行：

1. `Terminal > Run Task`
2. 选择 `Excel: sync once`

## 可调整项

配置文件在 `excel_sync_config.json`，你可以修改：

- `source_patterns`：要追踪哪些 Excel 文件
- `exclude_patterns`：排除哪些目录或临时文件
- `preview_rows`：Markdown 预览保留多少行
- `preview_columns`：Markdown 预览保留多少列

## 建议使用方式

以后你直接对 Cursor 说：

- “帮我总结表格里的卖点结构”
- “根据最新 Excel 生成文案框架”
- “对比这个表格里不同版本的 FABE”

它会优先读 `cursor_excel/` 里的同步结果，不需要你每次手动打开 Excel。
