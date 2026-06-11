---
name: desktop目录清晰化
overview: 把 desktop/ 的"开发"与"打包"职责通过重命名顶层文件夹 + 一份 README 文件地图划分清楚，清理垃圾文件，并重新打包最新版 exe。
todos:
  - id: del-junk
    content: 删除垃圾文件 desktop/src-tauri/2
    status: completed
  - id: rename-ui
    content: 将 desktop/src/ 重命名为 desktop/ui/
    status: completed
  - id: fix-conf
    content: 修改 tauri.conf.json 的 frontendDist 为 ../ui
    status: completed
  - id: add-readme
    content: 新增 desktop/README.md 文件地图，标注开发/打包职责
    status: completed
  - id: rebuild
    content: 结束运行中的 app.exe，cargo check 后重新 npm run build 打包 exe
    status: completed
isProject: false
---

# desktop 目录清晰化 + 重新打包

## 现状问题

`desktop/` 里文件按 Tauri 默认约定平铺，看不出哪些是"开发时改的"、哪些是"打包用的"。另有一个误操作产生的垃圾文件 `src-tauri/2`。

约束：Tauri 强制要求 `tauri.conf.json`、`Cargo.toml`、`build.rs`、`icons/`、`capabilities/`、`src/*.rs` 全部待在 `src-tauri/` 根目录，物理拆走会导致编译/打包失败。所以 `src-tauri/` 内部的开发/打包分离只能靠 README 文档标注，顶层则通过重命名让界面开发部分一眼可辨。

## 目标结构

```
desktop/
├── ui/                  ← 【开发】前端界面，你平时改这里
│   ├── index.html
│   ├── widget.css
│   └── widget.js
├── src-tauri/           ← 原生外壳 + 打包引擎（Tauri 约定，不可拆）
│   ├── src/             · 【开发】Rust 逻辑 lib.rs / main.rs
│   ├── tauri.conf.json  · 【打包】窗口与安装包配置
│   ├── Cargo.toml/lock  · 【打包】Rust 依赖
│   ├── build.rs         · 【打包】构建脚本
│   ├── icons/           · 【打包】应用图标
│   ├── capabilities/    · 【打包】权限声明
│   └── gen/             · 自动生成，忽略
├── config.json          ← 【开发/运行】默认服务器地址
├── package.json         ← 【打包】构建命令入口
├── package-lock.json
└── README.md            ← 新增：文件地图，标注每项是开发还是打包
```

## 改动清单

### 1. 清理垃圾文件
删除 [desktop/src-tauri/2](desktop/src-tauri/2)（内容是 npm 安装输出，误重定向产生）。

### 2. 重命名 `src/` -> `ui/`
将 `desktop/src/`（含 index.html、widget.css、widget.js）整体改名为 `desktop/ui/`。

唯一需要同步修改的引用在 [desktop/src-tauri/tauri.conf.json](desktop/src-tauri/tauri.conf.json) 第 7 行：
```json
"frontendDist": "../src"   ->   "frontendDist": "../ui"
```
（已确认全项目仅此一处引用 `../src`；`lib.rs` 用的是 `../../config.json`，不受影响。）

### 3. 新增 `desktop/README.md`
一份简短文件地图，分两栏说明：
- 开发时改哪些：`ui/`（界面）、`src-tauri/src/lib.rs`（逻辑）、`config.json`（默认地址）
- 打包相关：`tauri.conf.json`、`Cargo.toml`、`icons/`、`capabilities/`、`package.json`
- 两条命令：`npm run dev`（开发预览）、`npm run build`（打包 exe）

### 4. 根目录大文件夹
已确认根目录干净（只剩 `.cursor`、`desktop`、`web`、`.gitignore`、`README.md`），无需额外清理。

### 5. 重新打包 exe
在 `desktop/` 执行 `npm run build`。打包前需先结束正在运行的 `app.exe` 进程（否则 release 文件被占用会报 os error 5）。

产物：
- `desktop/src-tauri/target/release/bundle/nsis/na-trend-widget_0.1.0_x64-setup.exe`
- `desktop/src-tauri/target/release/bundle/msi/na-trend-widget_0.1.0_x64_en-US.msi`

## 验证
- 改完先 `cargo check` 确认 Rust 编译通过
- 再 `npm run build` 确认安装包正常生成
