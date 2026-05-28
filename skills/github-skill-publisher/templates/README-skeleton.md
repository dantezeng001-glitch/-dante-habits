# README 骨架模板

生成 README 骨架时，按以下结构填充占位符，输出给用户确认。
骨架控制在 15 行以内，每个章节只保留一句话摘要。

---

## 骨架格式

```markdown
# {skill_display_name}

{one_line_description}

## 章节预览

1. **核心功能** — {core_capabilities_summary}
2. **架构/流程** — {architecture_summary: "含 mermaid 图" 或 "从描述生成流程图" 或 "无"}
3. **目录结构** — {file_count} 个文件，{dir_list}
4. **使用示例** — {example_count} 个口令示例
5. **配置说明** — {config_summary: "含 context/ 配置" 或 "无需配置" 或 "含 .yml 配置"}
6. **CHANGELOG** — v1.0.0 首次发布

## Badges
- Agent Skill Compatible
- License: MIT

## 安装
`npx skills add {github_user}/{repo_name}` 或 clone 指引
```

---

## 填充规则

- `{skill_display_name}`: 将 skill 目录名转为可读形式（kebab-case → Title Case，如 `product-development` → `Product Development`）
- `{one_line_description}`: 从 SKILL.md frontmatter 的 description 字段提取第一句（脱敏后）
- `{core_capabilities_summary}`: 从 SKILL.md 正文提炼，≤ 20 字
- `{architecture_summary}`: 检查 SKILL.md 是否包含 mermaid 代码块
- `{file_count}`: 过滤后实际上传的文件数
- `{dir_list}`: 顶层子目录列表
- `{example_count}`: 从触发词推导的示例数（通常 2-3 个）
- `{config_summary}`: 扫描是否有 context/、config/、*.yml 等配置文件
- `{github_user}`: 从 `gh api user -q .login` 获取
- `{repo_name}`: 确认后的 repo 名称

---

## 完整版展开规则

用户确认骨架后，按 SKILL.md 中 "A4: 写完整 README + CHANGELOG" 的 7 个章节逐一展开。

展开时参考质量标准：
- 标题区居中排版，带 badges
- 流程图使用 mermaid 语法（GitHub 原生渲染）
- 目录树用 code block + tree 格式
- 使用示例用引用块格式
- 不堆砌内容，每个章节只放该章节该放的信息（参见 no-redundant-writing 规则）
