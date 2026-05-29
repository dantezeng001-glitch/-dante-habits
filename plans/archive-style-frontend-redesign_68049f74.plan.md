---
name: archive-style-frontend-redesign
overview: 把知识库前端从"通用 SaaS 蓝"改造成"编辑部档案馆"风格：移除 AI slop 视觉痕迹（双 radial gradient、22px 大圆角、漂浮阴影、装饰圆球、负字距），引入 Google Fonts 思源宋体 + 思源黑体的中文双字体方案，重写颜色 token 为米白底 + 深墨 + 朱砂 accent，并按档案馆调性重做 hero、卡片、章节分隔的视觉语言。
todos:
  - id: fonts
    content: index.html 加 Google Fonts preconnect 与 Noto Serif SC / Noto Sans SC / Fraunces / Inter 的 link
    status: completed
  - id: tokens
    content: app.css 重写 :root：颜色 token、radius=4px、shadow 近于无、新增 --font-display / --font-body
    status: completed
  - id: background
    content: 删除 body 双层 radial-gradient，换为米白底 + 细噪点网格
    status: completed
  - id: panel
    content: panel 改 hairline border + 删除阳影；h2 加粗横线底部
    status: completed
  - id: cards
    content: 各类卡片删渐变、hover 取消浮起、改边框变色 + 底色切换
    status: completed
  - id: hero
    content: app.js 里 renderHome 重构 hero：单列、刷头小字、stats 拆为独立 stats-strip
    status: completed
  - id: hero_css
    content: app.css 的 .home-hero 删装饰圆、删渐变、加顶部朱砂横条和右上 ARCHIVE 标记
    status: completed
  - id: nav_badge
    content: primary-nav 胶囊改下划线激活态；badge 改 1px border 票根样式
    status: completed
  - id: typography
    content: 清理所有 letter-spacing 负值；line-height 统一为 1.7/1.85/1.25 三档
    status: completed
  - id: doc_page
    content: doc-hero 改为与首页一致的顶部朱砂条；markdown-body 加窄栏 max-width 与宋体 italic blockquote
    status: completed
  - id: verify
    content: 人工目检首页 / 浏览页 / 详情页三个关键场景
    status: completed
isProject: false
---

## 范围与边界

**改 3 个文件**：

- [前端开发/static/index.html](前端开发/static/index.html)：加 Google Fonts preconnect + link
- [前端开发/static/app.css](前端开发/static/app.css)：颜色 token 重写、字体、装饰元素移除、卡片/章节视觉语言重做
- [前端开发/static/app.js](前端开发/static/app.js)：替换 hero 区那个无信息装饰圆为有内容承担的元素；调整 `renderDocCard` / hero 的标签语义结构以配合新视觉

**不改**：路由、API、数据流、`server.py`、`kb_backend.py`、测试。

---

## 一、字体方案（Google Fonts CDN）

`index.html` `<head>` 加：

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Noto+Sans+SC:wght@400;500;700&family=Fraunces:opsz,wght@9..144,500;9..144,700;9..144,900&family=Inter:wght@400;500;600&display=swap"
  rel="stylesheet"
/>
```

字体分工（`app.css`）：

- `--font-display: "Fraunces", "Noto Serif SC", "Songti SC", serif;` — h1/h2/hero 大标题，西文配中文宋体的呼吸感
- `--font-body: "Inter", "Noto Sans SC", "PingFang SC", sans-serif;` — 正文、卡片标题、按钮
- `--font-mono: "Cascadia Mono", Consolas, monospace;` — 保留原值，code 块

`body` 默认 `font-family: var(--font-body)`；所有 `h1, h2, .hero-copy h2, .doc-toolbar h2` 切到 `var(--font-display)`，字重 700，`**letter-spacing: 0**`（删掉所有 `-0.02em` / `-0.04em` 负字距）。

---

## 二、颜色与背景重写（`:root`）

把当前 token 整体替换为档案馆配色：

```css
:root {
  color-scheme: light;
  --bg: #f5f1e8;            /* 米白底，原 #eef4ff */
  --panel: #fbf8f1;         /* 卡片底，比页面略浅一点 */
  --panel-alt: #efe9da;     /* 嵌套区底色 */
  --text: #1a1a1a;          /* 深墨，原 #121a2c */
  --muted: #6b6358;         /* 暖灰，原冷灰 #637089 */
  --line: #d8cfb8;          /* 米色描边，原冷蓝 #dfe7f5 */
  --brand: #b8451f;         /* 朱砂，原蓝 #2557f6 */
  --brand-soft: rgba(184, 69, 31, 0.08);
  --brand-strong: #8f3315;
  --accent: #2c4a3a;        /* 墨绿，原绿 #0e9f7a */
  --danger: #a02818;
  --warning: #8a6300;
  --shadow: none;           /* 改用 hairline border 划层级，不要漂浮阴影 */
  --shadow-soft: 0 1px 2px rgba(26, 26, 26, 0.04);
  --radius: 4px;            /* 原 22px，改成档案票根式直角微圆 */
}
```

`**body` 背景删掉两层 radial-gradient**，只保留 `var(--bg)` + 一层细噪点：

```css
body {
  background: var(--bg);
  background-image:
    radial-gradient(circle at 1px 1px, rgba(26, 26, 26, 0.04) 1px, transparent 0);
  background-size: 24px 24px;
}
```

噪点网格让米白底有"纸张纹"质感，但不会喧宾夺主。

---

## 三、卡片、面板视觉语言重做

档案馆风格的核心：**hairline border + 章节标题用粗横线压制 + 不要漂浮卡片**。

### `.panel`

- 删 `box-shadow: var(--shadow)`
- 改为 `border: 1px solid var(--line)`，`border-radius: var(--radius)`（即 4px）
- `padding: 28px 32px`（原 22px，加大留白让内容透气）

### `.summary-card / .stat-card / .doc-card / .source-card`

- 删 `linear-gradient(180deg, #ffffff, var(--panel-alt))` 渐变底
- 改纯色 `background: var(--panel)`
- `border-radius: var(--radius)`（4px）
- `:hover` 删掉 `transform: translateY(-2px)` 和 `box-shadow`，改成 `border-color: var(--brand)` + `background: var(--panel-alt)` 的"按下感"，更工具/档案

### `.panel h2`（章节标题）

新增章节标题视觉锚点：

```css
.panel h2 {
  font-family: var(--font-display);
  font-size: clamp(22px, 2.4vw, 28px);
  font-weight: 700;
  letter-spacing: 0;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--text);
  margin-bottom: 20px;
}
```

整份页面靠这条**深墨粗横线**而不是卡片浮起来，承担"章节起点"的视觉信号。

---

## 四、hero 区重做

### 当前问题

- `.home-hero::after` 那个 260×260 的浅蓝装饰圆（[app.css:348-358](前端开发/static/app.css)）删掉
- `.home-hero` 的 `linear-gradient(135deg, rgba(37, 87, 246, 0.1), rgba(14, 159, 122, 0.08))` 删掉
- 改成米白底 + 顶部一条 4px 朱砂横条作为"档案封面"标记

### 新 hero 视觉

```css
.home-hero {
  position: relative;
  background: var(--panel);
  border-top: 4px solid var(--brand);
  padding-top: 36px;
}

.home-hero::before {
  content: "ARCHIVE / 知识档案";
  position: absolute;
  top: 12px;
  right: 32px;
  font-family: var(--font-body);
  font-size: 11px;
  letter-spacing: 0.18em;
  color: var(--muted);
}
```

### hero 内容增强（动 `app.js`）

[前端开发/static/app.js:307-329](前端开发/static/app.js) 这段 `home-hero` 的模板字符串里：

- 删 `<div class="hero-grid">` 那两个 stat-card（"知识页总数" / "知识区数量"）从 hero 内挪到 hero **下方的独立条带**作为"档案统计"
- hero 区只留标题 + 副标题 + 两个按钮，让首屏标题有压迫感
- 新增一行"档案出品信息"小字，类似杂志刊头："Vol. 01 · 更新于 ${最新更新日期} · 共收录 ${totalDocuments} 篇"

新 hero 内容大致：

```html
<section class="panel home-hero">
  <div class="hero-copy">
    <p class="eyebrow">Knowledge Archive · 知识档案</p>
    <h2>从一个入口查找、阅读和追溯知识资产</h2>
    <p class="subtle">聚合产品主张、策略判断、概念原理与来源材料。</p>
    <p class="hero-meta">Vol. 01 · 共收录 ${total} 篇 · 最新更新 ${latestDate}</p>
    <div class="toolbar-actions">
      <a class="primary-button" href="...">开始浏览</a>
      <a class="secondary-button" href="...">搜索知识库</a>
    </div>
  </div>
</section>

<section class="panel stats-strip">
  <!-- 原 hero 里的两个 stat-card 挪到这里，作为独立的统计条带 -->
</section>
```

`.home-hero` 改回单列布局（删 `grid-template-columns: minmax(0, 1.35fr) minmax(280px, 0.65fr)`）。

---

## 五、按钮与导航微调

### `.search-form button / .primary-button`

- 删 `:hover` 的 `box-shadow: 0 10px 22px rgba(...)` 漂浮阴影
- 改为 `:hover { background: var(--brand-strong); }`，干净直接

### `.primary-nav a`

- 当前用 `border-radius: 999px` 胶囊状——胶囊偏消费 App
- 改为 `border-radius: 0`，下边框作为激活态：`border-bottom: 2px solid transparent` → `is-active` 时 `border-bottom-color: var(--brand)`
- 这是经典编辑部 tab 视觉

### `.badge`

- 当前 `border-radius: 999px` 也偏甜
- 改为 `border-radius: 2px`，加一层 1px border：`border: 1px solid currentColor; background: transparent;`
- 视觉变成"档案标签贴纸"，而不是消费 App 彩色徽章

---

## 六、行距、字距系统统一

建立 4px 步进基数：

```css
body { line-height: 1.7; }                /* 原 1.6 */
.markdown-body { line-height: 1.85; }     /* 原 1.75，长文阅读 */
h1, h2 { line-height: 1.25; }             /* 原 1.18 / 1.2，统一 */
.hero-copy h2 { line-height: 1.15; font-size: clamp(34px, 4.5vw, 56px); }
```

**所有 `letter-spacing: -0.02em` / `-0.04em` 全部改为 `0` 或删除**——中文不需要负字距。

---

## 七、详情页（`renderDocument`）适配

[前端开发/static/app.js:563-595](前端开发/static/app.js) 的 `.doc-hero`：

- 当前 `background: linear-gradient(135deg, rgba(37, 87, 246, 0.08), transparent 58%), #ffffff` 改为纯 `var(--panel)` + `border-top: 4px solid var(--brand)`，跟首页 hero 视觉系统统一
- 面包屑 `.breadcrumbs` 字体切到 `var(--font-body)`，字号收到 13px，颜色用 `var(--muted)`

`.markdown-body` 的阅读体验是这次改造里最该被"档案馆化"的地方：

- 加 `max-width: 720px; margin: 0 auto;` 让长文阅读宽度受控（窄栏阅读是编辑部基本功）
- `font-family: var(--font-body)`，但 h1-h4 切到 `var(--font-display)`
- `blockquote` 当前左边一条 4px 蓝竖条 + 浅蓝底，改为左边 2px 深墨竖条 + 透明底，配宋体 italic：

```css
.markdown-body blockquote {
  border-left: 2px solid var(--text);
  background: transparent;
  font-family: var(--font-display);
  font-style: italic;
  color: var(--text);
  padding: 4px 0 4px 20px;
}
```

---

## 八、改动清单（按文件）

### `index.html`

- `<head>` 新增 Google Fonts preconnect + 字体 link（位置：`<title>` 之后、`<link rel="stylesheet">` 之前）
- 其余结构不动

### `app.css`

- `:root` token 整体重写（颜色 + radius + shadow + 新增字体变量）
- `body` 背景改纯色 + 噪点网格
- `.panel` 改 hairline border、删阴影、章节标题加粗横线
- `.summary-card / .stat-card / .doc-card / .source-card` 删渐变、改纯色、改 hover
- `.home-hero` 删装饰圆和渐变、单列、加顶部朱砂条 + 右上 ARCHIVE 标记
- `.primary-nav` 胶囊改下划线
- `.badge` 改 1px border 票根样式
- 所有 `letter-spacing` 负值删除/置 0
- `.markdown-body` 加窄栏 max-width、blockquote 改宋体 italic
- 按钮 hover 删阴影
- 新增 `.hero-meta`、`.stats-strip` 样式

### `app.js`

- `renderHome` 里 hero 区拆成 hero（标题+副标题+按钮+刊头小字）+ stats-strip 两段（[前端开发/static/app.js:306-329](前端开发/static/app.js)）
- `renderHome` 里增加从 `state.overview` 取 `latestUpdate` / `totalDocuments` 用于刊头小字
- 其他 render 函数不动

---

## 九、验证

改完后人工目检三件事：

1. 首页打开：hero 顶部一条朱砂线、右上"ARCHIVE / 知识档案"小字、宋体大标题、米白底有细噪点
2. 浏览页：卡片是 hairline 描边的纯色块、hover 不再浮起、章节标题下有粗横线
3. 详情页：长文阅读窄栏、blockquote 是宋体斜体、面包屑朴素

如目检发现某些密集列表（比如评论区）在新颜色下对比度不足，**单点 patch**，不全局回退方向。