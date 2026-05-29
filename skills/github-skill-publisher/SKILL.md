---
name: github-skill-publisher
description: >-
  将本地 Cursor/Claude Skill 发布到独立 GitHub repo，自动生成 README 和 CHANGELOG。
  支持首次发布和增量更新两条流程，内置三层保密过滤防止企业敏感数据泄露。
  Use when the user mentions 上传 skill、发布 skill、推送 skill、更新 skill、
  同步 skill、publish skill、upload skill、push skill to GitHub、
  sync skill、update skill on GitHub、把 skill 传到 GitHub。
---

# GitHub Skill Publisher

将本地 Cursor/Claude Skill 发布到独立 GitHub repo，自动生成 README + CHANGELOG，内置保密过滤。

## 前置条件

执行任何操作前，先验证：

1. `gh auth status` 已登录且 token 包含 `repo` scope
2. `git --version` 可用
3. `sensitive-keywords.yml` 存在于本 skill 目录下（路径：`~/.cursor/skills/github-skill-publisher/sensitive-keywords.yml`）

任一条件不满足则停止并告知用户如何修复。

---

## Step 0: 流程路由

| 用户口令信号 | 流程 |
|------------|------|
| "上传 / 发布 / publish / push" + skill 名 | **首次发布**（Flow A） |
| "更新 / 同步 / update / sync" + skill 名 | **更新同步**（Flow B） |
| 无法判断 | 问用户："是首次发布还是更新已有 repo？" |

两条流程都从 **Step 1: 定位 skill** 开始。

---

## Step 1: 定位 Skill 目录

按以下顺序搜索，找到第一个包含 `SKILL.md` 的目录即停止：

1. `~/.cursor/skills/{name}/SKILL.md`
2. `~/.claude/skills/{name}/SKILL.md`
3. 用户指定的绝对路径

找不到则报错，列出可用的 skill 名供用户选择（用 `ls ~/.cursor/skills/` 列出）。

找到后，读取 `SKILL.md` frontmatter（name、description）和完整目录树，作为后续步骤的输入。

---

## Step 2: 保密过滤（硬规则，不可跳过）

读取 `sensitive-keywords.yml`，提取 `brands`、`products`、`file_patterns` 三类关键词。

### 第一层：Skill 级别分析

**仅当 skill 目录名或 SKILL.md description 包含 `brands` 关键词时触发此层。**

扫描 skill 目录下所有文本文件内容，计算公司数据浓度：

```
浓度 = 命中任意敏感关键词的文件数 / 可上传文件总数（排除 node_modules 等运行时目录）
```

- **浓度 > 50%** → 阻断上传。向用户报告：
  > "skill `{name}` 的 {N}/{Total} 个文件包含企业敏感数据（浓度 {X}%），脱敏后 skill 将丧失核心价值。建议不上传此 skill。"
  > 用户坚持要求上传时才继续（需明确确认）。

- **浓度 ≤ 50%** → 提示重命名 repo：
  > "skill 名称 `{name}` 包含企业品牌名。建议 repo 名改为 `{suggested_name}`（去掉品牌关键词）。你也可以指定其他名字。"

**目录名不含品牌名时跳过此层，直接进入第二层。**

### 第二层：文件级别排除

对 skill 目录下每个文件：

1. 文件路径匹配 `file_patterns` 中的任一通配模式 → 排除
2. 文件内容中 `brands` 或 `products` 关键词命中次数 ≥ 5 → 排除（该文件以公司数据为主体）

被排除的文件记入过滤报告，不参与后续流程。

### 第三层：内容级别脱敏

对通过第二层的文件，逐个检查内容：

- 命中 `brands` 关键词 → 替换为 `[YourCompany]`
- 命中 `products` 关键词 → 按首次出现顺序替换为 `[ProductA]`、`[ProductB]`、`[ProductC]`…
- 无命中 → 原样保留

需要脱敏的文件：创建副本到临时目录 `.skill-publisher-staging/{skill-name}/`，后续上传使用副本。**本地原文件永远不改动。**

### 过滤报告

三层扫描完成后，向用户展示过滤报告：

```
## 保密过滤报告

**Skill**: {name}
**总文件数**: {N}
**可上传文件**: {M}

### 排除的文件（{E} 个）
- `context/shokz.md` — 原因：路径匹配 file_patterns
- `references/brand-data.md` — 原因：敏感关键词命中 12 次

### 脱敏的文件（{R} 个）
- `SKILL.md` — 替换 2 处：Shokz → [YourCompany]
- `context/README.md` — 替换 1 处：Shokz → [YourCompany]

### 原样保留（{K} 个）
[列表省略]
```

**必须暂停**，等用户确认后再继续。用户可以：
- "继续" → 进入下一步
- "排除 X 文件" → 追加排除
- "保留 X 文件" → 取消某个排除
- "取消" → 终止流程

---

## Flow A: 首次发布

保密过滤通过后执行以下步骤。

### A3: 生成 README 骨架

读取本 skill 目录下 [templates/README-skeleton.md](templates/README-skeleton.md) 模板。

基于脱敏后的 SKILL.md 内容和目录结构，填充模板中的占位符，生成 README 骨架（≤ 15 行）。骨架包含：

- 标题 + 一句话描述
- 章节列表（每章一句话摘要）
- 预计的 badges
- 安装命令

向用户展示骨架，**必须暂停**等确认：
> README 骨架如上。回复 **继续** 我写完整版；**调整 + 意见** 我修改后重新确认。

### A4: 写完整 README + CHANGELOG

**README 生成规则**（按顺序输出以下章节）：

1. **标题区**
   - 居中标题（skill 名称的可读形式）
   - 一句话描述（从 SKILL.md description 提炼，脱敏后）
   - Badges：`Agent Skill Compatible`、`License: MIT`
   - 安装命令：`npx skills add {github-user}/{repo-name}`（如果 skills.sh 支持）或手动 clone 指引

2. **核心功能**
   - 从 SKILL.md 提炼 3-5 个核心能力，每条一句话
   - 如 SKILL.md 有 mermaid 流程图 → 直接复用（脱敏后）
   - 如无流程图但有分步流程描述 → 生成 mermaid 图

3. **目录结构**
   - 用 `tree` 格式展示实际上传的文件结构（排除后的）
   - 对关键文件加简要注释

4. **使用示例**
   - 从 SKILL.md 的触发词构造 2-3 个真实用法示例
   - 格式：`> 用户："触发口令"` + 简述 skill 会做什么

5. **配置说明**（仅当 skill 含 context/、config/、或 .yml 配置文件时）
   - 说明哪些文件需要用户自定义
   - 提供修改示例

6. **迭代记录**
   - 链接到 `CHANGELOG.md`

7. **许可证**
   - 默认 MIT

**CHANGELOG 生成规则**：

读取 [templates/CHANGELOG-init.md](templates/CHANGELOG-init.md) 模板，填充：
- 版本号：`1.0.0`
- 日期：当天日期
- Added 列表：从 SKILL.md 提炼的功能点

### A5: 创建 GitHub Repo 并推送

Repo 名确定规则：
- 默认使用 skill 目录名
- 如 Step 2 第一层建议了重命名 → 使用重命名后的名称
- 用户在骨架确认时指定了其他名字 → 使用用户指定的

执行步骤（顺序执行，每步检查退出码）：

```
1. 创建临时工作目录（如果有脱敏文件，使用 .skill-publisher-staging/{skill-name}/）
2. 将原样保留的文件和脱敏副本组装到工作目录
3. 将生成的 README.md 和 CHANGELOG.md 写入工作目录
4. 生成 .gitignore（见下方规则）
5. 生成 LICENSE（MIT，copyright 用 gh 当前用户名）
6. cd 到工作目录
7. git init
8. git add .
9. git commit -m "Initial publish via github-skill-publisher"
10. gh repo create {repo-name} --public --source=. --push
11. 清理 .skill-publisher-staging/ 临时目录
```

### A6: 报告结果

```
发布完成！

📦 Repo: https://github.com/{user}/{repo-name}
📄 README: 已生成（{N} 个章节）
📋 CHANGELOG: v1.0.0
🔒 保密过滤: 排除 {E} 个文件，脱敏 {R} 个文件
```

---

## Flow B: 更新同步

用户说"更新 X skill"时执行。

### B1: 定位本地 skill + 远程 repo

1. 按 Step 1 定位本地 skill 目录
2. 用 `gh repo list` 查找同名 repo（或 skill 目录下有 `.git` 指向的远程）
3. 找不到远程 repo → 问用户是否要走首次发布流程

### B2: 执行保密过滤

与 Step 2 完全相同。对最新本地文件重新执行三层过滤。

### B3: 对比差异

1. Clone 远程 repo 到临时目录
2. 将过滤后的本地文件与远程文件做 diff
3. 分类汇总变更：
   - 新增文件
   - 修改文件（列出关键变更行数）
   - 删除文件（本地不再有的）

### B4: 生成变更摘要

向用户展示：

```
## 变更摘要

**Skill**: {name}
**远程 repo**: {url}
**上次更新**: {date}

### 文件变更
- 新增: {list}
- 修改: {list with line counts}
- 删除: {list}

### 建议 CHANGELOG 条目
## [{new-version}] - {today}
### Changed
- {变更描述 1}
- {变更描述 2}

### README 更新
- {是否需要更新 README，如目录结构变了/新增了功能}
```

**必须暂停**等用户确认。用户可以：
- "继续" → 按建议执行
- "改版本号为 X" → 调整版本号
- "修改 CHANGELOG 条目" → 编辑变更描述
- "取消" → 终止

### B5: 执行更新

```
1. 将过滤后的文件覆盖到 clone 的临时目录
2. 更新 README.md（如需）
3. 追加 CHANGELOG.md 条目（插入到文件头部，已有条目下移）
4. git add .
5. git commit -m "Update via github-skill-publisher: {版本号}"
6. git push
7. 清理临时目录
```

### B6: 报告结果

```
更新完成！

📦 Repo: https://github.com/{user}/{repo-name}
📋 CHANGELOG: {old-version} → {new-version}
📝 变更: {N} 个文件修改, {M} 个文件新增, {D} 个文件删除
🔒 保密过滤: 排除 {E} 个文件，脱敏 {R} 个文件
```

---

## .gitignore 生成规则

首次发布时自动在 repo 根目录生成 `.gitignore`：

```gitignore
# Runtime artifacts
node_modules/
__pycache__/
*.pyc
.DS_Store
Thumbs.db

# Backup files
*.bak.*
*.bak
*.tmp
*.swp

# Generated outputs
result-card-*.html
*.tsv

# Staging directory
.skill-publisher-staging/
```

更新时不覆盖已有的 `.gitignore`（用户可能做了自定义修改）。

---

## 异常处理

| 场景 | 处理 |
|------|------|
| `gh` 未登录 | 报错，给出 `gh auth login` 指引 |
| repo 名已存在（首次发布时） | 问用户：换个名字 / 改为更新流程 / 强制覆盖（危险） |
| push 失败（网络等） | 保留临时目录不清理，提示用户手动重试 `cd {staging} && git push` |
| skill 目录无 SKILL.md | 报错，不是有效的 skill 目录 |
| sensitive-keywords.yml 不存在 | 警告并继续（无过滤），但明确告知用户"本次上传未执行保密过滤" |
| 已有手写 README.md | 问用户：覆盖 / 合并（追加新章节保留旧内容）/ 跳过 README 生成 |
| 已有 CHANGELOG.md | 追加新条目到头部，保留已有条目 |
| 用户说"取消 / 算了" | 清理临时目录，终止流程 |
| 用户说"回退" | 提供 `git revert` 命令让用户手动执行（不自动操作远程 repo 的历史） |

---

## 关键约束

- **本地文件只读**：整个流程不修改用户本地 skill 目录中的任何文件。所有脱敏、README 生成都在临时目录进行。
- **保密过滤不可跳过**：即使用户说"直接上传不用检查"，仍然执行保密过滤。可以让用户确认过滤结果时全部放行，但扫描本身必须执行。
- **确认节点不可跳过**：过滤报告和 README 骨架两个确认点必须等用户明确回复。
- **一次只处理一个 skill**：不支持批量上传。用户想批量操作时，引导逐个执行。
- **README 和 CHANGELOG 默认中英双语**：各生成两个文件（`README.md` + `README.en.md`，`CHANGELOG.md` + `CHANGELOG.en.md`），每个文件顶部加语言切换链接（`[English](*.en.md)` / `[简体中文](*.md)`）。中文版全中文，英文版全英文，不混排。
