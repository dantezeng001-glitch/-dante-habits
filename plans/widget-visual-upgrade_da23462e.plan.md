---
name: widget-visual-upgrade
overview: 对桌面挂件做一次系统性视觉升级:玻璃质感、扫读性(来源字母色块+等高卡片)、字体与间距令牌、微动效与加载骨架屏,并让磨砂效果(Acrylic/Blur/Mica/关闭)可在托盘切换。沿用现有 Tauri 架构与三主题,不改后端、不改数据契约。
todos:
  - id: tokens-type
    content: widget.css 加间距令牌 + UI/内容字体角色分离 + 标题/摘要字号行高按基准调
    status: completed
  - id: glass-craft
    content: 三主题玻璃质感:顶部高光描边 + 柔阴影 + 圆角 + 层次(dante 保持直角/近不透明)
    status: completed
  - id: scannability
    content: 来源字母色块 monogram(hash 配色、零网络)+ 等高卡片(标题/摘要 2 行截断)+ 日期加粗/来源小字
    status: completed
  - id: nav-singlerow
    content: 顶栏分区 tab 改单行横滚 + 隐藏滚动条 + active scrollIntoView,消除换行抖动
    status: completed
  - id: microanim-skeleton
    content: hover/切换微动效(纯 CSS、滚动不动) + 首屏 shimmer 骨架屏
    status: completed
  - id: glass-effect-select
    content: 托盘子菜单选 Acrylic/Blur/Mica/关闭,Rust set_effects 实时应用 + 持久化读取
    status: completed
  - id: footer-link-autostart
    content: 页脚左加"打开完整网页"链接(opener 打开 apiBaseUrl)、右加"开机启动"开关(Rust get/set_autostart,与托盘同步)
    status: completed
  - id: verify
    content: dev 验证:三主题/四磨砂态/单行滚动/等高卡片/骨架屏/微动效 + 原功能回归,无报错
    status: completed
isProject: false
---

## 挂件视觉升级方案(基于先进案例)

参考依据:Rainmeter Frosted Glass(玻璃质感 + 编辑式排版 + 微动效 + 效果可调)、NetNewsWire/Reeder/Inoreader(可扫读性、来源图标、固定单行顶栏、单列、克制层级、滚动不加动效)。

目标文件全部在 `desktop/`,不动后端,不改 `load_digest` 数据契约。

### 1. 设计令牌 + 字体角色分离
改 [desktop/src/widget.css](desktop/src/widget.css):
- 间距 scale 令牌 `--s1..--s4 = 4/8/12/16`,所有 padding/margin 走令牌,统一节奏。
- 字体两套角色:UI 标签字体(分区/日期/来源/状态,等宽或 system-ui)与内容字体(标题/摘要,system-ui 优化)分离。
- 标题 13px/行高 1.35、摘要 11.5px/行高 1.5(贴近阅读基准并适配挂件密度);字重只用 400/700。

### 2. 玻璃质感(三主题分别调)
改 [desktop/src/widget.css](desktop/src/widget.css):
- `.widget` 增加 1px 顶部高光描边(`rgba(255,255,255,.18)`)+ 整体细边 + 柔阴影 `0 12px 40px rgba(0,0,0,.35)` + `border-radius:12px`;非 dante 主题加极弱顶部高光过渡,做出"高级玻璃"层次。
- ticktick/light 用半透明 bg 透出壁纸;dante 维持近不透明 Ink + 直角(品牌锁不变)。

### 3. 扫读性:来源字母色块 + 等高卡片
改 [desktop/src/widget.js](desktop/src/widget.js) 与 [desktop/src/widget.css](desktop/src/widget.css):
- 每条卡片左侧加 18x18 来源 monogram 色块:取来源名首字母,颜色由来源名 hash 决定(确定性、零网络)。替代纯文字找出处。
- 卡片等高化:标题 `-webkit-line-clamp:2`、摘要 `:2` 截断,统一内边距,卡片视觉等高更利扫读。
- 日期加粗独立、来源小字,层级清晰(参考 NetNewsWire timeline)。

### 4. 顶栏分区收成单行(消除抖动)
改 [desktop/src/index.html](desktop/src/index.html) + css:
- 7 个分区 tab 从换行改为**单行横向滚动**(`flex-nowrap` + `overflow-x:auto` + 隐藏滚动条 + 两侧渐隐),切换时 active tab `scrollIntoView`;顶栏固定不随内容滚动抖动。

### 5. 微动效 + 加载骨架屏
改 css + [desktop/src/widget.js](desktop/src/widget.js):
- hover/active 过渡 120-150ms(卡片轻微上浮 + 提亮,按钮/标签状态过渡),主题切换背景/文字 crossfade;**滚动不加任何动效**(避免干扰)。
- 首次加载渲染 4-5 张 shimmer 骨架卡(CSS keyframes,一次性),替代"正在读取"纯文字。

### 6. 磨砂效果可选(Acrylic/Blur/Mica/关闭)
改 [desktop/src-tauri/src/lib.rs](desktop/src-tauri/src/lib.rs)、[desktop/src-tauri/capabilities/default.json](desktop/src-tauri/capabilities/default.json)、[desktop/src-tauri/tauri.conf.json](desktop/src-tauri/tauri.conf.json):
- 托盘新增"磨砂效果"子菜单:Acrylic / Blur / Mica / 关闭;选择后 Rust 调 `window.set_effects(...)` 实时应用,并持久化到 appData 的 settings.json,启动时读取套用。
- 保留 `tauri.conf.json` 的 acrylic 作为默认初值。

### 7. 底部页脚:本地网页链接 + 开机启动开关
改 [desktop/src/index.html](desktop/src/index.html)、[desktop/src/widget.js](desktop/src/widget.js)、[desktop/src-tauri/src/lib.rs](desktop/src-tauri/src/lib.rs)、[desktop/src-tauri/capabilities/default.json](desktop/src-tauri/capabilities/default.json):
- 页脚(现 statusbar)重构为左右两区:
  - 左:"打开完整网页"链接,点击经 opener 打开 `config.apiBaseUrl`(即 `http://172.16.199.56:5050/`),仅放行 http/https。
  - 右:"开机启动"开关(pill/checkbox),反映系统真实自启状态,点击切换。
- 自启状态用 Rust 命令暴露给前端,避免依赖插件全局 JS:
  - `get_autostart() -> bool`、`set_autostart(enabled: bool)`,内部用 `app.autolaunch().is_enabled()/enable()/disable()`。
  - `invoke_handler` 注册这两个命令;启动时前端读取一次同步开关 UI。
- 托盘"开机自启"菜单保留,与页脚开关同源(都走 autolaunch),状态一致。

### 不做(避免过度设计)
- 不联网拉 favicon(改本地字母色块)。
- 不新增第三方动画库(纯 CSS)。
- 不改后端、不改数据结构、不动 dante 的品牌直角/橙色锁。

### 验证
- `npm run tauri dev` 跑通:三主题切换、磨砂四态切换实时生效、单行 tab 横滚不抖、卡片等高 + monogram、骨架屏首屏、hover 微动效;页脚"打开完整网页"能在浏览器打开内网站点、"开机启动"开关与系统真实状态一致且可切换(与托盘同步);原有拖动/缩放/隐藏/刷新/离线缓存功能回归正常,无编译/运行报错。