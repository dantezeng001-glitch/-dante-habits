---
name: region-grid-redesign
overview: 修复内嵌选区网格塌缩根因（table-layout:fixed 未生效 + td 被 -webkit-box 破坏单元格语义）用 Excel 风单行截断重做展示；并把选区交互拆成两步（点起点→点终点选定，带预览，保留拖拽）。
todos:
  - id: fixed-table-width
    content: renderRegionGrid/startColResize/autoFitCol 设置并同步 tbl.style.width=52+sum(colW)，让 table-layout:fixed 生效
    status: completed
  - id: cell-inner
    content: 单元格值包 .cell-inner div；CSS 把截断/换行规则移到 .cell-inner，删除把 td 变 -webkit-box 的规则
    status: completed
  - id: default-nowrap
    content: RM.wrap 默认 false（紧凑单行），换行开关沿用
    status: completed
  - id: two-step-select
    content: 选区拆两步（方案A）：点起点→点终点选定，带预览(picking)；保留拖拽松手即选定；Esc 取消；列头/行号/手填范围清掉 pending
    status: completed
  - id: pending-style
    content: 新增 RM.anchor/pending/committedSel 状态与 .picking 预览样式（虚线浅色）；paintRegion 按 pending 切换预览/确定外观
    status: completed
  - id: verify
    content: 验证列等宽不塌缩、拖拽/双击/横向滚动、换行模式、显示全部、两步点选与预览、Esc 取消
    status: completed
isProject: false
---

# 内嵌选区网格重做

## 根因（已定位）
1. [ui/style.css](ui/style.css) 第 390 行把 `td` 设成 `display: -webkit-box`，单元格失去 `table-cell` 语义，不再受列宽约束 → 列塌成 1 字符宽、长文竖排（截图现象）。
2. `table.region-grid` 从未设 `width`，`table-layout: fixed` 在 Chromium 下无宽度时退回自动排版 → 长文本把列撑宽（你最早说的"行很长"的真正根子）。

## 交互模型（目标）
- 像 Excel 选区：列宽固定可读，单元格默认单行、超出显示"…"，点单元格在底部栏看全文。
- 列宽真正受控：拖列头右边界即时改宽、双击自适应；表整体随列宽横向滚动。
- 长文本不撑宽：固定布局下被截断；需要读全文时点"换行"开关，文本在固定列宽内折行、每格最多 5 行后截断（行变高但不撑宽）。
- 大表不卡：默认渲染前 120 行 + "显示全部"。
- 选区两步走：先「选范围」（点起点 + 预览），再「选定」（点终点 / 拖拽松手），不再一拖到底跟着鼠标跑。

## 改动 1：让 table-layout:fixed 真正生效
文件：[ui/app.js](ui/app.js) `renderRegionGrid` / `startColResize` / `autoFitCol`

- 新增 `regionTableWidth()` = `52 + RM.colW 之和`（52 为角列 `cg-corner` 宽）。
- `renderRegionGrid` 渲染后设 `tbl.style.width = regionTableWidth() + "px"`，使固定布局以列宽为准。
- 列宽拖拽 `startColResize` 的 `setW`、`autoFitCol` 落地列宽后，同步更新 `tbl.style.width`。

## 改动 2：单元格内容包内层 div，修换行/截断
文件：[ui/app.js](ui/app.js) `renderRegionGrid` body 模板、[ui/style.css](ui/style.css) 第 389-390 行

- 单元格值包进 `<div class="cell-inner">…</div>`（`<td>` 保持 `table-cell`，列宽不再被破坏）。
- CSS：
  - `td`：去掉直接的 `white-space/text-overflow`，保留 `overflow:hidden; vertical-align:top; cursor:cell`。
  - 默认：`.region-grid .cell-inner { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }`
  - 换行：`.region-grid.wrap .cell-inner { white-space:normal; word-break:break-word; display:-webkit-box; -webkit-line-clamp:5; -webkit-box-orient:vertical; }`
  - 删除第 390 行那条把 `td` 变 `-webkit-box` 的规则。

## 改动 3：默认改回紧凑单行（Excel 风）
文件：[ui/app.js](ui/app.js) `RM` 初始

- `RM.wrap` 默认 `false`；`bindRegionModal` 已按 `RM.wrap` 设置"换行"按钮初始态，自动同步为关闭。
- 保留 `REGION_RENDER_LIMIT=120` 与"显示全部"、`regionAll` 选到完整 `n_rows`、列头 `.colh-inner` 手柄加固（这些上轮已正确，不回退）。

## 改动 4：选区交互拆两步（方案 A）
文件：[ui/app.js](ui/app.js) `attachRegionEvents` / `bindRegionModal` / `openRegionFor` / `paintRegion`、[ui/style.css](ui/style.css)

状态（加到 `RM`）：`anchor`(已点起点 {r,c})、`pending`(是否处于"选范围"预览中)、`committedSel`(上次选定，Esc 还原用)；模块级 `SEL = { dragStart, dragMoved }` 区分点击与拖拽。

逻辑（`td` 上 `mousedown`/`mouseenter` + 文档级 `mouseup`，文档监听只在 `bindRegionModal` 绑一次避免叠加）：
- `mousedown(td)`：记 `SEL.dragStart={r,c}`、`dragMoved=false`，先不改选区。
- `mouseenter(td)`：
  - 若 `SEL.dragStart` 存在（按住移动）→ 拖拽：`dragMoved=true`，`RM.anchor=dragStart`，`RM.pending=true`，`RM.sel=rect(dragStart, 当前格)`，`paintRegion()`。
  - 否则若 `RM.pending && RM.anchor`（两次点击之间）→ 预览：`RM.sel=rect(anchor, 当前格)`，`paintRegion()`。
  - 否则 → `showCellFull`（看全文）。
- `mouseup(document)`：
  - 拖拽完成(`dragMoved`)：`RM.pending=false`，提交（`paintRegion()`+`syncRegionInput()`+`committedSel=clone`，清 `anchor`）。
  - 纯点击：若 `pending&&anchor` → 这是终点：`RM.sel=rect(anchor, 点击格)`，提交。否则 → 这是起点：`RM.anchor=点击格`，`RM.pending=true`，`RM.sel=单格`，`paintRegion()`（进入预览）。
- `Esc`（`bindRegionModal` 绑一次）：若 `pending` → `RM.sel=committedSel`，清 `pending/anchor`，`paintRegion()`+`syncRegionInput()`。
- 列头/行号点选、手填范围、`regionAll`：设置后都 `RM.pending=false; RM.anchor=null`，即时提交。
- `paintRegion()` 末尾 `tbl.classList.toggle("picking", !!RM.pending)`；`openRegionFor`/`closeRegion` 重置 `anchor=null,pending=false,SEL` 清空。

提示文案：`updateRegionInfo` 在 `pending` 时显示"起点 A1 · 点终点或拖动选定 → 当前 A1:H60"，选定后显示"已选 A1:H60（n 行 × m 列）"。

## 改动 5：预览态样式
文件：[ui/style.css](ui/style.css)

- 已选定：沿用 `td.cell-sel`（实线 `box-shadow` + `primary-soft`）。
- 预览中：`table.region-grid.picking td.cell-sel { box-shadow:none; outline:1px dashed var(--primary); outline-offset:-1px; }`（虚线、轻量），区分"正在选"与"已选定"。
- 起点角标可选：`anchor` 单元格加 `.cell-anchor`（左上小三角或更粗描边），让用户看清起点。

## 不动的部分
- 结果表 `table.result`（有 `width:100%`，固定布局本就生效，列宽拖拽与 4 行截断正常）保持不变。

## 验证
- 打开选区弹窗：各列约 140px 等宽、长文本单行"…"截断、不再竖排塌缩。
- 拖列头右边界即时改宽、双击自适应、整表横向滚动正常。
- 点"换行"：文本在固定列宽内折行、每格最多 5 行截断，列不被撑宽。
- 前 120 行 + "显示全部"、全选已用区域覆盖整表、点列头/行号选整列整行、点单元格底部看全文均正常。
- 两步选区：点起点出现虚线预览、移动鼠标预览跟随、点终点转实线并写入范围；按住拖拽松手即选定；Esc 取消回到上次选定；列头/行号/手填范围都能正常打断并立即生效。