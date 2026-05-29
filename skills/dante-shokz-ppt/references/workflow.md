# Workflow · 从需求到交付

> 完整一次 deck 制作的步骤。SKILL.md §2 是速记版，本文是展开版。

---

## 阶段 0 · 接需求

### 0.1 第一句话先问清

不管用户说什么，先确认 4 个维度（一次性问完，不要挤牙膏）：

1. **场景**：什么会议 / 给谁看？（决定基调）
   - 转正答辩 / 述职 / 内部双周会 / 跨部门同步 / 高管汇报 / 培训 / 路演？
2. **页数预算**：希望几页？（决定密度和深度）
   - 5-8 页（紧凑）/ 10-16 页（标准）/ 20+ 页（培训级）
3. **时间预算**：讲多久？（决定文字量）
   - 5min（每页 20-30s）/ 15min（每页 1min）/ 30min（每页 2min）
4. **内容稿状态**：
   - 已有完整逐页文案 `.md` → 直接进 Step 1
   - 有讲稿但没分页 → 先和用户对齐分镜，再进 Step 1
   - 只有 brief / 一句话 → 先做内容稿，**不要带着没确认的内容直接做版**

> **不要替用户决定上面任一项**。这是用户的判断空间，不是 AI 的。

### 0.2 内容稿格式

理想形态是这样的 markdown（参考原任务的 `逐页文案稿.md`）：

```markdown
## P01 · 封面

**主标题**：学习业务，改造业务
**副标题**：试用期答辩
Presenter: 曾子逸 Dante Zeng
Role: Shokz 韶音 · 北美业务部 · 产品营销
Date: 2026 / 05

## P02 · 个人简介
...
```

---

## 阶段 1 · 叙事选型

### 1.1 选框架

参考 [`narrative-frameworks.md`](narrative-frameworks.md) §0 选型决策表，按场景反查 1-N 个匹配框架。

### 1.2 写分镜表

输出格式（必须 show 给用户认）：

| 页 | 主题 | 叙事框架 | 组件 | 内容稿来源 |
|---|---|---|---|---|
| P01 | 封面 | — | `cover.html` | 内容稿 §0 |
| P02 | 个人简介 | 时间线+心路 | `timeline-4col.html` | §1 |
| P03 | 全景 | 9-cards | `case-overview-9-cards.html` | §2 |
| P04 | 案例 ① · S/T/A | STAR | `star-card.html` | §3 |
| ... | ... | ... | ... | ... |

### 1.3 **必须停一下让用户认**

不要分镜写完就开始拼装 HTML。**show 给用户**：
- 总页数对吗？
- 每页对应内容稿的章节对吗？
- 框架选得合适吗？

用户认了 OK / 调整 OK / 不需要某页，才进 Step 2。

---

## 阶段 2 · 起手骨架

### 2.1 拷贝 skeleton

```
源：c:\Users\016551\.cursor\skills\dante-shokz-ppt\assets\deck-skeleton.html
目标：用户工作目录 / <topic>-<date>.html
```

例：`2026Q2-OpenRun-launch.html` / `转正答辩_v4.html`。

### 2.2 同步引入 deck.css

确保新 deck 的 `<head>` 里有：

```html
<link rel="stylesheet" href="<相对路径>/dante-shokz-ppt/assets/deck.css">
```

> 或者把 `deck.css` 也拷贝到用户工作目录 `assets/deck.css`，让 deck 自带依赖方便分发（推荐）。

### 2.3 改 `<title>` 和顶部计数

- `<title>` 改成 deck 主题
- 顶部 `.deck-toolbar` 的页数文字改成实际页数（如 `12 页`）

---

## 阶段 3 · 逐页拼装

对每一页执行：

### 3.1 新建 `<section>`

```html
<section class="deck-slide" id="slide-N" data-idx="N" style="background:#FFFFFF">
  <div class="slide-num">NN / 总数</div>

  <!-- header chrome -->
  ...
  <!-- 主标题 / 副标题 -->
  ...
  <!-- 内容组件 -->
  ...
  <!-- footer chrome -->
  ...
</section>
```

### 3.2 粘 chrome

从 [`snippets/header-chrome.html`](../assets/snippets/header-chrome.html) 粘页眉，改文字。

从 [`snippets/footer-chrome.html`](../assets/snippets/footer-chrome.html) 粘页脚，改右侧页码。

### 3.3 粘标题区

主标题（top: 85.33）+ 副标题（top: 165.3），如果当页需要徽章（如 `CASE 01 · STAR`），从 [`snippets/`](../assets/snippets/) 找对应小徽章模板。

### 3.4 粘核心组件

按分镜表的"组件"列找对应 snippet 文件，**整段复制**到主标题/副标题下方。

只改 snippet 内的"可改字段"，不动 `left/top/width/height/font-size/color`。

### 3.5 填内容

按内容稿 `.md` 的对应段落，把文字一条一条对应填进去。

> **填内容时三个红线**：
> 1. 不要"补充"用户没写的内容（如自己加一句"通过这次..."的总结）
> 2. 不要"优化"用户的原话（除非用户授权）
> 3. 关键词加粗/染色要克制，一段里最多 2 处橙色强调

---

## 阶段 4 · 中途 show

完成 30% 页数（如 16 页中的 5 页）后，**主动 show 一次**给用户看：

- 浏览器打开
- 翻 5 页给用户截屏 / 直接发文件
- 问："这个方向 OK 吗？字号、密度、强调点对吗？"

用户认了再继续。这是 Junior pass。

---

## 阶段 5 · 自检

完成全部页后，按 [`deck-page-checklist.md`](deck-page-checklist.md) 逐页过一遍。

---

## 阶段 6 · 目检

用 Chrome / Edge 打开 deck，用 ↑↓ 键完整翻一遍：

- 每页内容有没有溢出 `.deck-slide` 边界
- 字号大小一致性（参考 [`brand-spec.md`](brand-spec.md) §3 字号体系）
- 视觉密度是否分布合理（不是连续 3 页 High，也不是连续 3 页 Low）
- 翻页流畅度（不卡顿、不闪烁）

---

## 阶段 7 · 交付

### 7.1 单文件交付

直接发 `.html` 文件，用户双击就能开。

### 7.2 PDF 导出（如需要）

浏览器打印 → "另存为 PDF" → 横向 / 1280×720 缩放。**不**用本 skill 写专门的 PDF 导出脚本（保持轻量）。

### 7.3 留可编辑性

deck 是文本 HTML，用户后续可以自己改文字。所以：
- 不要 inline base64 大图（让图通过 `assets/` 引用，便于换图）
- 不要 minify HTML（用户要能阅读）
- 不要把所有 style 内联到 element 里（用 `deck.css` 类）—— 但这里有一个权衡：**snippet 内的定位 style 仍然必须内联**（因为每个组件位置可能不同），公共样式才走 class

---

## 阶段 8 · 修订

用户回来说要改：

| 情况 | 处理 |
|---|---|
| 改文字 | 直接编辑对应 `<section>` 内文字 |
| 改某页结构 | 整个 `<section>` 重写，不要在旧结构上打补丁 |
| 换风格 | **拒绝**——这是 Shokz 品牌锁，改风格意味着不用本 skill |
| 加页 | 在对应位置插入新 `<section>`，记得改后续所有页码 |
| 改顺序 | 重新排 `id="slide-N"` 和 `<div class="slide-num">NN / 总数</div>` |

---

## 工作流速查清单

```
0. 接需求      → 问场景/页数/时间/内容稿状态
1. 选叙事框架  → narrative-frameworks.md
2. 写分镜表    → 必须停下让用户认
3. 起骨架      → 拷贝 deck-skeleton.html
4. 拼装        → 每页：chrome + 标题 + 组件
5. 中途 show   → 完成 30% 时主动给用户看
6. 自检        → deck-page-checklist.md
7. 目检        → 浏览器翻一遍
8. 交付        → 单 HTML 文件
```
