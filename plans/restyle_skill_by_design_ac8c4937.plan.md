---
name: Restyle Skill by Design
overview: 将现有 skill 从"品牌分组"重构为"设计风格分组"，6 个风格全部按视觉设计语言命名，品牌降为"近似参考"。
todos:
  - id: rename-refs
    content: 重命名 16 个 references 文件（beats/bose/sony/chinese-tech → bold-contrast/sensory-premium/tech-premium/data-spectacle）
    status: completed
  - id: rename-skeletons
    content: 重命名 5 个 skeleton HTML 文件
    status: completed
  - id: update-titles
    content: 更新所有重命名文件内的标题，品牌名降为“近似品牌”
    status: completed
  - id: rewrite-skill-md
    content: 重写 SKILL.md 的风格选择表和索引表
    status: completed
  - id: cleanup-old
    content: 删除旧命名文件
    status: completed
isProject: false
---

# 按设计风格重构 Skill

## 6 个风格定义

| # | 风格名 | 近似品牌 | 核心视觉 | 核心文案 |
|---|--------|---------|---------|---------|
| 1 | **Shokz** | Shokz | B&W 中性，品牌橙点缀 | 技术短句 + 价值句 |
| 2 | **Apple** | Apple / Samsung / Google | 白底 + 深黑段交替 | 诗意双关，极简 |
| 3 | **Bold Contrast** | Beats / Marshall | 暗底 + 产品色强对比 | 街头自信口语短句 |
| 4 | **Sensory Premium** | Bose / B&O / Jabra | 极简黑白，感官温暖 | 第二人称感官词 |
| 5 | **Tech Premium** | Sony | 80%+ 深色，克制数据 | 三层叙事 + 媒体引用 |
| 6 | **Data Spectacle** | OPPO / Huawei / Soundcore / Oladance | 全暗沉浸，巨型数据 callout | 工程叙事 + 代际对比 |

## 需要做的改动

### 1. 重命名文件

现有文件 → 新文件名映射：

| 原文件 | 新文件 |
|--------|--------|
| `references/beats-*.md` (4 个) | `references/bold-contrast-*.md` |
| `references/bose-*.md` (4 个) | `references/sensory-premium-*.md` |
| `references/sony-*.md` (4 个) | `references/tech-premium-*.md` |
| `references/chinese-tech-*.md` (4 个) | `references/data-spectacle-*.md` |
| `assets/beats-product-page-skeleton.html` | `assets/bold-contrast-product-page-skeleton.html` |
| `assets/bose-product-page-skeleton.html` | `assets/sensory-premium-product-page-skeleton.html` |
| `assets/sony-marketing-skeleton.html` | `assets/tech-premium-marketing-skeleton.html` |
| `assets/sony-buy-skeleton.html` | `assets/tech-premium-buy-skeleton.html` |
| `assets/chinese-tech-product-page-skeleton.html` | `assets/data-spectacle-product-page-skeleton.html` |

Apple 和 Shokz 文件名不变。

### 2. 更新文件内标题

每个重命名的参考文件内部的 `# Beats Style` / `# Bose Style` 等标题改为 `# Bold Contrast Style` / `# Sensory Premium Style`，并在标题下方加一行"近似品牌：Beats / Marshall"。

### 3. 重写 SKILL.md

- 风格选择表：用设计风格名替代品牌名
- "代表品牌" 列改为 "近似品牌"
- 参考文件索引表更新路径
- 其余工作流逻辑不变

### 4. 删除旧文件

重命名完成后删除所有旧命名的文件。

## 不改动的部分

- Shokz 原始文件（无前缀）不动
- Apple 文件（`apple-*`）不动
- 所有文件的实质内容不变，只改文件名和内部标题
