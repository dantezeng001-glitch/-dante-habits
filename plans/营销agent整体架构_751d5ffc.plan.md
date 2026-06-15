---
name: 营销Agent整体架构
overview: 把现有的文案润色、Excel校对两个独立 demo，加上待建的知识库，收敛成一个以"统一知识库"为大脑、Cursor agent 窗口式外壳（对话为主 + 保留专用界面）的本地一体化营销 Agent 工具，三个功能成为 agent 可调用的工具。
todos:
  - id: kb-schema
    content: 阶段0:定义统一知识库 schema,把 brand-facts/style-palette/fewshot 与校对的 standard/dimensions 合并为单一事实源,作为 agent 的上下文层,两个工具改读共享源
    status: completed
  - id: shell
    content: 阶段1:搭建 Cursor agent 窗口式外壳(对话侧栏 + 结果画布 + 知识库上下文栏 + @引用 + 模型/档位选择),把文案润色封装为第一个 agent 工具并保留其左右分栏专用界面
    status: completed
  - id: proof-migrate
    content: 阶段2:把校对的 Excel 解析/配对/报告逻辑从 Python 迁移到 TS,封装为第二个 agent 工具,并保留三步向导专用界面
    status: completed
  - id: kb-ui
    content: 阶段2:做知识库可视化管理界面(术语/腔调/合规/风格/标准/模板的增删改查),支持对话中 @引用
    status: completed
  - id: doc-fill
    content: 阶段3:基于知识库+模板的文档自动填写,封装为第三个 agent 工具
    status: completed
  - id: agent-orchestration
    content: 阶段4(未来):多步任务编排(检索→生成→校对→报告)做稳,知识库后端化与共享账号
    status: completed
isProject: false
---

## 核心判断

知识库不是第三个并列功能，是整个软件的**大脑**。现在两个工具各自维护散落的知识：

- `文案副驾` 有 [brand-facts.json](翻译及美化/copywrite 前端/data/brand-facts.json)（腔调卡 / 术语 / 合规违禁词）、`style-palette.json`、`fewshot.json`
- `校对工具` 有"三方书写标准"和"术语/格式/语气/法务"维度（[校对/proofreader/standard.py](校对/proofreader/standard.py)、`rules.py`）

这两份本质是同一类知识，应收敛成**一份单一事实源**，被三个模块共同消费：文案生成、校对依据、文档自动填写。

## 目标形态：Cursor agent 窗口式外壳（双入口）

本地桌面应用（小团队内部分发）。主交互是一个 Cursor agent 窗口：对话为主，agent 调用工具，结果在主画布渲染；同时保留每个功能的专用结构化界面，可直接打开（像 Cursor 既能聊天也能直接编辑文件）。三个功能从"独立模块"变成 agent 可调用的工具，知识库是 agent 的上下文层。

映射到 Cursor 的形态：

- 对话侧栏 → 营销任务对话（自然语言驱动）
- 编辑器主区 → 结果画布：文案版本卡 / 校对差异表 / 填好的文档，可直接编辑
- @ 引用上下文 → @ 知识库条目 / @ 上传素材
- 工具调用（编辑/搜索） → 工具调用（润色 / 校对 / 填写 / 查改知识库）
- 模式 + 模型选择 → 标准/专家档、provider 无关模型
- 直接打开文件 → 直接打开文案左右分栏、校对三步向导等专用界面

## 架构蓝图

```mermaid
flowchart TD
    subgraph shell [Cursor agent 窗口式外壳]
        chat[对话侧栏<br/>自然语言驱动]
        canvas[结果画布<br/>版本卡/差异表/文档]
        ctx[知识库上下文栏<br/>@引用]
        panes[专用界面<br/>文案分栏/校对向导]
    end
    agent{{Agent 编排<br/>工具调用 + 多步}}
    subgraph tools [Agent 可调用工具]
        copy[润色文案]
        proof[校对 Excel]
        fill[填写文档]
        kbtool[查改知识库]
    end
    kb[(统一知识库<br/>本地 JSON/SQLite)]
    llm[LLM 客户端<br/>provider 无关]
    chat --> agent
    panes -.直接调用.-> tools
    agent --> tools
    tools --> canvas
    copy --> kb
    proof --> kb
    fill --> kb
    kbtool --> kb
    ctx --> kb
    agent --> llm
    tools --> llm
```

每个功能做成既能被 agent 在对话里调用，也能从专用界面直接用的**同一套工具核心**：工具逻辑与界面分离，对话和专用界面共享底层实现。



## 关键技术决策（需你拍板）

- **统一技术栈**：推荐以 `文案副驾` 的 Next.js + TS + Electron 为壳。`校对` 的 Python 逻辑（Excel 解析 / 配对 / 报告）迁移到 TS——`文案` 项目已含 `xlsx` 依赖，提示词与 LLM 调用也已有 TS 版（`lib/llm.ts`、`lib/prompt.ts`），迁移工作量有界。备选：短期把 Python 当 sidecar 由 Electron 拉起，但会让打包带两个运行时，不推荐长期保留。
- **知识库存储**：先用版本化 JSON（沿用现有模式），实体变多（多品牌/多产品/模板库）后迁 SQLite。放在固定 app-data 目录；"共享"可先用 OneDrive 同步该目录顶替服务端。
- **密钥**：现状是把 API Key 打进安装包（README 自述可被提取）。小团队内部可接受，但应改为首启在设置里填、存本地，不进前端 JS。
- **"Agent"落在外壳本身**：采用 Cursor agent 窗口形态后，编排层不再是后期才加的东西，而是阶段 1 的外壳骨架。现有单次 LLM 调用先封装成"工具"，对话里能调用即可；多步链式编排（检索→生成→校对→报告做稳、可中断可重试）留到阶段 4 打磨。
- **工具核心与界面分离**：每个功能拆成"工具核心（纯逻辑）+ 专用界面 + agent 工具描述"。对话调用和直接打开专用界面复用同一套核心，避免两套实现。

## 知识库 schema（收敛草案）

合并现有字段 + 新增：`brand` / `toneCard` / `terminology[]` / `compliance{bannedPhrases,healthClaimNote}` / `stylePalette[]` / `fewshot[]` / `writingStandards[]`（含术语·格式·语气·法务角色，来自校对）/ `documentTemplates[]`（新增，供文档填写）。

## 分阶段路线图

- **阶段 0｜知识收敛**：定知识库 schema，把两个工具里散落的知识抽进同一份文件作为 agent 上下文层，两个工具改读这份共享源。此阶段不动 UI，先证明"单一事实源"成立。
- **阶段 1｜agent 窗口外壳**：搭 Cursor 式外壳（对话侧栏 + 结果画布 + 知识库上下文栏 + @引用 + 模型/档位选择 + 工具调用展示），统一设计系统与密钥本地化。把文案润色封装为第一个 agent 工具，对话可调用，同时保留其左右分栏专用界面。
- **阶段 2｜校对迁移 + 知识库管理 UI**：校对逻辑迁到 TS，封装为第二个 agent 工具并保留三步向导界面；做知识库可视化增删改查，支持对话 @引用。
- **阶段 3｜文档填写工具**：基于知识库 + 模板自动填写营销文档（第三个诉求第 2 点），封装为第三个 agent 工具。
- **阶段 4（未来）｜多步编排 + 共享账号**：把跨工具链式任务做稳（可中断/重试/审计）；知识库后端化、加账号与权限。

## 不做 / 边界

- 不在阶段 0-1 引入服务器和账号系统，避免过度工程。
- 不保留两套技术栈长期并存；不为对话和专用界面写两套工具逻辑。
- 校对仍只读、不写回源文件；LLM 结果需人工复核（沿用现有边界）。

