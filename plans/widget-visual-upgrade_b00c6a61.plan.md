---
name: widget-visual-upgrade
overview: 对桌面挂件做中度视觉重构:按 Fluent/WidgetKit 规范修正材质与对比度(acrylic→mica + 内容 scrim、强调色不压玻璃)、重建字阶与头条焦点、导航改单行横滑分段、统一 SVG 图标与骨架态。仅改前端 + 一处窗口配置,不动 Rust 数据逻辑。
todos:
  - id: material
    content: tauri.conf.json 窗口效果 acrylic→mica;widget.css 分层底(顶栏轻透 + 内容区 scrim)+ 纯色兜底
    status: pending
  - id: contrast
    content: 清理压玻璃的强调色文字,正文近白/墨黑,accent 只上实心 pill/下划线,对比度≥4.5:1
    status: pending
  - id: hierarchy
    content: 字阶 token + 8pt 节奏;“今日要点”加头条焦点 + 次级要点
    status: pending
  - id: nav
    content: 导航改单行横滑分段控件(滚轮转横向 + 边缘渐隐)
    status: pending
  - id: icons-polish
    content: 顶栏换 SVG 图标;加骨架加载态与微交互过渡
    status: pending
  - id: themes
    content: 三套主题按材质规范重调(ticktick/dante/light),accent 只上实心元素
    status: pending
  - id: verify
    content: tauri dev 验证:花哨壁纸可读性、三主题、分段横滑、头条、骨架、拖动顺畅度、离线缓存
    status: pending
isProject: false
---

## 挂件视觉中度重构方案

依据来源:[Apple WidgetKit HIG](https://developer.apple.com/documentation/widgetkit)、[Fluent Acrylic](https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic)、[Fluent Mica](https://learn.microsoft.com/en-us/windows/apps/design/style/mica)、[2026 UI 趋势](https://internalorbit.com/2026/05/ui-ux-design-trends-2026/)、[极简仪表盘原则](https://ui-syntax.com/collections/minimalist-dashboards)。

### 范围与边界
- 改动文件:`desktop/src-tauri/tauri.conf.json`(仅窗口效果一处)、`desktop/src/index.html`、`desktop/src/widget.css`、`desktop/src/widget.js`。
- 不动 Rust(数据契约、托盘、单实例、缓存不变),不动 capabilities。
- 保留三套主题与记忆、缩放/隐藏/拖动、点击开原文等已实现能力。

### 1. 材质与可读性(最高优先,Fluent 规范修正)
- 窗口效果 `acrylic` → `mica`:常驻窗口应用 Mica(壁纸感、性能好、拖动更顺),acrylic 仅适合临时浮层。改 [tauri.conf.json](desktop/src-tauri/tauri.conf.json) 的 `windowEffects.effects`。
- 分层底:顶栏/分段栏轻透,**内容区(文字密集)用更实的 scrim**(近不透明),保证任意壁纸上新闻可读。
- 强调色不再压玻璃:正文用近白(深色主题)/ 墨黑(浅色),钴蓝/橙仅用于实心 pill、激活下划线、小标。目标对比度 ≥ 4.5:1。
- 兜底:关闭透明/高对比时回退纯色底(CSS 近不透明值即兜底)。运行时 Mica 不支持也能看。

### 2. 信息层级与头条焦点(WidgetKit/印刷层级)
- 字阶 token:`11 / 12.5 / 14 / 18 / 22`,字重仅 400/700。
- 默认"今日要点"视图加**头条焦点**:取最高信号一条放大(18-22pt)+ 来源/时效,其下 3-4 条次级要点/标题,形成一眼可见的视觉重心。
- 8pt 间距节奏,卡片留白统一。
- 渐进披露:要点给精华 → 点分区看明细 → 点条目开原文。

### 3. 导航重做:单行横滑分段控件
- 把现在换行的 `.tabs` 换成**单行不换行**的分段栏,支持滚轮转横向滚动 + 两侧渐隐提示。
- 顺序:`今日要点` 起手,后接 本地热点/消费电子/营销/Reddit/网感/Viral。
- 激活态:实心或下划线 accent(不靠彩色文字)。

### 4. 图标与打磨
- 顶栏 `◑ ⟳ ⤢ —` 换成统一内联 **SVG 图标**(Lucide 风格,`currentColor`,~14px):主题/刷新/缩放/隐藏。
- 微交互:hover/active 120-150ms 过渡,克制。
- **骨架态**:加载时显示 shimmer 占位块(替代纯文字"正在读取")。
- 失败/过期态视觉打磨(沿用现有 banner 文案逻辑)。

### 5. 三套主题按材质规范重调
- `ticktick`(默认):Mica + 内容 scrim,钴蓝 `#4772FA` 只上实心元素;青 `#93dde5` 作次强调小点。
- `dante`:Ink 实底 + 橙,直角(已够实),同步套用头条焦点与字阶。
- `light`:更实的浅色面,蓝色强调只上实心元素。

### 验证方式
- `npm run tauri dev` 后逐项确认:在"花哨壁纸"上正文是否清晰可读(对比度);三套主题切换正常;分段栏单行横滑/滚轮;头条焦点渲染;骨架态出现;拖动是否比 acrylic 更顺(Mica);缩放两档生效。
- 断网验证离线缓存 + 过期标记仍正常。
- 若运行时 Mica 不生效,确认纯色 scrim 兜底观感可接受。

### 不做(避免过度设计)
- 不做壁纸自适应取色/动态对比算法(成本高,先用固定 scrim 保证可读)。
- 不做自动更新服务、不加更多主题。