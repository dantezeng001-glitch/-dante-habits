---
name: 生成转正答辩HTML PPT
overview: 调用全局 guizang-ppt-skill，把 [转正答辩_PPT大纲版.md](C:\Users\016551\OneDrive\Desktop\个人信息相关\转正答辩\转正答辩_PPT大纲版.md) 生成为单文件 HTML 横向翻页 PPT，14 页，墨水经典主题，浏览器直接打开演讲。
todos:
  - id: read_skill
    content: 读取 SKILL.md 及 references/ 下的 layouts/themes/checklist/components
    status: completed
  - id: copy_template
    content: 拷贝 template.html 到转正答辩 转正答辩_演讲版.html，改 title 和墨水经典主题色
    status: completed
  - id: fill_pages_01_04
    content: 填充 01-04 页：封面 / 自我介绍 / 岗位认知 / 工作汇报章节封
    status: completed
  - id: fill_pages_05_08
    content: 填充 05-08 页：工作总览 / 目标达成 / AI 赋能 / 知识资产
    status: completed
  - id: fill_pages_09_12
    content: 填充 09-12 页：文化章节封 / 文化起点 / 文化顿悟 / 文化落地
    status: completed
  - id: fill_pages_13_14
    content: 填充 13-14 页：三个变化 / 下一阶段+致谢
    status: completed
  - id: p0_check
    content: 对照 checklist.md 运行 P0 级自检，修复问题
    status: completed
  - id: deliver
    content: 交付单文件 HTML，告知用户打开路径与占位符替换说明
    status: completed
isProject: false
---

# 生成转正答辩 HTML PPT

## 输入与输出

- 输入文档：[转正答辩_PPT大纲版.md](C:\Users\016551\OneDrive\Desktop\个人信息相关\转正答辩\转正答辩_PPT大纲版.md)
- 使用 skill：`C:\Users\016551\.cursor\skills\guizang-ppt-skill\`
- 输出文件：`C:\Users\016551\OneDrive\Desktop\个人信息相关\转正答辩\转正答辩_演讲版.html`（单文件，浏览器直接打开）

## 关键决策（已与用户确认）

- 主题色：**墨水经典**（`references/themes.md` 的预设之一，不自定义 hex）
- 范围：**完整 14 页一次性生成**
- 个人信息：保留占位符 `[姓名]` / `[团队]` / `[岗位]` / `[教育背景]` / `[过往经历]`，用户后续在 HTML 里自行替换
- 双百积分截图：暂留 placeholder 文案，不阻塞生成

## 执行步骤

### 1. 读取 skill 资产

按 skill 工作流要求，先依次读：

- `C:\Users\016551\.cursor\skills\guizang-ppt-skill\SKILL.md`（主工作流）
- `references/layouts.md`（10 种布局骨架，用于第 2 步类名预检）
- `references/themes.md`（墨水经典主题色变量）
- `references/checklist.md`（P0 自检清单）
- `references/components.md`（字体、网格、callout、stat、pipeline 组件）

### 2. 拷贝模板并改主题色

- 拷贝 `assets/template.html` 到 `转正答辩/转正答辩_演讲版.html`
- 修改 `<title>` 为"试用期转正答辩 · [姓名]"
- 替换 `:root{}` 里的 6 行变量为"墨水经典"主题色（具体值从 `themes.md` 读取，不自定义）

### 3. 按大纲填充 14 页

严格按照大纲第 14 行的"页面规划总览"逐页生成：

- **01 封面**（Hero + WebGL 背景启用）：主标题"从'接住任务'到'沉淀方法'"
- **02 自我介绍**（左文右图）：三段式金句 + 占位符
- **03 岗位认知**（大引用）：四行衬线大字 + 底部三关键词
- **04 章节封 · 工作汇报**（章节幕封 + WebGL）
- **05 工作总览**（2×2 网格）：业务交付 / 技术转译 / 流程沉淀 / 知识治理
- **06 目标达成**（左文右表）：5 行表格
- **07 AI 赋能**（Pipeline）：5 步横向流程 + AI/人分工对照
- **08 知识资产**（Before/After 对比）：4 行对照表
- **09 章节封 · 文化体验**（章节幕封 + WebGL）
- **10 文化 · 起点**（大引用，占满整页）：员工手册原话
- **11 文化 · 顿悟**（Before/After + 横向 Pipeline 因果链）：两个意象 + 因果链
- **12 文化 · 落地**（三栏大字报）：自由与责任的三条实践
- **13 三个变化**（三栏大字报）：信息→表达 / 文案→项目 / 单次→流程
- **14 下一阶段 + 致谢**（左文右图）：5 行规划表 + 致谢段 + 结束金句

每页严格按大纲给出的字数密度填充，**不在每页堆叠多段说明**。

### 4. 节奏控制

- WebGL hero 背景仅在 01 / 04 / 09 三页启用，其余正文页克制
- 衬线大标题 + 非衬线正文 + 等宽元数据的三级字体分工
- 横向翻页：键盘左右键 / 滚轮 / 触屏滑动 / 底部圆点 / ESC 索引

### 5. P0 自检

对照 `references/checklist.md` 的 P0 级问题逐项检查：

- 类名是否在 `template.html` 已定义（无未定义类名）
- 每页是否单一论点、信息密度是否过载
- hero / non-hero 节奏是否合理
- 主题色变量是否一致使用 `var(--...)`，无散落 hex
- 横向翻页能否正常切到第 14 页

### 6. 不做的事

- 不生成 AI 配图（用户未要求，且双百截图等待用户后续补）
- 不自定义主题色 hex
- 不修改大纲文档原文（生成器只读）
- 不删除大纲里的占位符 `[姓名]` 等，原样写入 HTML

## 交付后用户操作

- 浏览器直接打开 `转正答辩_演讲版.html`
- 在 HTML 里 Ctrl+F 搜索 `[姓名]` / `[团队]` 等占位符替换为真实信息
- 双百积分确认后，可在第 12 页页脚或附录补一行积分数据
- 如需调整字号/间距，在对应 section 的 inline style 里改

