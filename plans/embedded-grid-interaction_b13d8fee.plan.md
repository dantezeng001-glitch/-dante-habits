---
name: embedded-grid-interaction
overview: 优化两张内嵌表格的交互：选范围弹窗网格默认换行+收窄列宽+限制渲染行数并修拖拽，校对结果表新增拖拽改列宽。
todos:
  - id: grid-wrap-width
    content: 选范围网格默认换行、收窄默认列宽、换行单元格加行数截断（app.js RM/bindRegionModal/CSS）
    status: completed
  - id: grid-row-limit
    content: renderRegionGrid 默认只渲染前120行+“显示全部”控件；修 regionAll 全选到完整 n_rows
    status: completed
  - id: grid-resize-harden
    content: 列头内容包 position:relative 内层div，手柄锚定到它，加固拖拽改列宽
    status: completed
  - id: result-colgroup
    content: 结果表加 colgroup+S.resColW，列宽改用 col 元素，弱化 nth-child 百分比宽
    status: completed
  - id: result-resize
    content: 结果表表头加拖拽手柄并与排序共存（stopPropagation），复用通用 resize 函数
    status: completed
isProject: false
---

# 内嵌表格交互优化

## 背景（已核实）
- 选范围弹窗网格 `table.region-grid` 默认 `white-space: nowrap`，后端 `sheet_grid` 一次性返回最多 3000 行（[proofreader/excel_reader.py](proofreader/excel_reader.py) 第 75 行），前端全塞进 DOM → 又长又宽、卡顿。
- 校对结果表 `table.result` 表头是排序光标、无任何改列宽功能 → 这就是你"能点但列宽不变"的来源。
- 列宽手柄绝对定位锚在 `<th>` 上，表格单元格作为包含块不稳，是手柄"碰不到/不生效"的隐患。

## 改动 1：选范围网格默认换行 + 收窄列宽 + 限行渲染
文件：[ui/app.js](ui/app.js)、[ui/style.css](ui/style.css)

- `RM` 默认 `wrap: true`；`bindRegionModal` 里把换行按钮初始 `aria-pressed`/`active` 设为开。
- `DEFAULT_COL_W` 从 110 收窄（约 140），并在 CSS 给换行单元格加行数截断防止单行过高：

```css
table.region-grid.wrap td { white-space: normal; word-break: break-word; max-height: 7.5em; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 6; -webkit-box-orient: vertical; }
```

- `renderRegionGrid`：默认只渲染前 `RENDER_LIMIT`(=120) 行；网格下方加"已显示前 120 / 共 N 行 · 显示全部"控件，点击后重渲染全部行。完整单元格内容仍可点选在 `regionCellbar` 看全（已有）。
- 修 `regionAll`（第 540 行附近）：`r2` 由"已渲染最后一行"改为完整 `RM.grid.n_rows`，使"全选已用区域"覆盖整个范围。

## 改动 2：选范围网格拖拽改列宽加固
文件：[ui/app.js](ui/app.js) `renderRegionGrid`（第 593 行列头模板）、[ui/style.css](ui/style.css) `.col-resize`

- 列头内容包进内层 `div.colh-inner { position: relative }`，`.col-resize` 锚定到它而非 `<th>`，消除表格单元格作包含块的定位不稳。手柄宽度/高度沿用现有 `top:0;bottom:0;right:0`。

## 改动 3：校对结果表新增拖拽改列宽
文件：[ui/app.js](ui/app.js) `renderResult`(第 782 行)/`renderRows`(第 792 行)、[ui/style.css](ui/style.css) `table.result`(第 302–320 行)

- 状态加 `S.resColW`（9 列像素宽，初值由现有百分比按容器宽换算或给定默认值）。
- `renderResult` 输出的表加 `<colgroup>`，列宽走 `col` 元素；移除/弱化第 312–320 行的 `nth-child` 百分比宽。
- `renderRows` 的表头 `th` 内嵌 `position: relative` 包装 + 拖拽手柄，注意与现有"点表头排序"共存：手柄 `mousedown`/`click` 调 `stopPropagation`，避免拖拽误触发排序。
- 抽一个通用 `startColResizeGeneric(handle, colEl, getW, setW)` 复用网格与结果表逻辑，拖拽时加 `body.resizing-col` 锁光标（已有 CSS）。

## 验证
- 选范围弹窗：默认折行、列不被长文本撑宽、只显示前 120 行且能"显示全部"、全选覆盖整表、拖列头右边界即时改宽、双击自适应仍可用。
- 结果表：拖列头边界能改宽、点表头仍能排序、长文本仍 4 行截断。