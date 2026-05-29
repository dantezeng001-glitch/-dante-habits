---
name: Skill分享PPT制作
overview: 将「Skill 逻辑框架与案例」内容稿制作为 8 页 Shokz 品牌 HTML deck，嵌入 3 张用户提供的图 + 2 个案例链接，为 P02 生成一张"教实习生"场景插图。
todos:
  - id: gen-img
    content: P02 场景插图生成：扁平极简风“教实习生”场景
    status: completed
  - id: copy-assets
    content: 拷贝 deck.css + deck-skeleton.html 到工作目录
    status: completed
  - id: build-p01-p04
    content: 拼装 P01-P04（封面 + 引入 + 抽象 + 四格）
    status: completed
  - id: build-p05-p06
    content: 拼装 P05-P06（两个案例页，嵌图 + 四格 + 链接）
    status: completed
  - id: build-p07-p08
    content: 拼装 P07-P08（判断标准 + 致谢）
    status: completed
  - id: selfcheck
    content: 按 deck-page-checklist 自检：页码/chrome/配色/字号/密度
    status: completed
isProject: false
---

# Skill 分享 PPT 制作方案

## 分镜表（8 页）


| 页   | 主题             | 组件                              | 内容来源                | 密度       |
| --- | -------------- | ------------------------------- | ------------------- | -------- |
| P01 | 封面             | `cover.html`                    | 主题 / presenter / 日期 | Low      |
| P02 | 引入：教实习生写会议纪要   | 自定义 4 步布局 + 生成插图                | 内容稿 §0              | Mid-Low  |
| P03 | 从实习生到 Skill 四格 | 自定义对照表                          | 内容稿 §1              | Mid      |
| P04 | 四格框架           | 大图居中（图1）+ 底部强调句                 | 内容稿 §2 + 图1         | Mid-Low  |
| P05 | 案例 ① 术语库提取     | 大图（图2）+ 紧凑四格 + 链接               | 内容稿 §3 + 图2 + 术语库链接 | Mid-High |
| P06 | 案例 ② 说明书中英校对   | 大图（图3）+ 紧凑四格 + 链接               | 内容稿 §4 + 图3 + 校对链接  | Mid-High |
| P07 | 什么任务适合做成 Skill | 自定义三条件 + 判断逻辑                   | 内容稿 §5              | Mid      |
| P08 | 致谢             | `section-divider.html` 变体 Ink 底 | —                   | Low      |


## 各页细节

### P01 · 封面

- 场景名：Skills 分享
- 主标题：`Skill`（橙）+`实战分享`（黑）
- Presenter：曾子逸 Dante Zeng
- Role：Shokz 韶音 · PMKT · 产品营销
- Date：2026 / 05

### P02 · 引入：教实习生写会议纪要

- 页眉：`引入 · INTRO`
- 布局：4 个纵向排列的编号块（左侧橙色大编号 01-04 + 右侧每步的说明文字）
- 左侧或顶部放一张生成的插图（教实习生场景，与用户提供图保持一致风格：扁平线条、灰白底色、简洁人物）
- 底部金句：这四步就是一个最朴素的工作流

### P03 · 从实习生到 Skill 四格

- 页眉：`框架推导 · FRAMEWORK`
- 主标题：从实习生到 Skill 四格
- 核心内容：对照表（3 列 × 4 行）
  - 列头：教实习生 → 抽象为 → Skill 四格
  - 用 `#F1F1F1` 底 + `#050505` 文字 + 橙色强调关键词
- 底部全宽条（retro-bar 变体）：做 Skill = 把教实习生时"嘴上说的那套"写成文字，让 AI 能跑、让同事能接

### P04 · 四格框架

- 页眉：`四格框架 · SKILL FRAMEWORK`
- 图1 居中展示（`图1-Skill逻辑框架.png`，约 900px 宽）
- 图下方紧凑四格标签行（4 个 inline 标签：边界 / 输入 / 执行 / 输出）
- 底部强调句（橙色）：最容易被忽略的是**边界**——没写"不做什么"，AI 就会越界自作主张

### P05 · 案例 ① 术语库提取（沉淀型）

- 页眉：`案例 ① · CASE 01 · 术语库`
- 上半区：`图2-术语库案例-BeforeAfter.png`（全宽 1088px）
- 下半区左：紧凑四格（边界/输入/执行/输出，4 行 × 2 列小表格）
- 下半区右：效果金句 + 链接按钮
  - 链接：`https://chatgpt.com/share/e/6a03d3d0-34d0-8007-a086-b0050e9a0c89`
  - 标注文字："查看完整对话记录"

### P06 · 案例 ② 说明书中英校对（触发型）

- 页眉：`案例 ② · CASE 02 · 中英校对`
- 布局与 P05 同构
- 上半区：`图3-中英校对案例-BeforeAfter.png`
- 下半区左：紧凑四格
- 下半区右：效果金句 + 链接
  - 链接：`https://chatgpt.com/share/e/6a03deca-f6d4-8007-bdde-03bb5d39c740`

### P07 · 什么任务适合做成 Skill

- 页眉：`适用判断 · WHEN TO BUILD A SKILL`
- 主标题：什么任务适合做成 Skill
- 三栏条件（类似 GOAL-ACTION-METRIC 三栏布局，每栏一个条件）：
  - 栏 1：高重复（每周/每项目做一遍）
  - 栏 2：自由度低（有明确标准）
  - 栏 3：人工执行复杂（跨文档多表比对）
- 底部判断逻辑条（全宽，分三段）：
  - 3个都满足 → 立刻做 Skill
  - 只满足1-2个 → 拆出标准化部分
  - 都不满足 → AI 对话即可

### P08 · 致谢

- Ink 黑底
- 大字（60pt 白）：谢谢
- 副文（16pt 橙色等宽）：THANKS · Q&A

## 需要生成的图片

**P02 场景插图**：扁平极简风格，白底灰线条，一个"前辈 → 实习生"的示意场景，画面中有 4 个标注步骤的图标（任务/知道/怎么做/交什么），与用户提供的图1-3 保持视觉一致（线条人物、无渐变、简洁标注）。

## 文件结构

```
0513 Skills分享/
├── Skill实战分享-Dante.html          ← 主 deck 文件
├── assets/
│   └── deck.css                      ← 从 skill 拷贝
├── 图1-Skill逻辑框架.png             ← 已有
├── 图2-术语库案例-BeforeAfter.png    ← 已有
├── 图3-中英校对案例-BeforeAfter.png  ← 已有
└── 图0-教实习生场景.png              ← 生成
```

## 品牌锁

- 主色：`#FF7A3D`（橙）+ `#050505`（黑）
- 字体：Noto Sans SC + Consolas 等宽
- 8 档字号体系（60pt 封面 / 36pt 主标 / 11pt chrome）
- 直角矩形，无 `border-radius`
- 无渐变、无 emoji、无 icon

