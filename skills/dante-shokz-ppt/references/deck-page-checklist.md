# Deck Page Checklist · 交付前自检

> 全 deck 完成后、目检之前，按本表逐页过一遍。**任一项失败就回去改，不要带着已知问题交付**。

---

## 全局检查（整 deck 一次过）

### A. 文件 / 依赖

- [ ] 文件名带主题 + 日期，例：`2026Q2-OpenRun-launch.html`、`转正答辩_v4.html`
- [ ] `<title>` 改成 deck 主题，不是默认的"Untitled"
- [ ] `<link rel="stylesheet">` 指向 `deck.css`，且路径在用户工作目录能找到
- [ ] `deck.css` 文件本身存在（如选了"自带依赖"方案）
- [ ] 翻页脚本在文件末尾，能正确响应 ↑↓ 键

### B. 总页数 / 编号一致性

- [ ] `<section id="slide-N">` 的 N 从 1 连续递增到总数，**没有跳号**
- [ ] `data-idx="N"` 和 `id="slide-N"` 数字相同
- [ ] 顶部 `.deck-toolbar` 文字写的页数 = 实际页数
- [ ] 每页 `<div class="slide-num">NN / 总数</div>` 中的 NN 和 N 对应
- [ ] 每页右下角页脚的 `NN / 总数` 和 N 对应
- [ ] 总页数在 `slide-num` 和 footer 是一致的（如 16 / 16，不是 12 / 16）

---

## 逐页检查（每页一遍）

### C. Chrome（页眉 / 页脚）

- [ ] 页眉 `top: 32px`，等宽字体，11pt，色 `#666666`
- [ ] 页眉文字遵循"中文 · ENGLISH"格式
- [ ] 页脚左下 `Shokz 韶音 · BE OPEN`，每页一字不差
- [ ] 页脚右下 `NN / 总数`，等宽字体
- [ ] 封面页可以不要页眉（左上换为 `SHOKZ · PMKT ·`），但页脚仍要

### D. 标题

- [ ] 主标题 `top: 85.33px`，36pt（封面除外，封面用 60pt+），加粗，色 `#050505`
- [ ] 副标题 `top: 165.3px`，14pt，色 `#666666`（如本页有副标）
- [ ] 标题里的橙色强调词不超过 1-2 个关键短语
- [ ] 标题没用感叹号 / 问号（除非有意识地修辞）

### E. 配色

- [ ] 主色只用 `#FF7A3D` 和 `#050505`
- [ ] 灰阶只用 brand-spec 列的 4 个值（`#2F2F2F` / `#666666` / `#999999` / `#BABABA` / `#E5E5E5` / `#F1F1F1`）
- [ ] 整页没出现紫色 / 蓝色 / 绿色（Era 色 `#DBE3EC` / `#F4D9BC` 例外，但只在分类场景）
- [ ] 没有 `linear-gradient` / `radial-gradient`
- [ ] 没有 `border-radius: 8px+`（圆角是 0）
- [ ] 没有 `box-shadow`（页内元素）

### F. 字体 / 字号

- [ ] 中文文本字体堆栈 = brand-spec 规定
- [ ] 标签 / 编号 / 页脚使用 `Consolas, 'Courier New', monospace`
- [ ] 字号只用 8 档体系（60+ / 36 / 22 / 16-18 / 12-13 / 11 / 9-10 / 7-8.5）
- [ ] 没有 `font-style: italic`
- [ ] 没有 `text-decoration: underline`

### G. 内容密度

- [ ] 本页信息单元数在 [`layout-grid.md`](layout-grid.md) §6 密度区间内
- [ ] 没有"为了填满而加的"装饰元素（多余 icon / 重复文案 / 凑数 stats）
- [ ] 没有连续 3 页都是 Mid-High 或 High 密度

### H. 反 AI slop

- [ ] 没用 emoji 作 icon
- [ ] 没用"圆角卡片 + 左侧彩色 border accent"组合
- [ ] 没用 SVG 画人物 / 产品 / 抽象场景
- [ ] 涉及具体产品（OpenSwim Pro / OpenRun Pro 2 / NCE 等）时用了真实产品图
- [ ] 没出现"AI 觉得应该有"但用户原稿没有的内容

### I. 网格对齐

- [ ] 内容左边界 = 96px（除非有意识做全宽元素）
- [ ] 内容右边界 ≤ 1184px
- [ ] 多栏布局用 layout-grid 的标准栏宽（533 / 350 / 262 / 208）
- [ ] 三栏布局栏间距 = 18-21px
- [ ] 文字没溢出所在容器边界

### J. 中英文混排

- [ ] 没出现奇怪的字符截断（如"种语言" 被拆为 "种语 / 言"）
- [ ] 中文标点用全角（"，。：；！？"），英文标点用半角
- [ ] 中文引号用「」或""，不要用 `''`
- [ ] 数字 + 单位之间有空格（如 `5 min`、`100 件`）

---

## 内容质量检查

### K. 一致性

- [ ] 同一个产品名 / 项目名 / 公司名在全 deck 拼写一致
  - 例：是 `OpenRun Pro 2`，不是 `Open Run Pro2` / `OpenRunPro 2`
  - 例：是 `Shokz` 不是 `SHOKZ` / `shokz`（除非 LOGO 体或全大写 mono 标签里）
- [ ] 同一概念全 deck 用同一表达（如选了"AI 赋能"就不要某页又叫"AI 改造"）
- [ ] 时间格式一致（`2026 / 05` vs `2026年5月`，选一个）

### L. 准确性

- [ ] 所有数字（销量 / 时长 / 件数 / 百分比）和原内容稿一致，**没有"看起来更整"的篡改**
- [ ] 项目名 / 人名 / 部门名拼写正确
- [ ] 引用 / 引语标注准确，没编造
- [ ] 涉及具体数据时，能说出数据来源（如被人现场追问）

### M. 完整性

- [ ] 所有内容稿里的章节都映射到了 deck 页
- [ ] 没有"忘记翻译"的 placeholder（如 `<待补充>` / `[TODO]` / `XXX`）
- [ ] 图片资源都加载得了（`assets/p09-wechat-reaction.png` 等都在用户工作目录存在）

---

## 故障排查

### 翻页不工作

- 检查 `<script>` 块是否在 `</body>` 之前
- 检查是否引入了和翻页脚本冲突的其他 JS（如 motion.min.js 启用后写错调用）

### 文字溢出

- 检查所在 `.shp` 的 `width` / `height`
- 检查 `overflow: visible !important` 是否正常应用（否则会被 `.deck-slide .shp { overflow: hidden }` 截掉）
- 中文换行：`word-break: keep-all` + `overflow-wrap: normal`（已在 `deck.css` 里默认）

### 缩放后字号变模糊

- 不要在 `.deck-slide` 内手动加 `transform: scale()`
- 窄屏缩放由 `@media (max-width: 1360px)` 自动处理，已在 `deck.css` 里

### 字体显示为系统默认

- 检查 `font-family` 堆栈是否完整
- 检查用户环境是否安装了 Noto Sans SC（Windows 一般有 Microsoft YaHei 兜底，Mac 一般有 PingFang SC 兜底）

---

## 自检通过的样子

全部 checkbox 都打勾 → 浏览器目检翻一遍没异常 → 交付。

任一项未通过 → 回去改，不要"先交付再说"。
