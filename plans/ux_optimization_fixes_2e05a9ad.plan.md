---
name: UX optimization fixes
overview: 分三层修复北美趋势日报 web 网页和桌面挂件的用户体验问题：先补齐"出错/换内容后用户无下一步动作"的硬伤，再改善反馈、新鲜度、无障碍与一致性，最后做交互打磨。
todos:
  - id: web-refresh
    content: Web 端加手动刷新按钮 + 错误红条重试按钮，loadArchives 失败不再静默
    status: completed
  - id: web-loading
    content: Web 端切换存档/刷新时显示加载态（非首屏全屏 loader）
    status: completed
  - id: widget-config-cmd
    content: Rust 新增 save_config 命令写入 app_config_dir/config.json
    status: completed
  - id: widget-config-ui
    content: 挂件加设置入口可填并保存 API 地址，修掉 devFetch 硬编码
    status: completed
  - id: widget-error-recover
    content: 挂件不可达 placeholder 放明显重试按钮 + 打开设置入口
    status: completed
  - id: freshness
    content: 统一数据新鲜度显示：web 时区标注、挂件常驻上次更新时间
    status: completed
  - id: a11y
    content: 加 focus-visible 样式、信源状态色彩冗余、复核摘要对比度
    status: completed
  - id: widget-copy
    content: 挂件收窄 user-select，允许标题/摘要/tip 文字可选复制
    status: completed
  - id: web-archive-front
    content: Web 存档区从页尾前置，缩短回看路径
    status: completed
  - id: widget-theme-name
    content: 挂件主题切换显示当前主题名
    status: completed
  - id: widget-tab-discover
    content: 挂件横向 tab 加左右箭头或滚动暗示
    status: completed
  - id: section-consistency
    content: 统一 web 与挂件分区命名和顺序
    status: completed
isProject: false
---

# 北美趋势日报 UX 优化方案

按"能不能用 → 顺不顺 → 打磨"分三层，覆盖 web 网页、桌面挂件前端、挂件 Rust 后端。每条改动只动必要文件，遵守外科手术式 diff。

## 涉及文件
- Web: [src/App.jsx](src/App.jsx)、[src/styles.css](src/styles.css)
- 挂件前端: [desktop/src/widget.js](desktop/src/widget.js)、[desktop/src/index.html](desktop/src/index.html)、[desktop/src/widget.css](desktop/src/widget.css)
- 挂件后端: [desktop/src-tauri/src/lib.rs](desktop/src-tauri/src/lib.rs)

## 第一层：高优先级（能不能用）

### 1. Web 端加手动刷新 + 失败重试
- 在 `briefing-bar` 或 hero 区加一个刷新按钮，调用 `loadDigest(activeDate)`。
- 错误红条 `{error && ...}` 内加"重试"按钮，点了重新 `loadDigest`。
- `loadArchives()` 失败不再静默，记一个轻量提示状态。

### 2. Web 端切换存档/刷新时的加载反馈
- 当前 `loading` 只在 `loading && !digest` 时显示全屏 loader。改为：`digest` 已存在但 `loading` 时，在 `briefing-bar` 或内容区顶部显示一个细加载条/置灰，让用户知道点击生效了。
- 给 `archive-item` 点击态加 `disabled`/loading 视觉，避免重复点击。

### 3. 挂件 API 地址 UI 内可配置
- Rust 侧新增 `save_config` 命令：把 `{apiBaseUrl, refreshIntervalMinutes, ...}` 写入 `app_config_dir()/config.json`（`load_config` 已支持从该路径覆盖读取，见 lib.rs 50-62 行）。
- 挂件前端加一个轻量设置入口（顶栏齿轮或托盘菜单项），可填 API 地址并保存，保存后重新 `load_digest`。
- 修掉 `devFetch` 里第二处硬编码 `172.16.199.56:5050`，改成读 `state.config.apiBaseUrl`，与配置统一。

## 第二层：中优先级（顺不顺）

### 4. 挂件错误恢复入口提级
- 内网不可达的 placeholder 里直接放一个明显的"重试"按钮（不只依赖顶栏 24px 的 ⟳），并附"打开设置改地址"链接。

### 5. 数据新鲜度统一可见
- Web "生成时间"标注时区（统一显示北京时间或本地时间二选一并标明），与"下次 08:00 BJT"对齐。
- 挂件 `meta-row` 常驻显示"上次更新 时:分"（不只在 stale 时出现），数据来源用 `payload.cachedAt`/`generatedAt`。

### 6. 无障碍与键盘可达性
- 给 `side-nav a`、`item-card`、挂件 `.tab`/`.card` 加可见 `:focus-visible` 样式。
- 信源状态点 `dot ok/bad` 增加文字或形状冗余（如 "正常/失败" 文案或 ✓/✕），不只靠颜色。
- 复核正文摘要 `--muted`/`--mute-2` 对比度，必要时调高透明度。

### 7. 挂件允许复制文字
- 把全局 `user-select: none` 收窄：顶栏/标签/按钮保持不可选（便于拖动），但 `.card .title`、`.summary`、`.tip`、`.brief-summary` 允许 `user-select: text`。

### 8. Web 存档前置
- 把 `ArchiveRail` 从页尾移到正文上方（hero/briefing-bar 之后或正文侧栏），缩短回看路径；或在 hero 区加"最近存档"快捷下拉。

## 第三层：打磨

### 9. 挂件主题切换显名
- `cycleTheme` 后用一个短暂 toast/标题提示当前主题名（ticktick/dante/light），或把按钮换成下拉显式选择。

### 10. 挂件分区可发现性
- 横向 tab 两端加可点的左右箭头，或首次进入时短暂自动滚动暗示后面还有分区。

### 11. 两端分区一致性
- 统一 web 与挂件的分区命名与顺序（以一端为准对齐），减少心智切换。这是低风险纯展示调整。

## 验证方式
- Web: `npm run dev` 后手动走查刷新/重试/切档加载态、键盘 Tab、对比度。
- 挂件: `cd desktop && npm run tauri dev`，断开内网验证错误恢复与设置改地址，验证复制、新鲜度显示。
- Rust 改动后确认 `npm run tauri dev` 能编译、`save_config` 写入路径正确。