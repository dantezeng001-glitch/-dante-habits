# Output Templates

Use the template that matches the chosen route. Choose Lightweight or Full based on confidence and complexity.

## Template Selection

| Condition | Template |
| --- | --- |
| High confidence + single route (no combination) | Lightweight Recommendation |
| Medium/low confidence OR combination route | Full Recommendation |

## Lightweight Recommendation

Use when the route is obvious and single-layered. Do not over-engineer simple cases.

```markdown
# AI工具选型建议

## 需求理解
- 任务：
- 输入 → 输出：
- 频率：
- 置信度：__%

## 推荐路线
- 环境：文本 / Browser Agent / Coding Agent
- 控制：Prompt / Skill / Workflow
- 知识层：无 / RAG / 企业知识
- 一句话理由：

## 实现难度与前提
- 难度：★~★★★★★
- 前提条件：

## 具体执行方案
（放对应路线的产物）

## 什么时候该换路线
- 升级信号：
- 降级信号：
```

## Full Recommendation

Use when confidence is medium/low, the route is a combination, or trade-offs need explanation.

```markdown
# AI工具选型建议

## 1. 需求理解
- 当前任务：
- 输入：
- 期望输出：
- 频率/耗时：
- 当前痛点：
- 置信度：__%

## 2. 三轴判断
- 环境判断（Decision A）：文本 / Browser Agent / Coding Agent → 依据：
- 控制判断（Decision B）：Prompt / Skill / Workflow → 依据：
- 知识判断（Overlay）：无 / RAG / 企业知识 → 依据：

## 3. 推荐路线
最终路线 = 环境 × 控制 × 知识

## 4. 实现难度评估
- 综合难度：★~★★★★★
- 用户能力匹配：
- 如难度不匹配的降级方案：

## 5. 为什么不是其他路线
| 路线 | 不推荐原因 |

## 6. 具体执行方案
（放对应路线的产物）

## 7. 验证方法
（用户如何用一次小测试确认路线正确）

## 8. 什么时候该换路线
- 升级信号：
- 降级信号：

## 9. 仍需确认的假设
| 假设 | 影响 | 如何验证 |
```

## AI Chat Output

````markdown
## 推荐工具类型
通用 AI Chat。示例：ChatGPT / Gemini / 豆包 / Claude 等。

## 可直接使用的Prompt
```text
你是一名[角色]。我要完成[任务]。

背景：
[业务背景]

输入：
[粘贴或描述输入]

请你输出：
1. [输出项1]
2. [输出项2]
3. [输出项3]

要求：
- [格式要求]
- [判断标准]
- [语言/风格要求]
- 如果信息不足，先问我最多3个关键问题。
```

## 什么时候该升级
- 同样的上下文复制粘贴 ≥ 3 次 → 升级为 Skill
- 需要 AI 操作网页 → 升级为 Browser Agent
- 交付物需要是文件/代码 → 升级为 Coding Agent
````

## Skill Output

```markdown
## 推荐工具类型
制作 Skill。

## 下一步加载
读取 `references/skill-creation-guide.md`，再产出 skill brief 或完整 skill 文件夹。

## Skill草案
- 名称：
- 触发场景：
- 输入：
- 输出：
- 必读上下文：
- 工作流程：
- 质量检查：
- 示例请求：

## 是否需要文件化
如果用户确认，创建：
- `SKILL.md`
- `references/[domain].md`（如需要）
- `agents/openai.yaml`（如在 Codex 使用）
- 打包为 `[skill-name].zip`（如需要分享）

## 什么时候该换路线
- 规则每次都在变，没有稳定模式 → 降级为 Prompt
- 出现审批/系统集成/跳步出事 → 升级为 Workflow
```

## Workflow Output

```markdown
## 推荐工具类型
工作流 / Bot / 自动化平台。
示例平台：Dify、扣子、钉钉机器人/AI助手、n8n、Make、Zapier、内部工作流平台等。

## 节点设计
| 节点 | 作用 | 输入 | 输出 | 执行者（AI/人/系统） | 失败处理 |

## 决策规则
| 条件 | 去向 | 说明 |

## 人工确认点
| 节点 | 用户确认什么 | 不确认会怎样 |

## 测试用例
| 用例 | 输入 | 预期输出 |

## 什么时候该降级
- 实际没有审批/集成需求，只是"有步骤" → 降级为 Skill + 人工兜底
```

## Enterprise Knowledge / RAG Output

```markdown
## 推荐工具类型
知识库 / RAG 方案。

## 适用原因
（说明为什么内部知识不是简单粘贴上下文能解决）

## 知识场景判断
- 简单查阅/问答：优先企业内部知识搜索。
- 知识驱动工作流/Agent：使用知识库/RAG + 工作流/Agent。
- 定制应用/复杂权限/多源知识：使用自定义 RAG + AI 编程工具搭建。

## 知识源清单
| 知识源 | 位置 | 权限要求 | 是否需要引用来源 |

## 验证问题集
| 问题 | 期望引用来源 | 合格标准 |

## 风险与边界
- 权限隔离：
- 知识过期：
- 引用准确性：
- 人工确认点：

## 什么时候该降级
- 实际只用几份文档且不再增长 → 降级为粘贴上下文
```

## Browser Agent Output

````markdown
## 推荐工具类型
AI 浏览器代理。
示例：ChatGPT agent mode、Cursor browser、各类浏览器自动化 Agent 等。

## 适用原因
（说明为什么需要浏览器环境，而不是粘贴文本或代码工具）

## 执行Prompt
```text
你是浏览器执行代理。目标是：[目标]。

你可以：
- 打开网页：
- 搜索：
- 点击和填写：
- 提取信息：

约束：
- 不要提交/付款/删除/群发，除非我明确确认。
- 遇到登录、验证码、权限或高风险操作时暂停。
- 每完成一个阶段汇报当前结果和下一步。

输出格式：
[表格/清单/摘要/文件]
```

## 准备事项
- 需要登录的网站：
- 需要提供的数据：
- 需要人工确认的动作：

## 什么时候该升级
- 抓取后需要复杂数据处理/生成文件 → 加 Coding Agent
- 每周重复且规则固定 → 加 Skill 打包规则
````

## Coding Agent Output

````markdown
## 推荐工具类型
AI 编程工具 + Skills。
示例：Codex / Claude Code / Cursor / Windsurf 等。

## 适用原因
（说明为什么需要读写文件、运行代码、处理多文件数据或构建demo）

## Coding Agent Handoff Prompt
```text
你是实现代理。请先阅读需求和现有项目结构，再制定最小可运行方案。

目标：
[目标]

输入材料：
[PRD/需求摘要/样例文件/数据源]

交付物：
- 可运行代码
- README
- 样例数据
- 验收步骤

约束：
- 优先本地可运行
- 外部依赖默认Mock
- 不要在未验证前声称完成
- 完成后运行测试或手动验收路径
```

## 下一步
如果这是产品 demo，读取 `references/demo-build-branch.md`；需要生成详细 PRD、技术文档、Mock、验收或 README 时，再读取 `references/product-demo-templates.md`。

## 什么时候该降级
- 生成的脚本只用了一次就没再用 → 降级为 Chat
````
