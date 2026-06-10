---
name: desktop-widget-plan
overview: 在现有仓库内新增一个独立的 Tauri 桌面挂件 app(desktop/ 子目录),系统托盘静默常驻 + 桌面悬浮窗直接展示北美日报内容,直连内网接口 http://172.16.199.56:5050/api/digest?ai=1,不做通知,不改动现有后端;借系统 WebView2 输出几 MB 级小 exe。
todos:
  - id: env-setup
    content: 在打包机安装 Rust 工具链 + Tauri CLI(一次性),在 desktop/ 初始化 Tauri v2 骨架(src-tauri + 纯 HTML/JS 前端,无打包器)
    status: in_progress
  - id: window
    content: tauri.conf.json 配置无边框/置顶/透明/可缩放悬浮窗;data-tauri-drag-region 拖动;tauri-plugin-window-state 记忆位置/大小
    status: pending
  - id: tray
    content: 托盘图标与菜单:显示/隐藏挂件、立即刷新、开机自启(tauri-plugin-autostart)、退出;拦截窗口关闭改为隐藏到托盘
    status: pending
  - id: data
    content: 原生侧拉取 /api/digest?ai=1(tauri-plugin-http 或 Rust command,绕开浏览器 CORS),经命令/事件下发前端;tauri-plugin-single-instance 单实例
    status: pending
  - id: renderer
    content: 前端:默认视图为编辑摘要(ai.executiveSummary + executiveBullets),其下分区切换 + 紧凑卡片(zhTitle/source/ageHours/priorityLabel),点击经 opener 打开原文;套用 Dante Shokz 视觉(Ink 深底 + 橙色强调 + 等宽标签 + 直角粗边框)
    status: pending
  - id: states-cache
    content: 加载/失败/降级态 + 启动拉一次、每 60 分钟轮询;离线缓存(plugin-fs 写 appData,断网读缓存并打"数据可能过期"标记);打开外链仅放行 http/https
    status: pending
  - id: package
    content: tauri build 产出 Windows 安装包/exe;config.json 走 resources/appConfig 可改不重打包;另一台 Win11 机器验证双击可用(WebView2 已内置)
    status: pending
isProject: false
---

## 北美日报桌面挂件方案(Tauri)

### 目标与边界
- 形态:系统托盘图标(静默常驻,可开关挂件)+ 桌面悬浮窗(直接显示当天日报内容)。
- 不做桌面通知(避免打扰)。
- 直连已部署内网接口 `http://172.16.199.56:5050/api/digest?ai=1`,无需改后端。
- 运行时 Tauri(Rust 外壳 + 系统 WebView2),输出几 MB 级小 exe;前端用原生 HTML/JS,无打包器。
- 已确认环境:本机 Node 22 在、WebView2 已装(v149)、Rust 待安装(已获授权,仅装在打包机,不影响同事)。
- 视觉沿用 Dante Shokz 设计语言(见下"视觉风格")。壳和样式一起写,不单独出视觉稿。

### 为什么换 Tauri(取舍记录)
- Electron 每个 app 自带整套 Chromium,地板就是 150-200MB,与本挂件功能复杂度不成比例。
- Tauri 借 Win11 内置 WebView2,不背浏览器,exe 约 3-10MB。
- 代价仅在打包机一次性装 Rust;同事侧体验不变(都是双击 exe,零配置)。

### 数据来源(已确认,直接消费)
- 接口:`GET http://172.16.199.56:5050/api/digest?ai=1`(命中当天归档,15 分钟缓存)。
- 分区字段:`social.us`、`social.ca`、`socialTrends.reddit`、`viralStories`、`cultureSignals`、`products`、`marketing`。
- 条目字段(见 [src/App.jsx](src/App.jsx) 的 `ItemCard`):`zhTitle`/`title`、`zhSummary`/`summary`、`source`、`ageHours`、`link`、`priorityLabel`、`tags`、`marketingTip`。
- 顶部信息:`ai.executiveSummary`、`ai.executiveBullets`、`archiveDate`、`nextRefreshBeijing`、`generatedAt`。
- 取数在**原生侧**(http 插件 / Rust command)完成,绕开浏览器 CORS/CSP/混合内容问题。

### 目录结构(新增,不动现有文件)
```text
desktop/
  package.json            前端依赖(@tauri-apps/cli、插件 JS 绑定)与脚本
  src-tauri/
    Cargo.toml            Rust 依赖(tauri + 各插件)
    tauri.conf.json       窗口/托盘/打包/资源配置
    src/main.rs           托盘、单实例、命令、关闭收托盘
    icons/                应用与托盘图标
  src/
    index.html            挂件结构
    widget.css            Dante Shokz 视觉(Ink 深底 + 橙色强调 + 等宽标签 + 直角粗边框)
    widget.js             接收原生下发数据 + 渲染 + 分区切换 + 点击打开原文
  config.json             可改项:apiBaseUrl、刷新间隔、默认显示分区(随 resources 打包,可改不重打包)
```

### 悬浮窗(挂件)行为
- 无边框、置顶(`alwaysOnTop`)、透明背景、可缩放;顶栏用 `data-tauri-drag-region` 拖动;窗口底色用 Ink。
- `tauri-plugin-window-state` 记忆窗口位置与大小。
- 内容:顶部一行显示本期日期 + 下次刷新时间 + 手动刷新按钮;**默认视图为编辑摘要**(`ai.executiveSummary` + `ai.executiveBullets`,最适合扫一眼);其下分区切换(本地热点/消费电子/营销/Reddit/网感/Viral),每区 top N 条紧凑卡片(标题 `zhTitle`,副信息 `source · {ageHours}h 前 · priorityLabel`)。
- 点击条目经 opener 插件在默认浏览器打开原文。
- 加载/失败/降级态:接口失败显示"内网接口不可达"重试条 + 回退离线缓存;`ai.status !== 'ready'` 时顶部提示。

### 健壮性要点
- **原生侧取数**:不在 WebView 里跨域 fetch,避免 CORS/CSP/混合内容。
- **离线缓存(进 v1)**:每次成功写一份到 appData;断网/不可达时读缓存渲染,并打"数据可能过期 · 缓存于 {时间}"标记。
- **单实例**:`tauri-plugin-single-instance`,二次启动只唤起已有挂件。
- **关闭收托盘**:拦截窗口关闭事件改为隐藏,只有托盘"退出"才真正退出。
- **可写配置**:`config.json` 随 resources 打包,改地址不用重打包(必要时支持 appConfig 覆盖)。
- **打开外链硬化**:opener 前校验 `link` 仅为 `http/https`。

### 视觉风格(Dante Shokz 设计语言,适配挂件)
来源单一真源:`~/.cursor/skills/dante-shokz-ppt/references/brand-spec.md`。继承品牌色板/字体/几何规则,但不照搬 PPT 的 1280×720 固定画布与"中文·ENGLISH 页眉 + 页脚页码"。
- 主色:Orange `#FF7A3D`(强调、活跃分区、关键数字)+ Ink `#050505`(挂件底色)。灰阶只用 `#2F2F2F / #666 / #999 / #BABABA / #E5E5E5`,正文近白色;不发明新色,不用渐变,不用紫/蓝/绿作强调。
- 字体:中文 `"Noto Sans SC","Microsoft YaHei","PingFang SC",system-ui`;标签/时效/分区编号/来源用等宽 `Consolas,"Courier New",monospace`。
- 字重只有 400 / 700;不用斜体、不用下划线。
- 几何:全直角矩形,不用 `border-radius`;卡片用顶部 3px 橙色粗条(`border-top:3px solid #FF7A3D`)表示分区色条;分隔线 `#E5E5E5`/`#BABABA`。
- 分区切换做成等宽"中文 · ENGLISH"小标签(如 `本地热点 · LOCAL`、`营销 · CAMPAIGN`),呼应品牌眉头语言。
- 反 slop:不用 emoji 当 icon、不用圆角卡 + 左侧彩条那套 Material 风、不堆动效。

### 刷新策略(无通知)
- 启动时拉一次;之后每 60 分钟轮询一次(数据每天 08:00 BJT 才变,轮询只为兜底跨天);托盘菜单和挂件按钮支持手动刷新。
- 每次成功后写离线缓存;失败时回退缓存并打过期标记。
- 静默更新,不弹任何通知。
- 默认请求 `?ai=1`(不带 `refresh`),命中归档,不会触发 1-3 分钟的 AI 生成。

### 托盘菜单
- 显示 / 隐藏挂件(开关)
- 立即刷新
- 开机自启(`tauri-plugin-autostart`)开关
- 退出

### 打包与分发(内网)
- `tauri build` 产出 Windows 安装包(NSIS/MSI)或免安装 exe,同事双击即用;Win11 已内置 WebView2,无需额外运行时。
- API 基址放 `config.json`,内网地址变化改一个文件即可,不用重打包。

### 验证方式
- 本地 `npm run tauri dev` 启动,确认:挂件出现、原生侧能拉到 `172.16.199.56` 数据、默认进编辑摘要、分区切换正常、点击打开原文、托盘开关与开机自启生效、关闭收托盘、二次启动只唤起一个、关掉重开位置记忆正常。
- 断网/填错 IP:验证回退离线缓存并显示过期标记;恢复网络后自动恢复。
- `npm run tauri build` 产出 exe,在另一台 Win11 机器双击验证,并验证改 `config.json` 地址后无需重打包即生效。
