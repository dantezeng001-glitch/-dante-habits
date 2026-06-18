---
name: FanBox 下一步行动
overview: 基于上次 Claude 会话的实际落地情况，梳理已完成项、遗留问题和可系统性推进的改进方向。
todos:
  - id: rebuild-copilot-bundle
    content: 跑 npm run build:copilot 重编译 vendor-server/copilot.cjs，让知识库模板清理生效（当前 bundle 仍内嵌 Shokz 旧数据）
    status: completed
  - id: check-stat-api
    content: 确认 /api/stat 端点返回 isDir 字段，确保会话恢复时目录和文件的处理逻辑正确
    status: completed
  - id: verify-changes
    content: 在开发环境运行 FanBox，验证会话恢复、行号定位、配置备份恢复三个新功能是否正常工作
    status: completed
  - id: windows-packaging
    content: 评估 Windows 打包可行性：添加 dist:win 脚本，处理 node-pty 编译依赖
    status: completed
  - id: copilot-integration
    content: 理清 copilot-src TypeScript 模块的编译和运行路径，确认校对功能 UI 是否已接通
    status: completed
isProject: false
---

# FanBox 下一步行动方案

## 上次会话实际落地情况

上次 Claude 会话虽然频繁报错（`app.js` 的字符串匹配反复失败），但核心改动 **全部成功写入** 了：

| 改动 | 涉及文件 | 状态 |
|---|---|---|
| 会话状态持久化（重开恢复目录/文件/终端） | `main.js` `preload.js` `app.js` | 已落地，IPC 三件套 + 防抖保存 + 恢复逻辑完整 |
| 在编辑器打开到当前行 | `server.js` `app.js` | 已落地，`code -g file:line` |
| 配置自动备份 + 损坏恢复 | `server.js` | 已落地，10 份轮转备份 |
| 知识库模板脱敏 | `knowledge-base.json` | 已落地，Shokz 内容替换为通用模板 |
| README 对齐 | `README.md` | 已包含会话恢复和行号定位的描述 |

**结论：上次会话的源文件改动已经完成。** 但探查发现一个遗漏：运行时 bundle 未重编译。

---

## 当前需要做的事（按顺序）

### 0. 重编译 copilot bundle（阻塞项）

`copilot-src/data/knowledge-base.json` 已清理为通用模板，但 `server.js` 实际 `require` 的是 `vendor-server/copilot.cjs`——这个 bundle 的 mtime 是 6 月 15 日，仍然内嵌 Shokz 旧知识库（`brand: "Shokz 韶音"`、`Shokzstar Program` 等）。

**修复**：跑 `npm run build:copilot`，让 `vendor-server/copilot.cjs` 从最新源文件重新生成。

### 1. 确认 `/api/stat` 端点返回 `isDir`

[`server.js:2396`](fanbox-1.11.2/server.js) 的 `/api/stat` 端点、[`app.js:4542`](fanbox-1.11.2/public/app.js) 的 `statPath` 函数——会话恢复逻辑依赖 `st.isDir` 判断是导航到目录还是打开文件预览。需要读代码确认返回值结构。

### 2. 验证上次改动能跑

上次改动跨 4 个文件，没有经过运行验证：

- `npm run app` 启动，检查：
  - 打开一个项目目录 → 选中文件 → 开终端 → 关闭 app → 重开，看是否恢复
  - 编辑代码文件 → 点"在编辑器打开" → 看 VS Code 是否跳到对应行
  - 故意损坏 `~/.fanbox/config.json` → 重启 → 看是否从备份恢复
- 如果出错，根据报错修复

---

## 后续可系统性推进的方向（按价值排序）

### A. 跨平台打包（Windows / Linux）

README 明确写了"当前仅 macOS Apple Silicon"，但你的开发环境是 **Windows**（`win32 10.0.26200`）。代码里的路径处理和 `openInOS` 已经有 Windows 分支，但 `electron-builder` 只配了 `--mac`。

- 在 `package.json` 加 `"dist:win": "electron-builder --win"` 脚本
- 处理 `node-pty` 在 Windows 上的编译（需要 VS Build Tools）
- 测试 `fs.watch`、终端 CWD 追踪等在 Windows 上的行为

### B. `copilot-src` TypeScript 模块的集成路径

`copilot-src/` 下有完整的校对引擎（`proofread/`）、文档提取（`documents/`）、知识库管理（`kb/`），全部 TypeScript 编写。但 `package.json` 的 build 脚本只有 `"build:copilot": "node scripts/build-copilot.mjs"`。

需要确认：
- 这些 TypeScript 模块是编译后在 Electron 中运行，还是有独立的运行方式？
- 校对功能的 UI 入口在 `app.js` 的哪里？是否已接通？

### C. 本地模型集成（已实验但暂停）

[`experiments/local-model-202606/`](fanbox-1.11.2/experiments/local-model-202606/README.md) 的结论：
- VLM 截图打标：不可用（太慢）
- md 语义关联 + recall：可用但暂不集成

如果要恢复这条线，按实验文档建议：先换运行时（MLX-VLM / vllm-mlx），再考虑集成。

### D. 工程质量提升

- `app.js` 单文件 ~4900 行，是维护的最大瓶颈。但作者有意保持"零 build"前端，模块化需要权衡。
- 没有自动化测试。`experiments/bugfix-202606/verify.js` 只是一次性验证脚本。
- 没有 linter / formatter 配置。

### E. 用户体验细节

- **终端 WebGL 在 Windows 上的表现**：CJK 残影问题，README 提到了 `fbWebgl(false)` 诊断开关
- **AI 对话窗后端切换**：支持 Cursor / Codex / OpenAI 兼容 API，但配置入口是否足够清晰？
- **磁盘占用透视**的性能——大目录 `du` 扫描是否会卡 UI？
