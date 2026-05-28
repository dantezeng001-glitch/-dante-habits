# CHANGELOG 模板

生成 CHANGELOG 时按此模板填充。遵循 [Keep a Changelog](https://keepachangelog.com/) 格式。

---

## 首次发布模板

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] - {YYYY-MM-DD}

### Added

{feature_list}
```

---

## 更新追加模板

每次更新时，在已有内容的 `## [1.0.0]` 之前插入新条目：

```markdown
## [{new_version}] - {YYYY-MM-DD}

### Added
{new_features}

### Changed
{modifications}

### Removed
{deletions}
```

仅保留有内容的分类（Added/Changed/Removed），空分类不输出。

---

## 填充规则

- `{YYYY-MM-DD}`: 执行当天日期
- `{feature_list}`: 从 SKILL.md 提炼功能点，每条一行，以 `- ` 开头
- `{new_version}`: 基于变更类型递增
  - 新增功能 → minor 版本 +1（如 1.0.0 → 1.1.0）
  - 仅修改/修复 → patch 版本 +1（如 1.0.0 → 1.0.1）
  - 用户可在确认时自定义版本号
- `{new_features}` / `{modifications}` / `{deletions}`: 从 diff 摘要提炼
