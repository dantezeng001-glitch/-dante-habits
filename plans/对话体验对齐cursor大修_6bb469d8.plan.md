---
name: 对话体验对齐Cursor大修
overview: 把 Fanbox 对话面板从"会卡死、发不出第二条、回复重复、看不到 agent 在干嘛"修成接近 Cursor IDE 的体验：随时可停止、不锁死、流式不重复、能看到工具步骤、上下文不静默失败。
todos:
  - id: stop
    content: send() 加 AbortController + chat.stop()；index.html 发送键流式期间切「停止」
    status: pending
  - id: no-lock
    content: 流式期间不锁输入 + 单槽排队（_queued），finally 后自动发出
    status: pending
  - id: watchdog
    content: 加无事件看门狗 + 状态条已用时显示
    status: pending
  - id: dedup
    content: server.js chatCursor/chatClaude 按 message.id 只发增量后缀，修流式重复
    status: pending
  - id: toolsteps
    content: server.js 解析 tool_use 发 tool 事件；app.js 渲染工具步骤行 + css
    status: pending
  - id: ctx-empty
    content: dingtalk.sendToAgent 先取 markdown，空则明确提示不静默
    status: pending
  - id: polish
    content: 切后端/开新对话 abort 当前流、清排队、复位按钮 + 错误信息细化
    status: pending
isProject: false
---

# 对话体验对齐 Cursor 的大修

## 根因回顾（已定位）

- 发不出第二条：`send()` 的 `if (this.streaming) return`，而 `streaming` 只在 SSE 收到结束才复位；agent 这一轮卡住 → 永远 true → 发送键永久 disabled，且无停止键。
- 回复重复：`chatCursor` 用 `--stream-partial-output`，前端 `acc += text` 把累积式部分输出叠两遍。
- 正文为空：`甩给对话` 时 markdown 没拉到就静默发了空内容。

## A. 随时可停止（最关键）

- [public/app.js](fanbox-1.11.2/public/app.js) `send()`：给 `fetch` 加 `AbortController`，存到 `this._abort`。
- 新增 `chat.stop()`：`this._abort.abort()`，并立刻复位 `streaming`/按钮。
- [public/index.html](fanbox-1.11.2/public/index.html)：发送键在流式期间变成"停止"（复用 `#chat-send` 切换文案/样式，或加 `#chat-stop`）。
- 后端已有 `res.on('close', () => child.kill())`（[server.js](fanbox-1.11.2/server.js) `chatCursor`/`chatClaude`），所以前端一 abort，服务端会自动杀掉 agent 进程。

## B. 不锁死输入 + 单槽排队

- 流式期间 textarea 保持可输入；`onKeydown` 回车：若在流式中则把这条**排队**（`this._queued`），当前轮 `finally` 结束后自动发出。
- 没排队内容时回车正常发送。

## C. 卡死保护

- `send()` 内加看门狗：每收到一个 SSE 事件刷新计时；超过 N 秒（如 90s）无任何事件，状态条提示"似乎卡住了，点停止重试"，并保证停止键可用。
- 状态条显示已用时（"思考中… 23s"）。

## D. 修流式重复（服务端去重）

- [server.js](fanbox-1.11.2/server.js) `chatCursor`：按 `ev.message.id` 跟踪每条 assistant 已发送的文本长度，`delta` 只发**新增后缀**，不再发累积全文。
- 前端 `acc += text` 保持不变即可（拿到的是纯增量）。`chatClaude` 同口径处理。

## E. 工具步骤可视化（对齐 Cursor）

- [server.js](fanbox-1.11.2/server.js)：解析 stream-json 里的 `tool_use`（assistant content 内）与工具结果，新增 SSE 事件 `tool`，载荷 `{name, target}`（如 Read/Edit/Write/Bash + 文件名）。实现时先用 `--debug` 跑一次确认 cursor-agent / claude 的确切字段名。
- [public/app.js](fanbox-1.11.2/public/app.js) `send()` 加 `else if (ev.event === 'tool')` 分支；在助手气泡内渲染一行紧凑步骤（"读取 X"/"修改 Y"），样式见 [public/style.css](fanbox-1.11.2/public/style.css)。

## F. 上下文不再静默失败

- [public/app.js](fanbox-1.11.2/public/app.js) `dingtalk.sendToAgent`：先 `await` 把 markdown 拉到；为空则 `toast` 明确提示"这篇文档正文没拉到（可能是表格/链接/权限）"，并把 `docUrl` + dws 读取指令一起给 agent，而不是发空。

## G. 收尾打磨

- 错误信息显示具体原因 + 停止后保留已生成内容。
- 开新对话 / 切后端时 abort 当前流、清排队、复位按钮。

## 验证

- 制造一轮长任务：能点停止立即中断、输入解锁、可发第二条。
- 改文件任务：气泡里能看到"修改 X"步骤，最终文本不重复。
- 甩一篇空正文文档：有明确提示，不再静默"正文为空"。