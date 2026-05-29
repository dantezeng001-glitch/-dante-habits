---
name: 前端体验审查
overview: 对 `前端开发` 目录按 Vercel Web Interface Guidelines 做了一轮审查。建议优先修复可访问性反馈、长列表渲染、Markdown 链接协议校验和表单细节，再考虑源文件预览等增强。
todos:
  - id: a11y-feedback
    content: 补 `#app-status` 状态播报、路由切换聚焦、评论表单错误聚焦
    status: completed
  - id: markdown-security
    content: 限制 Markdown 链接协议，防止危险 href 进入页面
    status: completed
  - id: pagination
    content: 为文档列表和搜索结果增加分页或加载更多
    status: completed
  - id: form-polish
    content: 补表单 autocomplete、占位符省略号、加载文案统一
    status: completed
  - id: motion-touch
    content: 补 prefers-reduced-motion 和 touch-action 规则
    status: completed
isProject: false
---

# 前端体验审查改进计划

## 优先级判断
当前方案适合作为零依赖 MVP，但要继续给团队长期使用，需要先补齐“可访问、可扩展、可控风险”三件事。

## 建议改动范围
- `前端开发/static/app.js`：补路由切换后的主内容聚焦、aria-live 状态更新、表单错误聚焦、列表分页或限制数量、中文化加载文案。
- `前端开发/static/markdown.js`：限制 Markdown 链接协议，只允许 `http:`、`https:`、`mailto:`、相对路径；避免 `javascript:` 等危险链接。
- `前端开发/static/index.html`：保留现有 skip link 和 status region，但让 `app.js` 实际写入 `#app-status`。
- `前端开发/static/app.css`：补 `prefers-reduced-motion`、`touch-action: manipulation`、移动端正文/表格溢出体验。
- `前端开发/kb_backend.py`：给 `/api/documents` 和 `/api/search` 增加 `limit/offset`，避免一次返回全部文档。

## 推荐实施顺序
1. 先修安全与可访问性：Markdown 链接协议、路由焦点、aria-live、表单错误聚焦。
2. 再修性能：后端分页参数 + 前端列表分页或“加载更多”。
3. 再修体验细节：占位符、加载省略号、日期/数字格式、移动端触控和 reduced motion。
4. 最后做增强：源 PDF/Excel 预览，前提是源二进制文件重新进入知识库。