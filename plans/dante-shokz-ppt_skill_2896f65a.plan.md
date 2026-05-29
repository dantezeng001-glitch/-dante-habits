---
name: dante-shokz-ppt skill
overview: 从 [转正答辩_v3_动画版.html](转正答辩_v3_动画版.html) 提取 Shokz 品牌排版 DNA、可复用组件、叙事框架库，落成 `c:\Users\016551\.cursor\skills\dante-shokz-ppt\` 一个中等工程化 skill：详尽 SKILL.md 做总入口，brand-spec / components / narrative-frameworks 作为分章 references，starter HTML 骨架 + 11 个 component snippet 让 agent 拼装而非纯手写，完整原 deck 保留作 example。
todos:
  - id: scaffold
    content: 创建 skill 目录结构（references/ assets/snippets/ example/）
    status: completed
  - id: skill-md
    content: 写 SKILL.md：触发条件 + 路由 + 工作流 + huashu-design 红线复用 + 资产协议
    status: completed
  - id: brand-spec
    content: 写 references/brand-spec.md：色板 / 字体堆栈 / 关键数值常量 / 禁区
    status: completed
  - id: layout-grid
    content: 写 references/layout-grid.md：1280x720 网格 + 关键点位 + 边距
    status: completed
  - id: components
    content: 写 references/components.md：11 类组件用法说明 + 对应 snippet 引用
    status: completed
  - id: narratives
    content: 写 references/narrative-frameworks.md：7 种叙事框架 + 何时用 + 何时不用
    status: completed
  - id: workflow-checklist
    content: 写 references/workflow.md + deck-page-checklist.md：分镜流程 + 交付自检
    status: completed
  - id: skeleton-css
    content: 写 assets/deck-skeleton.html + assets/deck.css：空白外壳 + 抽离公共样式 + 翻页脚本 + motion.min.js 复用
    status: completed
  - id: snippets
    content: 从 example 抽出 11 个 component snippet 到 assets/snippets/，每个顶部加'替换字段 / 不可改数值'注释
    status: completed
  - id: example-copy
    content: 把原 [转正答辩_v3_动画版.html](转正答辩_v3_动画版.html) 拷贝到 example/ 作为完整参考实现
    status: completed
isProject: false
---

# Dante Shokz PPT Skill

## 一、范围与定位

- **目标用户**：仅 Dante 一人，固定品牌 Shokz、固定职位 PMKT
- **触发场景**：所有 Shokz 内部 PPT——汇报 / 答辩 / 培训 / 产品上市 / 案例分享 / 路演 / 复盘
- **锁定维度**：品牌色板、排版网格、字体堆栈、页眉页脚、组件库（强制锁）
- **可选维度**：叙事框架库（STAR / 9-cards / 三层涟漪 / 时间线 / GOAL-ACTION-METRIC / FORMED-SHAPING 按场景挑用）
- **不做**：subagent 调度 / harness / validator 等 ppt-agent v4.1 的重工程化套件，保持 huashu-design 量级

## 二、目录结构

```
c:\Users\016551\.cursor\skills\dante-shokz-ppt\
├── SKILL.md                          (总入口 + 路由 + 工作流)
├── references/
│   ├── brand-spec.md                 (色 / 字 / 数值常量)
│   ├── layout-grid.md                (1280x720 网格 + 关键点位)
│   ├── components.md                 (11 类组件用法 + 引用 snippet)
│   ├── narrative-frameworks.md       (7 种叙事框架 + 何时用)
│   ├── workflow.md                   (内容稿 -> 逐页 HTML 流程)
│   └── deck-page-checklist.md        (交付前自检)
├── assets/
│   ├── deck-skeleton.html            (空白外壳 + 翻页脚本)
│   ├── deck.css                      (公共样式抽出)
│   ├── motion.min.js                 (从原 HTML 复用)
│   └── snippets/                     (11 个组件 HTML 片段)
│       ├── header-chrome.html
│       ├── footer-chrome.html
│       ├── cover.html
│       ├── section-divider.html
│       ├── star-card.html
│       ├── case-overview-9-cards.html
│       ├── timeline-4col.html
│       ├── three-column-goal-action-metric.html
│       ├── ripple-3-layer.html
│       ├── change-card.html
│       ├── retro-bar.html
│       ├── inline-badge.html
│       └── data-card-with-status.html
└── example/
    └── 转正答辩_v3_动画版.html       (完整参考实现，原样保留)
```

## 三、核心要点

### 3.1 品牌 DNA（必锁）
- 画布 1280x720 px，每页一个 `<section class="deck-slide">`
- 主色：`#FF7A3D` Shokz Orange / `#050505` Ink / `#666666` Mute
- 灰阶：`#2F2F2F` / `#BABABA` / `#E5E5E5` / `#F1F1F1`
- 字体：`"Noto Sans SC","Microsoft YaHei","PingFang SC","Noto Sans",system-ui` 中文 + `Consolas,"Courier New",monospace` 标签
- 边距：左右 96 / 顶 32（页眉）/ 主标题 85 / 副标题 165 / 内容 210+ / 页脚 674
- 标签语法："中文 · ENGLISH"（如 `案例 ① · 月银白 SOP`、`SITUATION · 背景`）

### 3.2 11 类核心组件
源自 [转正答辩_v3_动画版.html](转正答辩_v3_动画版.html)：
- 页眉 chrome（[L104-105](转正答辩_v3_动画版.html#L104)）/ 页脚 chrome
- 封面（橙色竖条 + 主副标题 + presenter + date）
- 章节分隔（全屏黑 + 大字 + 右下角导航）
- STAR 黑头卡（S/T/A/R 各一，黑头 50px + 灰 body）
- 9-cards Overview（左 3 大类锚点 + 右 3x3 数据卡，[L390-518](转正答辩_v3_动画版.html#L390)）
- 时间线 4 列（不同色 era + 圆点轴 + 心路面板）
- 三栏 GOAL/ACTION/METRIC（未来规划页同款骨架）
- 三层涟漪（部门内 / 跨部门 / 公司级 三色顶 border）
- 关键变化卡（编号 + 状态英文 + 标题 + 2-3 行 takeaway）
- 复盘条（橙色细边框 + 左侧橙色 `RETRO · 复盘` 徽章）
- 思考/任务 inline 徽章（黑底/橙底 7pt 等宽 + 嵌入段落）

### 3.3 7 种叙事框架（可选库）
- **STAR**（成功案例，[L524 slide-6/7](转正答辩_v3_动画版.html#L524)）
- **STAR + WARNING**（反面案例，[L618 slide-10](转正答辩_v3_动画版.html#L618)）
- **9-cards 全景**（多任务/多项目概览，[L381 slide-5](转正答辩_v3_动画版.html#L381)）
- **时间线 + 心路历程**（成长/迁移叙事，[L100 slide-2](转正答辩_v3_动画版.html#L100)）
- **三层涟漪**（影响力/扩散叙事，[L614 slide-9](转正答辩_v3_动画版.html#L614)）
- **GOAL-ACTION-METRIC 三段**（未来规划/OKR，[L747 slide-11](转正答辩_v3_动画版.html#L747)）
- **FORMED-SHAPING 关键变化**（个人成长/反思页，[L987 slide-15](转正答辩_v3_动画版.html#L987)）

### 3.4 工作流（SKILL.md 主链）
1. **场景识别**：用户给来内容稿 / brief / 大纲，先识别是哪类 PPT
2. **叙事选型**：从 `narrative-frameworks.md` 挑 1-N 个匹配框架
3. **分镜**：把内容映射到具体页（封面 / 章节 / STAR / 对比 / 收尾）
4. **拼装**：拷贝 `deck-skeleton.html` 为基底，每页从 `snippets/` 选组件粘进去
5. **填内容**：保持品牌色 + 标签语法 + 字号体系
6. **自检**：过 `deck-page-checklist.md`（页眉页脚页码 / 密度 / 反 slop）
7. **目检**：浏览器打开人工过一遍

### 3.5 复用 huashu-design 的红线
- 反 AI slop（禁止圆角 card + 左 border accent 滥用、禁 emoji 图标、禁紫渐变）
- 涉及具体产品（OpenSwim Pro / OpenRun Pro 2 等）时必须用真实产品图，不画 CSS 剪影
- Junior pass：先把骨架 show 给用户，再填内容
- 每个细节做到 120%，其他 80%

## 四、关键工程决策

- **不重新发明 deck-stage**：沿用原 HTML 的 `IntersectionObserver` 翻页脚本，简单稳定
- **CSS 抽离 vs 内联**：把 `.deck-slide / .shp / .pp / .tbl` 公共样式抽到 `deck.css`，每页 `<section>` 内只保留 inline 定位/颜色——这是中等工程化的核心收益
- **motion.min.js 保留但不强制**：v3 版引入但未启用动画，作为 nice-to-have 留位
- **snippet 用法约定**：每个 snippet 顶部用 HTML 注释标注 "1) 替换哪些字段 2) 哪些数值不能动"，避免 agent 乱改

## 五、不做的事

- 不写 Python harness / validator（不值得）
- 不写多文件 deck（保持单 HTML，沿用原方案）
- 不做导出 PDF / PPTX 脚本（用户用浏览器打印 PDF 已够；如需可后续追加）
- 不抽 React 组件（HTML 直拼更适合这种 fixed-layout 场景）
- 不写 brand-spec 之外的 design system 文档（已用 `references/` 拆好）
