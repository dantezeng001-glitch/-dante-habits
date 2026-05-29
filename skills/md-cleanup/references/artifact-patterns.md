# 协作文档导出的伪影清单

收录各家富文本协作文档导出为 MD 后常见的伪影模式。当前仅基于钉钉样本；飞书 / Notion / Google Docs 占位待补。

发现新模式时，按"来源 / 模式 / 归属家族 / 样本"四列记录。脚本能否自动化由家族决定（见 [SKILL.md](../SKILL.md)）。

---

## 钉钉（DingTalk）

来源样例：2026 北美区域游泳 IMC 项目书.md（2026-04-20 清洗）

| # | 模式 | 家族 | 样本 | 清洗后 |
|---|---|---|---|---|
| D1 | LaTeX 着色包裹 @ 提及 | F3.1 | `$\color{#0089FF}{@欧丰硕(Elliott)}$` | `@欧丰硕(Elliott)` |
| D2 | LaTeX 着色包裹普通文字 | F3.1 | `$\color{#FF0000}{红色强调}$` | `红色强调` |
| D3 | `:::` 块容器（warning / info / 自定义） | F3.2 | `:::\n内容\n:::` | `内容` |
| D4 | 链接文案前缀 | F4 | `[请至钉钉文档查看附件《文档名》](https://alidocs.dingtalk.com/...)` | `[《文档名》](https://...)` |
| D5 | 不必要的 `\-` `\*` `\_` 转义 | F2 | `\- 列表项` / `\*斜体\*` / `\_下划线\_` | `- 列表项` / `*斜体*` / `_下划线_` |
| D6 | 表格单元格内嵌套有序列表被展平 | F3.4（agent） | `1.  a<br>    <br>2.  b` | `① a<br>② b` 或语义化改写 |
| D7 | 标题层级全部 `#` 一级 | F5.1（agent） | 全文 `# 项目组成员` `# 立项材料` `# 项目背景` 并列 | 按语义重建 H1/H2/H3 |
| D8 | 空 section（标题后无内容） | F5.4（agent） | `# 立项材料\n\n# 项目背景` 之间空 | 加 `_（待补充）_` 占位或合并 |
| D9 | 阿里云 OSS 长 URL 内联图片 | 无需清洗 | `![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/.../xxx.png)` | 保留原样 |

### 典型清洗收益

钉钉项目书（396 行）清洗后约 347 行，可读性收益主要来自：

- 标题层级重建（H1 变成 H1 + 多个 H2）
- `$\color{}{}$` 从全文大量出现变成 0
- `:::` 围栏块删除
- 链接文案去前缀
- 多重空行压缩

---

## Excel 抽取（openpyxl / excel_sync.py 默认输出）

来源样例：2026 北美广告命名规范.xlsx（2026-04-20 清洗）

9 张 sheet、合计约 700 条数据行，旧 `excel_sync.py` 输出 key-value 竖排，MD 总行数约 4700；改表格格式后降到约 670 行。

| # | 模式 | 家族 | 样本 | 清洗后 |
|---|---|---|---|---|
| E1 | 每行数据被抽成 `### 第 N 行` + 一堆 `- 字段: 值` | F5.5（agent） | 见下方 Before / After | 折叠为单个 Markdown 表格 |
| E2 | 表格单元格含真实 `\n`（多行表头没转义） | F5.6（agent） | `\| 受众人群\nINT:直接关键词\nRMKT:... \|` | `\| 受众人群<br>INT:直接关键词<br>RMKT:... \|` |
| E3 | 纯空占位列（列名 `column_N` 且整列为空） | F5.5 剪枝步 | — | 删除该列 |
| E4 | 合并单元格没展开，平台列只在每组首行有值，其他行为空 | 归 file-sync 抽取层 | `Meta / "" / "" / Google / ""` | file-sync 展开 `ws.merged_cells.ranges` 让每行都有值 |
| E5 | 表头检测被合并横幅顶掉，数据行被当 header | 归 file-sync 抽取层 | 真表头在 row 2，row 1 是 "@某某 的备注" | file-sync 用"自上而下首个 ≥2 非空 + 唯一度 ≥ 0.7 的行" |

### E1 典型 Before / After

Before（37 行数据 → 290 行 MD）：

```
### 第 2 行

- `项目类型`: AO
- `人群/关键词类型`: INT
- `广告组完整命名`: AO_INT_Collections-Page_test

### 第 3 行

- `项目类型`: Launch
- `人群/关键词类型`: ASC
- `广告组完整命名`: Launch_ASC_Pillar-Page-Openear_
```

After（37 行数据 → 48 行 MD，-83%）：

```
| 项目类型 | 人群/关键词类型 | 广告组完整命名 |
|---|---|---|
| AO | INT | AO_INT_Collections-Page_test |
| Launch | ASC | Launch_ASC_Pillar-Page-Openear_ |
```

### 交叉引用

E4 / E5 属于 file-sync 抽取层的缺陷，md-cleanup 能修但每次都手修成本高。永久解决方案见 file-sync/SKILL.md 的 "Excel 已知抽取伪影"。

---

## 飞书（Feishu / Lark）

_待补充样本。_ 已知可能的模式：

- [ ] 飞书的 @ 提及语法（待确认是否也用 `$\color{}$` 或其他形式）
- [ ] 飞书 callout 块的 MD 表达
- [ ] 飞书表格的嵌套列表展开格式

---

## Notion

_待补充样本。_ 已知可能的模式：

- [ ] Notion callout 块（`> 💡 ...`）
- [ ] Notion toggle 块（展开 / 折叠 MD 表达）
- [ ] Notion database embed 的 MD 残留
- [ ] Notion 页面 link 的长 URL 格式

---

## Google Docs

_待补充样本。_ 已知可能的模式：

- [ ] Google Docs 评论脚注 MD 表达
- [ ] 彩色字 MD 表达（可能也是 `$\color{}$` 或 `<span style>`）
- [ ] 文档内链接的 redirect URL

---

## Quip / Confluence / 其他

待按需扩展。
