---
name: Skill分享演示文稿
overview: 基于内容稿 `Skill逻辑框架与案例-karl-PPT版.md` 和 3 张配图，用 dante-shokz-ppt 模板拼装 8 页 HTML deck，输出为单文件 `Skill逻辑框架与案例.html`。
todos:
  - id: setup
    content: 创建目录结构，复制 deck.css 到 0513 Skills分享/assets/
    status: pending
  - id: p01-cover
    content: 拼装 P01 封面（cover.html 填内容）
    status: pending
  - id: p02-intro
    content: 拼装 P02 引入页（教实习生 4 步）
    status: pending
  - id: p03-abstract
    content: 拼装 P03 抽象映射页（三栏表格）
    status: pending
  - id: p04-framework
    content: 拼装 P04 四格框架页（图1 + 金句）
    status: pending
  - id: p05-case1
    content: 拼装 P05 术语库案例页（图2 + 4格摘要）
    status: pending
  - id: p06-case2
    content: 拼装 P06 中英校对案例页（图3 + 4格摘要）
    status: pending
  - id: p07-criteria
    content: 拼装 P07 判断准则页（三栏布局）
    status: pending
  - id: p08-thanks
    content: 拼装 P08 致谢页（Ink 底）
    status: pending
  - id: checklist
    content: 过 deck-page-checklist 自检
    status: pending
isProject: false
---

# Skill 逻辑框架与案例 · 演示文稿制作计划

## 叙事选型

培训课件场景，内容结构为"故事引入 → 概念抽象 → 框架 → 案例 x2 → 判断准则"。不套单一标准框架，按内容稿原有 6 节 1:1 映射到 8 页（含封面和致谢）。

## 分镜表


| 页   | 主题             | 组件 / 版式                                                                          | 内容稿来源 | 密度       |
| --- | -------------- | -------------------------------------------------------------------------------- | ----- | -------- |
| P01 | 封面             | `cover.html`                                                                     | —     | Low      |
| P02 | 引入：教实习生写会议纪要   | 自定义 4 步编号列表（左侧大编号 + 右侧正文，仿 change-card 结构）                                       | §0    | Mid-Low  |
| P03 | 从实习生到 Skill 四格 | 自定义表格（左栏"教实习生" → 中栏"抽象为" → 右栏"Skill 四格"）                                         | §1    | Mid      |
| P04 | 四格框架           | 整页嵌入 `图1-Skill逻辑框架.png` + 底部一句话金句                                                | §2    | Mid-Low  |
| P05 | 案例 ① 术语库提取     | 上方嵌入 `图2-术语库案例-BeforeAfter.png`，下方 4 格摘要条（边界/输入/执行/输出），右下角附 ChatGPT 分享链接二维码或文字链接 | §3    | Mid-High |
| P06 | 案例 ② 中英校对      | 上方嵌入 `图3-中英校对案例-BeforeAfter.png`，下方 4 格摘要条                                       | §4    | Mid-High |
| P07 | 什么任务适合做 Skill  | 三栏并列（高重复 / 自由度低 / 人工执行复杂），底部判断准则金句                                               | §5    | Mid      |
| P08 | 致谢             | `section-divider.html` 变体（Ink 底 + 大字"谢谢"）                                        | —     | Low      |


## 封面信息（默认值，可改）

- 左上标签：`SHOKZ · PMKT ·`
- 右上：`Dante Zeng`
- 场景名（22pt）：`内部分享`
- 主标题（60pt）：`Skill` （橙色）+ `逻辑框架与案例`（黑色）
- Presenter：`Karl`
- 角色：`Shokz 韶音 · PMKT · 产品营销`
- 日期：`2026 / 05`

## 图片引用

三张图已在 `0513 Skills分享/` 目录下，deck 与图同目录，用相对路径引用：

- `图1-Skill逻辑框架.png` → P04
- `图2-术语库案例-BeforeAfter.png` → P05
- `图3-中英校对案例-BeforeAfter.png` → P06

## 文件产出

- `0513 Skills分享/Skill逻辑框架与案例.html` — 主 deck
- `0513 Skills分享/assets/deck.css` — 从 skill 复制过来，deck 自带依赖

## 关键排版决策

- P02 四步编号：复用 change-card 的"左侧大编号 + 右侧标题 + 正文"结构，4 张卡纵向堆叠，状态词分别为 `STEP 01 / 02 / 03 / 04`
- P03 三列映射表：用三栏 350.22 布局，左栏"教实习生"、中栏"抽象为"、右栏"Skill 四格"，每栏 4 行对应
- P04 图片：`<img>` 居中放在内容区，宽度 fit 到 900px 左右，保留底部空间放金句
- P05/P06 案例页：图片占上半区（~320px 高），下半区放 4 个并排的微型摘要块（边界/输入/执行/输出），每块用 Ink 头 + 浅灰 body 的极简 mini-card
- P07 三栏：复用三栏 350.22 布局，每栏顶部 3pt 粗 border（沿用涟漪配色逻辑表示"重要程度递增"），内容为条件名 + 说明 + 举例

