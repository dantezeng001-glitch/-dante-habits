---
name: PDF 校对标注
overview: 用 PyMuPDF 在目标 PDF 上为全部 17 条校对发现添加高亮 + 批注气泡，输出带标注的新 PDF 文件。
todos:
  - id: install-pymupdf
    content: 安装 PyMuPDF 库
    status: completed
  - id: write-script
    content: 编写标注脚本，含 17 条 finding 定义 + 搜索/高亮/批注逻辑
    status: completed
  - id: run-and-verify
    content: 运行脚本生成标注 PDF 并验证
    status: completed
isProject: false
---

# PDF 校对标注方案

## 技术路径

使用 Python + PyMuPDF (`fitz`) 库，在目标 PDF 的对应位置添加：
- **黄色高亮**：标记问题文字
- **批注气泡**（Text Annotation / Sticky Note）：显示问题描述、建议修改、严重程度

## 输入输出

- **输入**: `OpenTri(S710)线上说明书-英文 240905.pdf`（原文件不修改）
- **输出**: 同目录下生成 `OpenTri(S710)_校对标注.pdf`

## 标注颜色按严重程度区分

- 高严重程度：红色高亮
- 中严重程度：橙色高亮
- 低严重程度：黄色高亮

## 17 条 finding 的文本搜索策略

每条 finding 在对应页面上搜索关键文本片段定位位置：

| # | PDF 页码（0-indexed） | 搜索文本 |
|---|---|---|
| 1 | 20, 25, 27, 30 | "Audrey say" |
| 2 | 34 | "when you in" |
| 3 | 29 | "so that to confirm" |
| 4 | 11, 14 | "MP" (标题区域，搜索附近文本定位) |
| 5 | 33 | "thecorresponding" |
| 6 | 34 | "use with earplugs" |
| 7 | 36 | "Contact authorized" |
| 8 | 2 "countries.Google", 34 "corrosion.Please" |  |
| 9 | 23 "8.Turn", 24 "9.Turn" |  |
| 10 | 20 | 搜索中文句号 |
| 11 | 23, 24 | 搜索中文冒号 |
| 12 | 33 | "headset" |
| 13 | 13 | "OpenTri :" |
| 14 | 9 | "Click once", "Click Once" |
| 15 | 6 | "Volume+" |
| 16 | 17 | "Standard mode:" |
| 17 | 15, 18 | "Audrey will say :" |

对于 #4（MP3 乱码），因 PDF 内部编码可能无法文本搜索，备选方案是在该页顶部添加批注指向标题区域。

## 实现步骤

1. 安装 PyMuPDF（`pip install PyMuPDF`）
2. 编写 Python 脚本 `annotate_proofread.py`，包含：
   - 17 条 finding 的数据结构（页码、搜索文本、批注内容、严重程度颜色）
   - 对每条 finding：在指定页面搜索文本 -> 添加高亮 -> 在高亮区域旁添加批注
   - 搜索失败时回退到页面顶部放置批注
3. 运行脚本，生成标注后的 PDF
4. 验证输出文件可正常打开、标注可见
