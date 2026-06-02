# dante-habits

我（Dante）个人的 Cursor 工作习惯沉淀。

> 这不是工具备份，是我对 AI 协作怎么用得稳的偏好集合。它解释了：我下达任务时希望 AI 用什么节奏、什么纪律来回应，以及我反复用到的几类工作场景靠哪些 skill 来兜底。

仓库同步三件东西：**`rules/`**（全局生效的纪律）+ **`skills/`**（按场景触发的能力包）+ **`scripts/`**（让这套配置在新机器上一键重建的安装脚本）。运行时数据、Cursor 自带内容、临时备份一律不进库。

---

## Part 1 · `rules/` — 我希望 AI 怎么"做事"

5 条规则，分成两类：写代码的纪律 + 写文档的纪律。它们随项目自动加载，不需要每次提醒。

### 写代码

| 规则 | 它解决什么 |
|---|---|
| `ai-coding-discipline.mdc` | **AI 写代码的瓶颈是边界感，不是能力。** 下手前先停一步、改动不要跨文件扩散、交付必须可验证。涉及读/写/改任何 `.py / .ts / .ps1 / .sql / Dockerfile` 等代码与配置时强制生效。 |

### 写文档（长文 / 方案 / brief / PRD / 报告）

| 规则 | 它解决什么 |
|---|---|
| `work-in-layers.mdc` | **先骨架后内容，不一次性交付成品。** 改 ≥ 2 个文件、写 > 1 页、含"分析/规划/方案"的任务必须分层确认。 |
| `content-integrity.mdc` | **可以提出判断，不得制造规范。** 不添油加醋（"必须/最佳实践"要么有出处要么降级为"我的判断"）、跨文件不失真、表达凝练。 |
| `no-redundant-writing.mdc` | **同一件事只讲一次。** 删元叙述（"本节将讲…""综上所述…"）、删表格的二次解释、删章节自我介绍。 |
| `writing-quality.mdc` | **保留下来的句子要够利落。** 砍填充词、抽象改具体、加数字基准、控版式密度。先 `no-redundant-writing` 去重，再用本条精修。 |

**这套规则反映的工作习惯：**
- 我不喜欢 AI 直接吐成品，喜欢看到它先把骨架摆出来让我校准
- 我对"听起来很对但没出处"的判断零容忍
- 我宁愿短而准，不要长而软

---

## Part 2 · `skills/` — 我反复要做的几件事

12 个 skill，按用途分四组。

### 1. 内容/文档基础设施（每天都用）

| Skill | 我用它做什么 |
|---|---|
| `file-sync` | 把 PDF / PPT / DOCX / XLSX / XLSM 抽成 Markdown 给 AI 读，反向把 MD 导成 Word / PDF。处理扫描 PDF 的 OCR、图片型 PPTX、Excel 内嵌图、断行修复。 |
| `md-cleanup` | 文件抽出来的 Markdown 不能直接读——清掉钉钉/飞书/Notion 导出残留、字符编码残渣、过度转义、OCR 段落散乱、"## Page 3 / ## Slide 5" 这类机械标题。`file-sync` 抽完之后接力跑这个。 |
| `content-integrity-guard` | 多文档审计——查未被支持的判断、跨文档矛盾、信息冗余。和 `content-integrity` 规则配套，规则管"写的时候别犯"，这个 skill 管"写完了一起审"。 |

### 2. PPT / 演示文稿（高频）

| Skill | 我用它做什么 |
|---|---|
| `ppt-agent` | 全流程做 HTML 网页 PPT——需求调研 → 资料搜集 → 大纲 → 策划稿 → 设计稿。给老板汇报、给客户路演、培训课件都走这个。 |
| `guizang-ppt-skill` | 杂志风/电子墨水风格的横向翻页网页 PPT，单 HTML 文件交付。适合发布会、对外分享。 |

### 3. 设计 / 前端原型（中频）

| Skill | 我用它做什么 |
|---|---|
| `huashu-design` | 用 HTML 做高保真原型、动画 Demo、设计变体探索。需求模糊时它会先给 3 个差异化方向让我选，避免一上来就锁死风格。 |
| `frontend-design` | 写"看起来不像 AI 生成"的前端组件、页面、应用。 |
| `tailwind-design-system` | 用 Tailwind 搭设计系统——design tokens、组件变体、响应式、可访问性。 |
| `ui-ux-pro-max` | UI/UX 知识库（50+ 风格、161 配色、57 字体配对、99 条 UX 规则、25 种图表），覆盖 React / Next / Vue / Svelte / SwiftUI / RN / Flutter / shadcn / 纯 HTML。 |
| `web-design-guidelines` | 评审 UI 代码是否符合 Web Interface Guidelines。设计走完跑一遍。 |

### 4. 工作方法论（场景化）

| Skill | 我用它做什么 |
|---|---|
| `pua-motivator` | 兜底机制。AI 失败 ≥ 2 次、想放弃、提议"手动做吧"、把锅推给环境时强制启动结构化排错。我说"再试试 / 换个方法 / 为什么还不行"也会触发。 |
| `darwin-skill` | 自动优化我自己写的 skill 和 rule 文件——8 维度评分 + 山地爬升 + 测试验证 + 结果卡片。当我觉得某个 skill 写得不够好的时候用。 |

---

## 不在仓库里的东西

`plans/`、`projects/`、`plugins/`、`skills-cursor/`（Cursor 内置技能）、`subagents/`、`extensions/`、`ai-tracking/` 是运行时数据或 Cursor 自带内容，不进仓库。`skills/` 下任何 `*.bak-*/` 备份目录也忽略。详见 `.gitignore`。

## 自动同步

`scripts/auto-sync.ps1` 由 Windows 计划任务 `CursorConfigAutoSync` 每 2 小时跑一次，commit 后 push 到 `origin/main`，开机登录时也跑一次。日志在 `~/.cursor/.sync.log`。

**新机器一键恢复：** clone 本仓库到 `%USERPROFILE%\.cursor\`，然后跑

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\.cursor\scripts\install-auto-sync.ps1"
```
