---
name: listing-page-scan
description: >-
  将网页完整截取为一张连续长图（PNG）。自动处理弹窗关闭、懒加载触发、
  "View More"展开、fixed/sticky 元素修正。逐屏滚动截图后拼接，
  不破坏轮播等依赖视口高度的布局。
  当用户给出一个 URL 并要求扫描、截图、截全页、打印网页、
  抓取页面长图、购买页扫描时触发。
---

# 购买页扫描（Listing Page Scan）

将任意网页截取为一张完整的连续长图。

## 前置依赖

脚本位于 `~/.cursor/skills/listing-page-scan/scripts/screenshot.mjs`，
运行需要 `puppeteer-core` 和 `sharp`。

首次使用或依赖缺失时，在脚本所在目录执行：

```bash
cd ~/.cursor/skills/listing-page-scan/scripts
npm install puppeteer-core sharp
```

脚本通过 `puppeteer-core` 调用系统已安装的 Edge 或 Chrome，不额外下载 Chromium。

## 使用方法

```bash
node ~/.cursor/skills/listing-page-scan/scripts/screenshot.mjs "<URL>" ["<输出目录>"]
```

- **URL**（必填）：目标网页地址
- **输出目录**（可选）：PNG 保存位置，默认为用户桌面

输出文件名自动从 URL 路径生成：`screenshot-<slug>.png`

## 工作流

收到用户的扫描/截图请求后：

1. 确认目标 URL
2. 检查依赖是否就绪（`node_modules` 是否存在），缺失则安装
3. 执行脚本，等待完成
4. 告知用户文件路径、像素尺寸、文件大小

## 脚本内部流程

1. 启动 headless Edge/Chrome（视口 1440×900）
2. 加载页面（`networkidle2`，60s 超时兜底）
3. 关闭弹窗 — 隐藏 `z-index > 999` 或覆盖 >50% 视口的 fixed 蒙层
4. 展开 "View More" / "查看更多" / "Show More" 等折叠区域
5. 全页滚动一遍触发懒加载，等待图片就绪
6. 冻结 CSS 动画；`fixed` 元素隐藏，`sticky` 元素转 `relative`
7. 逐 900px 滚动截图，最后一屏裁掉重叠部分
8. 用 sharp 垂直拼接所有分片，输出 PNG

## 常见问题

| 现象 | 原因 | 处理 |
|------|------|------|
| 产品主图消失 | sticky 容器被 `display:none` | 已改为 `position:relative`，不隐藏 |
| 轮播图重叠 | `fullPage:true` 拉伸视口破坏布局 | 已改用逐屏截图+拼接 |
| 弹窗残留 | 弹窗延迟弹出 | 脚本等待 3s 后再清理 |
| 图片空白 | 懒加载未触发 | 全页滚动 + 8s 超时等待 |
