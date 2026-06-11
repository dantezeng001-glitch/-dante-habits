---
name: slate to swiss grid theme
overview: 把现有 slate 主题替换为瑞士国际主义风（克莱因蓝 + 网格点阵 + 无衬线大字号对比），并改名为 grid，与 paper / ink 同款单字命名；paper / ink 两套不动。
todos:
  - id: rename
    content: "把主题 slate 改名为 grid：更新 widget.js 的 THEMES / THEME_LABELS / 默认值 / fallback / localStorage 默认；CSS 选择器同步改名"
    status: pending
  - id: tokens
    content: "重写 :root(=grid) 令牌：结构化深色底 + 克莱因蓝单一 accent + 无衬线 grotesk 字体栈；给 paper/ink 补 --backdrop: none"
    status: pending
  - id: swiss
    content: "新增 [data-theme=grid] 专属规则：网格点阵 .widget::after 叠层、瑞士字号对比（品牌/标题放大、标签收紧）、active 下划线/方块化"
    status: pending
  - id: verify
    content: "打开 index.html 逐个切 grid / paper / ink 验证：grid 焕新且 paper/ink 像素不变，accent 蓝不撞 ink 橙"
    status: pending
isProject: false
---

# slate 主题替换为瑞士国际主义风（改名 grid）

只动这一套主题。`paper` / `ink` 两套令牌、HTML 结构不改。涉及两文件：[desktop/src/widget.css](desktop/src/widget.css) 和 [desktop/src/widget.js](desktop/src/widget.js)（仅改名相关常量）。

## 为什么换方向

huashu 的暖深衬线编辑部风和现有三套气质偏近（重复度高）。改用 guizang 的「瑞士国际主义」：冷硬、网格、克莱因蓝、无衬线大字号对比——和 paper(浅) / ink(黑终端橙) / huashu(暖衬线) 全部正相反，信息驱动的「趋势 digest」也最契合。

## 命名

`paper` / `ink` / `slate` 是印刷/材料类单字名。瑞士风 + 蓝 + 网格，取同款单字名 **`grid`**（标签 `Grid`）。备选 `blueprint` / `klein`，定稿后改名只是一行 token 值的事。

## 设计要点（Swiss → grid）

- 底色：结构化深色（冷调近黑、略带蓝灰，非纯黑避开 ink），不透明度提到约 `0.85` 让网格线清晰、有存在感；保留极轻毛玻璃。
- accent：**单一克莱因蓝 IKB**（约 `#0B3DF5` / `#002FA7` 系，在深底上提亮）。Swiss 的「一个功能色」原则，正好避开 paper/ink 的橙。
- 字体：无衬线 grotesk 栈 `"Inter","Helvetica Neue",Helvetica,"Noto Sans SC",Arial,sans-serif`（Swiss = Helvetica，这里 Inter/Helvetica 是正确风格不是 slop）。
- 字号对比：品牌名/分区标题放大加粗，标签/日期/来源收紧字距小字号——制造瑞士式戏剧化层级。
- 签名细节：`.widget::after` 叠极淡网格点阵（dot matrix，opacity ≤ 0.06），仅 grid 生效。
- active/强调：tab active、pill 走方块化 + 蓝色块（去圆角的瑞士功能态）。
- 反 slop 自检：单色不堆叠、无紫渐变、无 emoji 图标、不照搬 GitHub 深蓝黑。

## 具体改动

### 1. 改名 slate → grid（[desktop/src/widget.js](desktop/src/widget.js)）
- `const THEMES = ["slate", "paper", "ink"]` → `["grid", "paper", "ink"]`（第 15 行）。
- `THEME_LABELS` 的 `slate: "Slate"` → `grid: "Grid"`（第 16 行）。
- `state.theme` 默认 `"slate"` → `"grid"`（第 32 行）。
- `applyTheme` fallback `"slate"` → `"grid"`（第 76 行）。
- 初始化 `applyTheme(savedTheme || "slate")` → `"grid"`（第 462 行）。
- 兼容：老用户 localStorage 存了 `"slate"`，因不在 THEMES 内会自动回退到默认 `grid`，无需迁移。

### 2. :root 令牌重写（= grid 默认）（[desktop/src/widget.css](desktop/src/widget.css)）
- `--bg` 改冷调结构化深色、不透明度约 `0.85`。
- `--accent` / `--accent-2` 统一克莱因蓝系（accent-2 仅深浅差，不引第二色相）。
- `--font-content` 换 grotesk 无衬线栈；`--font-ui` 仍走等宽做元数据。
- 新增 `--backdrop: blur(16px) saturate(115%)`；paper / ink 各自令牌块补 `--backdrop: none` 保持原样。
- 调 `--line/--edge/--surface` 配深底；视情况收圆角（`--radius*`）让功能态更方正。

### 3. grid 专属结构（新增 `[data-theme="grid"]` 选择器）
- `.widget::after`：dot-matrix / 细网格叠层（`background-image` radial/linear，极淡），仅 grid。
- 字号对比：放大 `.brand-cn` / 分区标题，收紧 `.meta-cell`/`.tab`/`.src` 字距。
- 功能态：`.tab.active`、`.pill` 方块化（去圆角）+ 蓝色填充。

### 4. `.widget` 加 `backdrop-filter: var(--backdrop, none)`
- 靠 token 控制，仅 grid 生效，paper/ink 为 none。WebView2 支持。

### 5. 验证
- 打开 [desktop/src/index.html](desktop/src/index.html)，用 ◑ 按钮循环切 grid / paper / ink：grid 焕新、另两套像素不变；切换 toast 显示「风格 · Grid」。
- 确认网格点阵不抢文字、蓝 accent 与 ink 橙无撞色。

## 不做

- 不改 paper / ink 令牌与外观，不改 HTML 结构、Tauri 配置。
- 不引入网络字体（小组件离线，全走系统字体栈）。
- 不做 guizang 的 WebGL 流体背景 / 横向翻页那套（那是 PPT 场景，这里只借瑞士视觉语言）。

## 待你拍板（不阻塞，可后改）

- 主题名 `grid`（备选 `blueprint` / `klein`）。
- accent 蓝深浅：偏正统深 IKB `#002FA7` 还是深底更亮的 `#0B3DF5`。
