---
name: Excel校对桌面Demo
overview: 搭一个本地桌面 app：选母本 Excel + 目标 Excel，锁定到 sheet 内的特定单元格范围做高精度配对，按 document-proofreader skill 的方法论调用云端 LLM，输出可定位、带严重度/置信度的九列校对表并可导出。
todos:
  - id: scaffold
    content: 创建项目骨架：requirements.txt、config.example.json、proofreader 包、ui 目录、README
    status: completed
  - id: sources
    content: 实现 sources/ 文档来源抽象：本地 file dialog provider + 云端 provider 接口(stub, 未配置时置灰)
    status: completed
  - id: excel_scope
    content: 实现 excel_reader.py + scope.py：列 sheet、解析/校验 range、范围预览、列角色检测、抽取范围内带坐标的单元格
    status: completed
  - id: pairing
    content: 实现 pairing.py：范围内按行号/关键列配对，产出带母本+目标坐标的配对单元
    status: completed
  - id: standard
    content: 实现 standard.py：加载三方书写标准(xlsx/docx/md/txt 或文本)抽纯文本 + 说明 + 角色，供 prompt 使用
    status: completed
  - id: evaluation
    content: 实现 rules.py(五维度+维度开关+三方标准边界 system prompt)、prompt.py(启用维度+配对单元+全范围+三方标准, JSON schema)、llm_client.py
    status: completed
  - id: report
    content: 实现 report.py：解析 LLM JSON 为九列 findings、聚类校验、按严重度统计、导出 Markdown / xlsx
    status: completed
  - id: ui
    content: 实现 pywebview 桌面 UI(app.py + ui/*)：三步 stepper、来源切换、三方标准卡片、范围选择、维度勾选(必选锁定)、结果表(筛选/排序/严重度色标)、加载/空/错误态、设置、明暗色
    status: completed
  - id: run_doc
    content: 补 README 运行说明，本地跑通一次完整校对流程
    status: completed
isProject: false
---

# Excel 校对桌面 Demo

## 形态与技术栈
- 桌面 app：`pywebview`（原生窗口）+ Python 后端 + 单页 HTML/CSS/JS 前端。Python 端跑 `openpyxl` 读 Excel、调 LLM；前端负责来源/文件选择、范围设置、结果表格。
- LLM：`openai` SDK，走 OpenAI 兼容接口，`base_url / model / api_key` 在设置面板配置（默认 OpenAI，可指向其他兼容网关）。配置存本地 `config.json`，不入库。
- 只读：绝不写回母本/目标文件（遵循 skill 的 read-only 铁律）。

## 核心数据流
1. 母本、目标各选来源（本地 / 云端）→ 本地 xlsx 路径；可选加载三方书写标准（文件/文本 + 说明 + 角色）
2. 各自选 sheet + 单元格范围（如 `A3:H60`）+ 列角色 + 源-目标关系；勾选参与的评估维度（必选项锁定）
3. 范围内配对（按行号 或 按关键列）→ 配对单元（带坐标）
4. 组装提示词：勾选的维度开关 + 五维度评估规则(system) + 配对单元 + 全范围上下文 + 三方标准及说明(user)
5. 调云端 LLM，返回 JSON findings（含维度/子类型/严重度/置信度/依据）
6. 解析为九列表 + 聚类校验 + 严重度统计，前端展示，可导出 md / xlsx

## 文档来源（本地 + 云端）
母本和目标各有一套独立的来源选择，抽象成统一的 `DocumentSource` 接口，后续接云不改上层逻辑：
- `LocalSource`：调 pywebview 原生文件对话框选本地 `.xlsx`，直接得到路径。第一版可用。
- `CloudSource`（接口先留，未配置）：定义 `list_documents()` 与 `fetch(doc_id) -> 本地临时 xlsx 路径` 两个方法。云端文档统一先下载成本地临时 xlsx，再走同一套读取/范围/配对逻辑——保证云端文档和本地文档在下游完全等价。
- UI：每个文件槽顶部有来源切换（本地文件 / 云端文档）。云端未配置时该选项置灰，并提示"云端来源待配置"，不阻塞本地流程。
- 实现落在 `proofreader/sources/`：`base.py`(接口) + `local.py` + `cloud.py`(stub)。

## 校对评估方法（五维度 + 多层比较，不止一一对应）
评估完全对齐 `document-proofreader` 的五维度模型；"一一对应"只是其中一层。共五层判断，配对级 + 范围级 + 跨版本级都覆盖：

- **A 配对级 · Accuracy（准确性）**：母本↔目标同一单元对比。子类型：`产品事实不一致`（功能/名称/SKU/URL/装箱清单变动）、`参数不一致`（数值/单位/范围/条件，如 25h vs 27h、IP54 vs 全防水）。依赖确定性配对。
- **B 配对级 · Sync（同步）**：关系=翻译/版本时，源已改但目标仍旧。子类型：`源文案未同步`、`旧版本残留`。优先读母本里的变更痕迹（批注、变色、删除线、"已修改/更新为"）。
- **C 范围级 · Consistency（一致性，非一一对应）**：在整个范围内横向扫描，同一概念多种写法/格式。子类型：`术语不统一`（earbuds/earphones 混用、app 名、技术名、动作词）、`格式不统一`（日期/单位/标点/大小写）。需要把全范围内容一起喂模型，而不是逐对比。
- **D 跨版本/跨语言 · Consistency/定位差异**：同一行在 简中/大中华/国际 或多语言列给出不同品类词/口号/卖点，标 `术语不统一` 或定位差异，报告但不一律判错。
- **E 范围与基准 · Scope（范围）**：`不在本轮基准范围`（目标有内容但母本范围未覆盖，暂停问母本）、`基准冲突`（两个基准/源-母本打架）、`基准待确认`（母本是 `?`/`待确认`/`TBD`/空）、`语境差异`（封面短文案 vs 说明书长句等合理差异，标"可接受差异"）。
- **F 语气层 · Tone（语气，事实对但表达不同）**：`风格差异`（更营销/更技术）、`表达强度差异`（fully/best/guaranteed/全防水 等绝对词强化或弱化）、`信息颗粒度差异`（漏掉或多出条件/范围/步骤/限定）。默认不判错，提示确认。

判断质量层（每条 finding 都要过）：
- **聚类**：同维度+同子类型+同根因 = 一条 finding，`位置`列列出全部受影响坐标，不一处一行。
- **证据强制**：`依据` 必须引母本片段+坐标；引不出就降级为 `需确认` + 置信度 `低`，不许判成确定错误（呼应 content-integrity）。
- **严重度 / 置信度 双维**：严重度=错了后果多大(`高/中/低/可接受差异`)；置信度=有多确定是错(`高/中/低`)。不允许全填 `中`。
- **母本完整性预检**：写进 system prompt——先核对母本与目标是否同一产品（型号/品类/形态），不一致先标注再判。

精度设计：把"找哪行对哪行"交给 Python 确定性配对（带坐标），把"这对/这一片差在哪、属于哪一维"交给模型。A/B 用配对单元，C/D/E/F 用全范围上下文，因此提示词同时携带"配对单元"和"范围内全部内容"两份数据。

## 评估维度选择（UI 可勾选 · 分必选/可选）
六个维度在步骤 2 做成勾选项，按下面划分（聚类 / 证据回引 / 严重度+置信度是每条 finding 都跑的质量纪律，不是可勾选维度，不进勾选区）：
- **必选（锁定，不可取消）**：A 准确性、E 范围与基准。前者是校对核心，后者是防"无依据乱判错"的安全网，必须常开。
- **可选 · 默认开**：C/D 一致性（术语/格式/跨版本）、B 同步（仅当源-目标关系=翻译或同语言不同版本时可勾，模板vs填写关系下自动禁用并说明原因）。
- **可选 · 默认关**：F 语气（风格/强度/颗粒度），噪声最大、严重度最低，按需开。

实现：勾选状态进 prompt 的"启用维度"开关，未勾的维度模型不输出该类 findings；前端用 `disabled-states` 表达不可用维度并给说明，必选项以锁定态展示（`read-only-distinction`）。

## 三方书写标准（第三输入）
在母本(标准)、目标(校对对象)之外引入第三个校对依据，对应 skill 的"用户确认的辅助来源"（术语表 / 品牌规范 / 法务措辞）。可选，不填不影响主流程。
- **输入形态（两者都支持，可只用其一）**：
  - 上传标准文件：`.xlsx / .docx / .md / .txt`，由 `proofreader/standard.py` 抽成纯文本喂模型；
  - 文本框：直接粘贴/书写标准条目。
- **书写标准的说明**：一个必填的说明文本框（只要启用了三方标准就必填），让用户写清这份标准"管什么、权威到什么程度"。同时 UI 内置 helper text 解释"三方标准是什么、会怎么被使用"。
- **角色标注**：勾选这份标准约束哪些维度——`术语` / `格式` / `语气` / `法务`。模型只在被勾的角色内把它当权威，不越权（遵循 skill 的"auxiliary sources used only within confirmed role"）。
- **对判断的影响**：有了标准/术语表，原本"无官方译法→只能给一致性建议"的术语类 finding 可以引标准作权威、置信度给到 `高`；`依据` 列改为引标准片段+位置。法务/格式同理。没有勾到的维度，标准不参与。
- 进 prompt 的结构：system 增加"如何使用三方标准 + 角色边界"段；user 增加"三方标准内容 + 用户说明 + 角色"块。

## 文件结构
- `app.py` — pywebview 入口，暴露给 JS 的 `Api` 类（选来源、列 sheet/范围预览、跑校对、导出、读写配置）
- `proofreader/sources/base.py` `local.py` `cloud.py` — 文档来源抽象：本地 file dialog + 云端 stub，统一产出本地 xlsx 路径
- `proofreader/excel_reader.py` — 读工作簿结构（改写自 `_skill_ref/scripts/extract_workbook_outline.py`），列 sheet、建议表头行、检测列
- `proofreader/scope.py` — 解析/校验 range 字符串，抽取范围内单元格（坐标+值），输出预览
- `proofreader/pairing.py` — 范围内按行号 / 关键列配对，产出带坐标的配对单元
- `proofreader/standard.py` — 加载三方书写标准（xlsx/docx/md/txt 或文本）抽成纯文本 + 说明 + 角色，供 prompt 使用
- `proofreader/rules.py` — 把五维度模型、维度开关说明、三方标准使用边界、严重度/置信度锚点、聚类、证据规则压成 system prompt
- `proofreader/prompt.py` — 拼 user prompt（启用维度 + 配对单元 + 全范围上下文 + 三方标准及说明），约定 JSON 输出 schema
- `proofreader/llm_client.py` — OpenAI 兼容客户端，超时/报错处理
- `proofreader/report.py` — 解析 LLM JSON → findings；聚类校验；导出 Markdown / xlsx
- `ui/index.html` `ui/style.css` `ui/app.js` — 三步式界面
- `config.example.json` `requirements.txt` `README.md`

## UI/UX 设计（参考 ui-ux-pro-max）
该 skill 偏移动端，这里只取对桌面 Web 适用的规则。整体定位：专业、克制的桌面数据工具，单一主操作，明暗双色。

整体框架与信息架构：
- 左侧竖向 **3 步 stepper**（来源与文件 → 范围与关系 → 结果），当前步高亮（`nav-state-active`）；右侧主内容区。导航位置全局一致（`navigation-consistency`）。
- 每屏只有一个主 CTA（`primary-action`）：步骤 1/2 是"下一步"，步骤 2 末是"开始校对"。次级操作（设置、导出）视觉降级。
- 顶部右上角设置入口：API 配置（base_url/model/key）、明暗切换。

视觉与排版（§4/§6）：
- 语义色 token（primary/surface/on-surface/danger/warning/success），不在组件里写死 hex（`color-semantic`）；明暗各调一套，独立验证对比度（`color-dark-mode`）。
- 正文 ≥14px、行高 1.5；数据/坐标列用等宽数字（`number-tabular`）防止表格抖动。图标用 SVG（Lucide），不用 emoji（`no-emoji-icons`）。

步骤 1 来源与输入：
- 母本、目标两个卡片，各有来源切换（本地文件 / 云端文档，云端置灰提示）。选完显示文件名、大小、sheet 数。
- 第三个卡片"三方书写标准（可选）"：来源切换（上传文件 / 文本框），启用后必填"说明"，并勾选角色（术语/格式/语气/法务）；内置 helper text 解释它是什么、怎么被用。

步骤 2 范围 · 关系 · 维度（核心交互）：
- 每个文件：**sheet 下拉**（切换即刷新预览）+ **范围**（A1 输入框校验回显行列数 / "用已用区域"一键填充，拖选作为增强项）+ **列角色**（表头每列下拉：关键列/源列/目标列/忽略，后端给默认建议）。
- **源-目标关系**单选（翻译 / 同语言不同版本 / 模板vs填写）+ **配对方式**单选（按行号 / 按关键列）。
- **评估维度勾选区**：A 准确性、E 范围与基准 锁定常开；C/D 一致性、B 同步 默认勾选（B 在模板vs填写关系下置灰）；F 语气 默认不勾。每项配一句作用说明。
- 预览网格只读，前 N 行 × 实际列；选完实时回显"已选 N 行 × M 列，关键列=X，源列=Y，目标列=Z"（`success-feedback`）。
- 表单规范：可见 label 不靠 placeholder（`input-labels`）；range 非法时在字段下方就近报错并说明怎么改（`error-placement`/`error-clarity`）；blur 时校验（`inline-validation`）。

步骤 3 结果（数据表，§8/§10）：
- 九列表：文件 / 位置 / 原文 / 建议 / 维度 / 子类型 / 严重程度 / 置信度 / 依据。
- 严重度用 **颜色 + 图标 + 文字**三重编码，不只靠颜色（`color-not-only`）；表头吸顶；可按严重度/维度筛选、按列排序（`sortable-table`）；`依据` 长文用展开/tooltip（`truncation-strategy`）；行数多时虚拟滚动（`virtualize-lists`）。
- 顶部统计条：高 x / 中 x / 低·可接受 x / 不在范围 x / 低置信度 x（来自 report.py）。
- 导出 md / xlsx 按钮（`export-option`）。

状态与反馈（§2/§8）：
- LLM 调用 >1s，用骨架/进度条而非空转 spinner（`progressive-loading`）；调用中禁用"开始校对"按钮并显示进行态（`loading-buttons`）。
- 空态：未选文件/无差异时给明确文案+下一步指引（`empty-states`），"无差异"是合法结果不编造。
- 错误恢复：API 失败给原因 + 重试入口（`error-recovery`）。

可访问性（§1）：正文对比度 ≥4.5:1；交互元素可见 focus ring（`focus-states`）；全键盘可达、Tab 顺序合理（`keyboard-nav`）；图标按钮带 aria-label。

动效（§7）：步骤切换/展开 150–300ms，ease-out 进、ease-in 出；尊重 `prefers-reduced-motion`。

## 范围选择 · 后端接口
`app.py` 暴露给前端：`list_sheets(path)`、`preview_range(path, sheet, range)`、`detect_columns(path, sheet, range)`；范围解析与单元格抽取落在 `scope.py`，母本与目标各一套独立状态、互不影响。

## 范围与取舍
- 第一版聚焦 Excel↔Excel、单范围对单范围、一次跑完（不做 skill 的多文件分批暂停，因为这是单机工具非对话）。
- skill 的"母本完整性检查/基准冲突/不在范围"等仍写进 system prompt，让模型在输出里标注，但不做交互式 STOP。
- 暂不打包 .exe；先 `python app.py` 跑通 demo，后续可加 PyInstaller。