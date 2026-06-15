---
name: 钉钉文档接入Fanbox
overview: 在 Fanbox 主区新增一块「钉钉」面板：用 Electron webview 嵌入钉钉在线文档(alidocs)做原样查看与编辑，同时用 dws CLI 把文档正文拉成 Markdown，打通终端里的 coding agent（检索知识库 / 接收上下文 / 可选写回）。
todos:
  - id: verify-webview
    content: 开 webviewTag 并验证 Electron webview 能登录+渲染 alidocs.dingtalk.com（方案成立的前提）
    status: pending
  - id: backend-api
    content: server.js 路由表新增 /api/dingtalk/spaces|tree|doc|search，child_process 调 dws 返回 JSON，沿用 /api/chat 模式
    status: completed
  - id: frontend-ui
    content: "index.html 加 topbar「钉钉」按钮 + #dingtalk-panel（左目录树/搜索，右 webview），套用 terminal/chat 面板显隐与 resizer"
    status: completed
  - id: frontend-logic
    content: app.js 新增 dingtalk 模块：loadSpaces/loadTree/openDoc/searchKB，与 term/chat 停靠区互斥
    status: completed
  - id: agent-read
    content: 期一 agent 交互：甩文档正文进终端(term.sendContext) + 知识库检索结果交给 agent
    status: pending
  - id: agent-write
    content: 期二可选：引导 agent 用 dws doc update 写回，强制 --dry-run + 二次确认
    status: pending
isProject: false
---

# 在 Fanbox 中接入钉钉在线文档面板

## 已确认的前提

- 架构走 **hybrid**：webview 嵌 `alidocs.dingtalk.com` 原样查看/编辑 + dws 拉 Markdown 给 agent。
- Fanbox **没有内置 LLM agent**：它的"Agent"是你在内嵌终端（node-pty/xterm）里跑的 Claude Code / Codex。dws CLI 正是为这类 agent 设计的，所以"和 Agent 交互"= 钉钉面板 ↔ 终端 agent，经 dws 打通。
- dws 在本机已装好、已登录（device-flow OAuth，天然每人各自登录），`dws wiki space list` 已实测可返回知识库列表与 `spaceUrl`。

## 我对「Agent 交互」的判断（你让我定的 Q2）

分两期，先安全后强力：

- 期一（读，零风险）：
  - `as_context`：把当前文档正文一键甩进终端，复用 Fanbox 现成的 `term.sendContext(text, srcPath)`（[public/app.js](fanbox-1.11.2/public/app.js) line 2604）。
  - `kb_search`：面板里搜知识库，调 `dws doc search` / `dws wiki`，结果带引用展示并可甩给 agent。这正是"作为线上知识库"的核心诉求。
- 期二（写，加护栏）：
  - `agent_writeback`：让 agent 用 `dws doc update` 改写并写回，强制 `--dry-run` 预览 + 二次确认。

## 关键风险（动手前必须先验证）

- **iframe 大概率不行**：alidocs 很可能设了 `X-Frame-Options`/CSP，普通 `<iframe>` 会被拒。需改用 Electron `<webview>`（`webPreferences.webviewTag=true`）或 `WebContentsView`——它是顶层 webContents，不受 X-Frame-Options 限制。**第一步就要验证 webview 能登录并渲染 alidocs**，验证不过则整个 hybrid 方向要调整。
- **两套登录**：webview 的钉钉网页登录(cookie，存进持久化 partition) + dws CLI 登录(device-flow)。都是"每人各自登录"，但用户要登两次。这是 hybrid 的固有代价，需向使用者说明。
- **平台**：Fanbox 打包目标是 mac arm64 dmg（[package.json](fanbox-1.11.2/package.json) `build.mac`），而你在 Windows。开发模式 `npm run app` 能在 Windows 跑（[electron/main.js](fanbox-1.11.2/electron/main.js) 已处理 win32 PATH/powershell）；要分发 Windows 版需另配 electron-builder win target。
- **dws 前置**：每台机器需装 dws、`dws auth login` 过；企业 admin 需开通 CLI access（dws 当前处于 co-creation 阶段，需授权）。

## 落地步骤

### 1. 验证 webview 加载 alidocs（先做，决定方案成立与否）
- [electron/main.js](fanbox-1.11.2/electron/main.js) `createWindow()` 的 `webPreferences` 加 `webviewTag: true`。
- 临时在 [public/index.html](fanbox-1.11.2/public/index.html) 塞一个 `<webview src="https://alidocs.dingtalk.com/..." partition="persist:dingtalk">`，确认能登录 + 渲染 + 编辑。

### 2. 后端：server.js 新增 dws 接口
在 [server.js](fanbox-1.11.2/server.js) 路由表（line 2128+ 的 `if (p === '/api/...')`）按现有模式新增：
- `/api/dingtalk/spaces` → `dws wiki space list`
- `/api/dingtalk/tree` → `dws wiki node ...`（知识库目录树）
- `/api/dingtalk/doc` → `dws doc read`（拉 Markdown）+ `dws doc info`（取 alidocs url）
- `/api/dingtalk/search` → `dws doc search` / `dws wiki ... search`

用 `child_process`（server.js 顶部已 require `exec/spawn/execFile`）shell 出 dws，`sendJSON` 返回。参照已有的 `/api/chat`、`/api/release/prepare` 处理器写法。

### 3. 前端 UI：新增钉钉面板
- [public/index.html](fanbox-1.11.2/public/index.html)：topbar 加「钉钉」按钮（仿 `#btn-terminal`/`#btn-chat`，line 94-95）；`#main-body` 内加 `<section id="dingtalk-panel">`，左列=知识库树+搜索框，右列=`<webview>` 文档区；复用 `#terminal-resizer` 同款 resizer。
- 套用 `#terminal-panel`/`#chat-panel` 的显隐与停靠互斥逻辑。

### 4. 前端逻辑：app.js 加 dingtalk 模块
在 [public/app.js](fanbox-1.11.2/public/app.js) 加 `dingtalk` 对象：`toggle/open/close`、`loadSpaces()`、`loadTree()`、`openDoc(doc)`（设 `webview.src = doc.url`，并 fetch `/api/dingtalk/doc` 缓存 Markdown）、`searchKB()`。与 `term`/`chat` 共用停靠区，互斥显示（参照 line 2051/2055 的 toggle 绑定与 line 2502-2510 的互斥处理）。

### 5. 接 Agent（期一）
- 面板加「甩给 Agent」按钮 → `term.sendContext(markdown, docTitle)`。
- 「问知识库」→ 调 `/api/dingtalk/search`，把结果+引用甩进终端或在面板展示。

### 6. Agent 写回（期二，可选）
- 面板「让 Agent 改写」→ 在终端引导 agent 调 `dws doc update`，强制 `--dry-run` 预览 + 二次确认后执行。

## 验收标准
- 面板内能登录钉钉、浏览知识库目录树、打开文档原样查看/编辑。
- 能把当前文档（dws 拉的 Markdown）一键甩进终端给 agent。
- 能在面板里检索知识库并把带引用的结果交给 agent。