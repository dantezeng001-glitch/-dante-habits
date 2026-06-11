---
name: fix-autostart-path
overview: 开机自启注册表项仍指向已删除的开发版 exe，导致开机启动失败。修复方法是让正式版重新登记自启，使注册表项指向新安装的正式版 app.exe。
todos:
  - id: relaunch-register
    content: 运行正式版 app.exe，通过托盘"开机自启"先关再开，重新登记为正式版路径
    status: completed
  - id: verify-registry
    content: 只读检查注册表 na-trend-widget 值已指向正式版 exe、文件存在、StartupApproved 为启用
    status: completed
  - id: equivalent-boot-test
    content: 直接执行注册表中的启动命令，验证能拉起正式版托盘（等价开机测试）
    status: completed
  - id: optional-reinstall
    content: 可选：重装到非 OneDrive 路径以避免按需同步导致文件缺失
    status: pending
isProject: false
---

# 修复开机自启：让注册表项指向正式版

## 诊断结论（已验证）

- 注册表 `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` 下 `na-trend-widget` 的值仍是开发版路径：`...\desktop\src-tauri\target\debug\app.exe`（且带尾随空格）。
- 该 debug 文件**已不存在** → 开机启动一个缺失文件，静默失败。
- 正式版 `c:\Users\016551\OneDrive\Desktop\na-trend-widget\app.exe` 存在，但从未登记进自启。
- 该启动项在 Windows 中是"启用"状态（StartupApproved = `02`），不是被禁用。

## 修复方案（主：用正式版自身重新登记）

让插件自己写注册表，能保证写入格式与 `is_enabled()` 校验一致，避免手改格式不匹配：

1. 双击运行正式版 `c:\Users\016551\OneDrive\Desktop\na-trend-widget\app.exe`，托盘出现图标。
2. 右键托盘菜单 -> "开机自启"。因为现存同名项指向的是 debug 旧路径，`is_enabled()` 可能判定为"未启用"或状态不一致，所以建议**先点一次（关），再点一次（开）**，确保最后一次是 `enable()`，用正式版 `current_exe()` 路径覆盖旧项。

> 备选（若托盘开关行为不确定）：直接重写注册表值为正式版路径。风险是 auto-launch 对值的格式（是否带引号/尾随空格）有预期，手写格式不一致会让 app 内 `is_enabled()` 显示状态不符。因此优先用上面的 app 自身开关。

## 验证（我可在你操作后跑只读检查）

- 注册表 `na-trend-widget` 值已变为含 `na-trend-widget\app.exe` 的正式版路径。
- 该 exe 存在；StartupApproved 仍为 `02`（启用）。
- 等价开机测试：直接执行注册表里那条命令，确认能拉起正式版托盘（昨天用过的方法，不必真重启）。

## 可选加固：安装路径不在 OneDrive 下

正式版被装在 `OneDrive\Desktop\na-trend-widget`。若 OneDrive 启用"按需同步/释放空间"，开机时该 exe 可能被 dehydrate 到云端，本地无文件 -> 自启再次失败。
- 建议：卸载后用安装包重装到默认非 OneDrive 路径（NSIS 默认 `%LOCALAPPDATA%\na-trend-widget`），再按上面步骤开自启。
- 此项不影响"先把自启修好"，可后续再做。