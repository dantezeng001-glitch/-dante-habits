---
name: md-cleanup
description: Source-agnostic Markdown readability cleanup. Strips rich-text export artifacts (Dingtalk `$\color{}` mentions, `:::` fences, `请至钉钉文档查看附件…` link prefixes), fixes character-level encoding residuals (Kangxi radicals, NFKC, traditional leftovers), unescapes unnecessary MD escapes (`\-` `\*` `\_` `\|`), compresses blank-line noise, repairs OCR text into readable paragraphs, and guides semantic structural rewrites (heading hierarchy flattening, `## Page N`/`## Slide N:` to semantic titles). Use when the user asks to clean up / reformat / polish / 清洗 / 整理格式 / 提高可读性 of an MD file, when a Markdown file was just exported from Dingtalk / Feishu / Notion / Google Docs, or immediately after file-sync extraction of PDF/PPT/DOCX/XLSX into MD.
---

# MD Cleanup

通用 MD 可读性清洗。输入源无关——无论是从 PDF/PPT 抽取出的 MD、钉钉/飞书/Notion/Google Docs 导出的 MD、还是手写 MD 混入了伪影，都按本 skill 的规则处理。

本 skill 与 `file-sync` 的分工：

- `file-sync`：负责二进制文件（PDF/PPT/DOCX/XLSX）→ MD 的抽取，以及抽取特有的后处理（空页 OCR 重抽、PDF 断行合并、最终验证审计）
- `md-cleanup`（本 skill）：负责通用 MD 表现层清洗、OCR 文本段落整理，被 `file-sync` 在抽取完成后自动调用，也可独立使用

---

## 何时触发

- 用户说 "清洗 / 整理格式 / 提高可读性 / reformat / clean up / polish"
- 用户刚从钉钉 / 飞书 / Notion / Google Docs 导出 MD 并拖进项目
- `file-sync` 在 Part A 抽取完成后（由其 SKILL.md 硬约束调用本 skill）
- 批量新收到多份伪影明显的 MD 文件
- 看到一份 MD 里有 3+ 个 `### 第 \d+ 行` + `- 字段名: 值` 列表结构（Excel 抽取成竖排 key-value，必须改表格，见 F5.5）
- 看到 MD 表格被 `\n` 撑坏（逻辑 row 跨多个物理行，见 F5.6）
- 看到 `## 图片 OCR`、`[OCR attempted ...]`、逐行 OCR 碎片、中文字间空格（如 `以 下 文档`），或用户说 OCR 内容要整理成完整段落（见 F7）

## 执行顺序（强制）

一个完整的 cleanup 交付必须跑完以下两段，一段不能跳：

1. **脚本段**：`python "<skill-dir>/scripts/md_cleanup.py" <files> --in-place`
   自动处理 F1 / F2 / F3 / F4 / F6 家族（见规则库）
2. **AI 段**：由 agent 按本文档 F5 / F7 规则做语义重排或 OCR 段落修补
   - 命中 F5 / F7 触发条件时必做，不命中才允许跳过
   - 不允许把 F5 / F7 的工作甩给用户"再说一声"

**只跑脚本段就交付 = 流程违规。** 用户不需要提醒"再整理一下结构"。

### 交付前扫读友好度自检（强制）

脚本段跑完后，交付前 agent 必须回答以下四个问题。**任一为"不"就必须动 F5**，不得把判断推给用户：

1. 文件里是否有 3+ 个 `### 第 \d+ 行` / `### Slide \d+` 之类的机械标题？ → 命中 F5.2 或 F5.5
2. 有没有 MD 表格行跨越多个物理行（表格被 `\n` 撑坏）？ → 命中 F5.6
3. 文件行数 ÷ 原始数据行数 是否超过 3 倍？（Excel 93 行数据变成 800 行 MD = 红灯） → 十有八九是 F5.5
4. 正文是否 90%+ 是 `- ` 或全是 `#`？ → 命中 F5.1 / F5.3
5. 是否存在 `## 图片 OCR` 且 OCR 文本仍是逐行碎片、明显错断或乱码？ → 命中 F7

"用户没提醒 = 不用做" 是错误心态。用户提醒"可读性太差"时，说明你漏了第 3 题。

---

## 规则库（按伪影家族组织）

每个家族都带「触发条件 / 处理动作 / Before / After / 谁负责」。**不是每份文件都跑全部规则**，只跑命中触发条件的部分。

### F1 字符级（脚本负责）

| 子规则 | 触发 | 处理 |
|---|---|---|
| F1.1 NFKC 归一化 | 始终 | `unicodedata.normalize("NFKC", text)` |
| F1.2 康熙部首 | 字符 `⼀⽉⾊⾸` 等（U+2F00–U+2FD5） | 映射到标准 CJK `一月色首` |
| F1.3 CJK 补充部首 | 字符 `⻚⻢⻓` 等（U+2E80–U+2EFF） | 映射到简体 `页马长` |
| F1.4 传统字残留 | 常见对（如 `戶`→`户`） | 替换 |

常见于 PDF / PPT 抽取后的 MD。钉钉导出一般不触发 F1.2–F1.4。

**NFKC 已知副作用（F1.1）**：会把**全角半角混排**的字符归一化，包括：

- 全角英文字母 / 数字（`Ａ` `１`）→ 半角（`A` `1`）
- 全角英文标点 `：` `，`（FULLWIDTH COLON / COMMA，U+FF1A / U+FF0C）→ 半角 `:` `,`
- 全角英文圆括号 `（` `）`（U+FF08 / U+FF09）→ 半角 `(` `)`

中文专有标点 **不会** 被 NFKC 转换：

- 句号 `。`（U+3002）保留
- 书名号 `《》`、顿号 `、`、引号 `""''` 全部保留

对于抽取出的 MD（全角半角混排常见）这个归一化是合理的。对于**纯手写中文 MD**，用户若希望完全保留中文标点风格（如希望 `：` 不要变 `:`），可跳过 F1：`python md_cleanup.py <file> --in-place` 暂无 `--no-f1` 开关，目前需在脚本源码里注释掉相应调用。后续如有反馈可加 flag。

### F2 转义残留（脚本负责）

| 触发 | 处理 |
|---|---|
| 正则 `(?<!\\)\\([\-*_\|])` 命中 | 移除不必要的反斜杠 |

**Before:**

```
\- 一条列表
带转义的 \*斜体\* 和 \_下划线\_
```

**After:**

```
- 一条列表
带转义的 *斜体* 和 _下划线_
```

钉钉、飞书富文本编辑器导出常见。

### F3 富文本导出伪影（脚本负责 F3.1–F3.3，agent 负责 F3.4）

#### F3.1 LaTeX 着色包裹（脚本）

| 触发 | 处理 |
|---|---|
| 正则 `\$\\color\{#?[0-9A-Fa-f]{3,8}\}\{([^{}$]*)\}\$` 命中 | 剥离着色保留内容 |

**Before:** `$\color{#0089FF}{@欧丰硕(Elliott)}$`
**After:** `@欧丰硕(Elliott)`

钉钉导出中的 @ 提及、重点色字都是这种格式。

#### F3.2 `:::` 围栏容器（脚本）

| 触发 | 处理 |
|---|---|
| 整行匹配 `^\s*:::\s*[A-Za-z_-]*\s*$` | 删除此行（保留内部内容） |

**Before:**

```
:::
IMC/PMO-Elliott
:::
```

**After:**

```
IMC/PMO-Elliott
```

钉钉块容器（warning / info / 自定义 block）导出都是这种语法。

#### F3.3 组合情况：被着色包裹的提及

F3.1 完成后，`$\color{}{@...}$` 自动变成 `@...`，不需要额外规则。如需进一步把 `@姓名(花名)` 改成 `@花名` 这种口语化表达，属于 F5 范畴（AI 判断）。

#### F3.4 表格单元格内嵌套有序列表（agent 负责，不走脚本）

| 触发 | 处理 |
|---|---|
| 表格单元格内出现 `1.  xxx<br>    <br>2.  yyy<br>    <br>3.  zzz` 模式 | agent 手动重写为 `① xxx<br>② yyy<br>③ zzz`，或用分号分隔 |

**为什么脚本不做？** 同时触碰 HTML `<br>` 与 Markdown 表格单元格，自动替换有破坏语义的风险。agent 判断后手动处理。

### F4 链接文案噪音（脚本负责）

| 触发 | 处理 |
|---|---|
| 文本出现 `请至钉钉文档查看附件` | 删除此前缀，`《文档名》` 保留 |

**Before:** `[请至钉钉文档查看附件《Swimming IMC 指标追踪》](https://...)`
**After:** `[《Swimming IMC 指标追踪》](https://...)`

其他家协作文档类似模式（如 Notion 的 "View in Notion"）可按需追加。

### F5 结构级（agent 负责，AI 推理）

脚本不做任何结构调整。以下触发条件任一命中，agent 必须动手：

| 子规则 | 触发 | 处理 |
|---|---|---|
| F5.1 全 `#` 一级标题 | 全文 `#` 开头的标题 ≥ 3 个，且没有 `##` 或更深层级 | 按语义重建 H1 / H2 / H3 层级。文档首行顶级标题保持 H1；后续根据内容归属改 H2/H3 |
| F5.2 抽取伪标题 | 3+ 个 `## Page \d+` 或 `## Slide \d+:` | 用 slide/page 实际内容替换为语义标题（如 `## Slide 5: 2024/9/30` → `### 直销-官网`） |
| F5.3 扁平 bullets | 正文 90% 以上的行以 `- ` 开头 | 识别逻辑分组，用嵌套列表或标题层级重组 |
| F5.4 空 section 标题 | 标题下方没有任何内容（下一个标题紧接着出现） | 加占位 `_（待补充）_` 或与前后合并 |
| F5.5 竖排 key-value 表格 | 3+ 个 `### 第 \d+ 行` 块，每块下是 `- 字段名: 值` 列表（Excel 抽取惯犯） | 全部折叠为**单个 Markdown 表格**：字段名做列头，每块一个数据行；`表头前备注` 保留在上方。详见下文 |
| F5.6 表格单元格含真实换行 | Markdown 表格行里出现 `\n`（一行逻辑 row 被物理拆成多行，表格被撑坏） | 单元格内 `\r\n` / `\n` → `<br>`；竖线 `\|` 转义。**只动表格内，不动代码块/段落** |

**硬约束：**

- **绝不编造内容。** 不添加原文没有的数据、数字、分析、结论。不确定时原样保留。
- **先跑脚本段，再做 F5。** F1/F2/F3/F4 清完，F5 判断才准。
- **跨章节合并要慎重。** 把看似重复的章节合成一节前，先检查两段是否确实是同一主题。
- **F5.5 不得丢数据行，也不得擅自删"看起来空"的列**——列是否空要先扫完整个数据段才能判定。
- **存在多个合理重组方案时先停一下。** 如果同一份文档既能按时间线重组，也能按主题重组，先给用户一个推荐结构，再继续改，不要替用户做不可逆的结构选择。

#### F5.5 详解：竖排 key-value 怎么改表格

坏格式（Excel 抽取出来就是这样）：

```
### 第 2 行

- `项目类型`: AO
- `人群/关键词类型`: INT
- `广告组完整命名`: AO_INT_Collections-Page_test
- `命名规则`: 首字母大写

### 第 3 行

- `项目类型`: Launch
- `人群/关键词类型`: ASC
- `广告组完整命名`: Launch_ASC_Pillar-Page-Openear_
- `命名规则`: 新品上市统一命名为Launch
```

37 行数据会膨胀到 290 行 MD，扫读成本指数级上升。

好格式：

```
| 项目类型 | 人群/关键词类型 | 广告组完整命名 | 命名规则 |
|---|---|---|---|
| AO | INT | AO_INT_Collections-Page_test | 首字母大写 |
| Launch | ASC | Launch_ASC_Pillar-Page-Openear_ | 新品上市统一命名为Launch |
```

重写时：

1. 列头取并集（以 `## 字段` 列表为准；若无 `## 字段` 段，扫所有数据块收集字段名顺序）
2. 某行缺某字段 → 该单元格留空
3. 单元格内 `\n` → `<br>`，`|` → `\|`
4. 纯空占位列（列名为 `column_N` 且该列所有数据全空）可删，其它空列必须保留
5. `## 表头前备注` 原样保留在表格之前

### F6 噪音级（脚本负责）

| 子规则 | 触发 | 处理 |
|---|---|---|
| F6.1 多重空行 | 3+ 连续空行 | 压缩为 2 |
| F6.2 行尾空白 | 任意行末 ` ` 或 `\t` | 删除 |
| F6.3 `[No text extracted]` 残留 | 孤立的 `[No text extracted]` 行 | 由 file-sync 的 Step 0 负责 OCR 重抽；md-cleanup 本身不删（删了会掩盖问题） |

### F7 OCR 文本段落级（脚本 + agent 负责）

`file-sync` 负责把图片 OCR 抽出来；`md-cleanup` 负责把 OCR 文本整理成读者能读的段落。**不得交付逐行 OCR 碎片**，尤其是中文资料。

| 子规则 | 触发 | 处理 |
|---|---|---|
| F7.1 中文字间空格 | `以 下 文档 按 产 出 顺序` | 仅在同一行内删中文-中文、中文-中文标点之间的多余空格；不要用 `\s+` 跨换行删除，避免把段落边界吞掉 |
| F7.2 OCR 视觉换行 | 一句话被图片排版断成多行 | 合并成自然段；英文用空格连接，中文通常直接连接 |
| F7.3 连字符断词 | `com-\nplete` | 合并为 `complete` |
| F7.4 明显乱码 | 随机字母 / 符号串，无法还原 | 不硬猜；改成 `_OCR 输出疑似乱码，未能可靠还原文字。_` 或保留可靠片段 |
| F7.5 语义错断 | OCR 空行把同一句切成两段，如上一段以 `不/和/与/或/but/and/with/of` 等悬空词结尾 | agent 轻修：结合上下文把本来属于同一句/同一段的内容接回去 |
| F7.6 图像无字 | LOGO / 产品图 / 装饰图 | 保留 `_OCR 未识别出文字（可能是 LOGO 或纯图）_`，不要删除该图记录 |

#### F7 输出格式

保留图片编号和来源，正文用普通段落，不用 `>` 引用块：

```
## 图片 OCR

_文本经 Tesseract OCR 抽出后整理为段落；部分明显错断、乱码由 AI 轻修。修补只做断句、连接和明显 OCR 误识修正，不新增事实。_

### 图 1 — `image1.png`

_来源: `xl/media/image1.png`_

以下文档按产出顺序排序，不可变换。本文档作为 0 号文档放在第一个 sheet。

需包含 SPEC / 文字变更点，并 @ 各领域同步。FABE 变更后需及时同步 PMKT / 营销 CTM；不确定内容标红。
```

#### F7 硬约束

- **不新增事实。** 只做断句、连接、明显 OCR 误识修正；不要补充图片里没有的信息。
- **不要把无把握乱码改成看似正确的句子。** 标记无法可靠还原比伪造内容安全。
- **不保留原始 OCR**，除非用户要求可追溯；默认只交付整理后的可读段落。
- **如果 OCR 语言包不足要明说。** 中文图片只有 `eng` 时，不能声称中文 OCR 完成；应安装/使用 `chi_sim` 或 `chi_tra` 后重跑。

---

## 使用方法

### 独立使用（用户拖了一份 MD 进来）

```bash
python "<skill-dir>/scripts/md_cleanup.py" "path/to/file.md" --in-place
```

`<skill-dir>` = `~/.cursor/skills/md-cleanup/`

批量：

```bash
python "<skill-dir>/scripts/md_cleanup.py" "dir/*.md" --in-place
```

脚本跑完，agent 扫一遍文件看 F5 / F7 触发条件是否命中，命中则继续做结构重排或 OCR 段落修补。

### 被 `file-sync` 自动调用

`file-sync` 在 Part A 抽取完成后，其模板脚本 `template_document_sync.py` / `template_excel_sync.py` 会在 `main()` 末尾 subprocess 调用本 skill 的 `md_cleanup.py`。若本 skill 不存在，file-sync 脚本静默跳过，agent 在 SKILL.md 层手动调用。

### 反例：干净的 MD

- 手写 MD 通常触发不到任何规则，`md_cleanup.py` 会报告 `OK: <filename>` 不改动内容
- 脚本是幂等的——清洗过的文件再跑一次仍然 `OK`

---

## 规则扩展

发现新的伪影模式时：

1. 先判断归属哪个家族（F1–F7），不要新开家族
2. 脚本能安全自动化的 → 扩 `scripts/md_cleanup.py`
3. 需要上下文判断的 → 扩本文档 F5 规则
4. 把典型样本记录到 `references/artifact-patterns.md`

当前 references 覆盖：钉钉。待扩展：飞书 / Notion / Google Docs / Quip。

---

## Additional Reference

- 各家协作文档的典型伪影样本：[references/artifact-patterns.md](references/artifact-patterns.md)
- 脚本源码：[scripts/md_cleanup.py](scripts/md_cleanup.py)
