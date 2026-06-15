---
name: 体验修正布局性能
overview: 承接一期反馈：把布局改成 Cursor 式（对话主体 + 右侧可开合可拖宽面板），修复内嵌表格加载慢（read_only 随机访问改 iter_rows），让范围选择器单元格内容可看全。后端 Agent 编排不动。完成后再进二期（补充材料整理）。
todos:
  - id: layout-resizable
    content: 布局改为对话主体 + 右侧可开合可拖宽面板（toggle + resizer + 自动打开时机）
    status: completed
  - id: perf-iterrows
    content: sheet_grid / extract_cells / preview 改 iter_rows 流式读取，行补齐到 max_col
    status: completed
  - id: grid-enhance
    content: 范围选择器网格增强：拖列宽/拖行高/双击自适应/选整列整行/换行可切换/底部全文显示
    status: pending
  - id: verify
    content: 重启验证：加载速度、布局开合/拖宽、单元格可看全
    status: pending
isProject: false
---

# 体验修正：Cursor 式布局 + 性能 + 可读性

一期把壳重构成对话工作台，实测暴露三个体验问题。这一期专修这三点，后端 Agent 编排（`orchestrator.py` / `chat_step`）不动。

## 三块改动

### 1. 布局：对话主体 + 右侧可开合可拖宽面板

当前是固定双栏（对话 42% + 工作区 flex），分隔不可拖、窄窗右栏被挤没。改成 Cursor 式：

```mermaid
flowchart LR
  chat["对话(占主体, flex:1)"]
  resizer["分隔条(可拖宽)"]
  panel["右侧工作面板(可开合)<br/>状态卡 + 结果表"]
  chat --- resizer --- panel
```

- 对话占满主体；右侧面板默认收起，header 加"工作区"开关按钮可手动开关。
- Agent 调工具改了状态(加文档/设范围/出结果)时自动滑出面板，让你看到变化。
- 中间分隔条可拖动调宽；面板有关闭按钮。
- 文件:[ui/index.html](ui/index.html)(加 toggle 按钮 + resizer + 面板容器)、[ui/app.js](ui/app.js)(开合/拖宽逻辑 + 自动打开时机)、[ui/style.css](ui/style.css)(`.workbench` 改为 chat flex:1 + 可变宽 work-pane + resizer 命中区)。

### 2. 性能:内嵌表格加载从"几秒"降到"亚秒"

根因明确:openpyxl read_only 模式下用 `ws.cell(row,col)` 随机访问会反复重扫文件。三处同病,改成 `iter_rows` 流式遍历:

- [proofreader/excel_reader.py](proofreader/excel_reader.py) `sheet_grid`(范围选择器加载,你主要抱怨的点)
- [proofreader/scope.py](proofreader/scope.py) `extract_cells`(跑校对路径)
- [proofreader/scope.py](proofreader/scope.py) `preview`(同模式一并修)
- 注意:iter_rows 要把每行补齐到 max_col,避免短行导致列错位。

### 3. 范围选择器:升级成准 Excel 网格

大模态保留(拖选需要最大空间)。当前是只读拖选网格、单元格截断。升级为更接近 Excel 的网格,全部六项:

- 拖列宽:用 `<colgroup><col>` 控制每列宽度,列头右边界加拖拽手柄。
- 拖行高:行号下边界加拖拽手柄。
- 双击列边界:按该列内容自动适应宽度。
- 点列头/行号:选中整列/整行(加速框选大区域)。
- 内容换行不截断:工具栏加开关,切换截断/换行显示。
- 底部全文条:悬停/点选某格→模态底部显示该格完整内容。

关键技术风险:拖拽手柄(改列宽/行高)与单元格拖选共用 mousedown,必须把手柄命中区与单元格选区事件分开(手柄区域 stopPropagation,不触发框选)。

- 文件:[ui/index.html](ui/index.html)(底部内容条 + 换行开关)、[ui/app.js](ui/app.js)(列宽/行高拖拽、整列整行选择、自适应、全文显示)、[ui/style.css](ui/style.css)(colgroup 列宽、手柄命中区、换行模式)。

## 二期是什么(布局稳了再做)

二期 = 你最早提的需求:**Agent + 文档上传整理补充材料**。在对话里上传参考文档或说一段话,Agent 归纳成结构化补充信息,区分两类:

- 判据(evidence):术语表/品牌规范等,直接影响校对结论(取代旧的"三方标准 + 角色")。
- 背景(context):只帮模型读懂语境,不单独判错。

取代你截图里那个"上传文件 + 敲说明 + 勾角色"的死板表单。

## 风险

- 拖宽/开合的鼠标事件要处理干净:拖动时禁用文本选中、resizer 命中区够宽、释放后保存宽度。
- iter_rows 改造必须保证每行列数补齐,否则范围内容与坐标错位会污染校对结果。
- 自动打开面板的时机别太频繁打扰,只在状态实质变化时触发。