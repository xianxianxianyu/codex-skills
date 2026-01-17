# Skillpack skills 重叠/冲突分析与优化建议

本文重新聚焦在“主要重叠/冲突簇”以及它们的**融合式处理方法**：目标不是删除某个 skill，而是把多个 skill 组织成分工明确、可复用的组合工作流。

权威清单（name → location）：`E:\OS\skillpack\skills-index.md`

---

## 冲突的语义根因：一句话里混了多个维度

在 Codex 里，自动选 skill 的信号来自你的输入语义与 skill 的 `description`。当你说“写文档/做 UI/做评测/做 agent”，通常同时包含：
- 产物（What）：最终要落到文件系统里的是什么？
- 阶段（When）：现在是结构/内容/风格/验证中的哪一步？
- 约束（How）：受众、是否可运行、是否要回归/偏差控制等

同一条输入如果没把这三点说清楚，就会让“多个 skill 看起来都对”。

---

# 第 1 章（维护者视角）：把冲突簇变成“角色 + 交接产物”的组合协议

## 1.1 维护者总规则：一个阶段只能有一个 Primary

把每个 skill 放进一个角色槽位里，冲突就会变成协作：
- Primary（结构/决策）：同一阶段只允许一个
- Research（资料/枚举）：扩展候选空间
- Styling（主题/模板）：最后叠加，不当 Primary
- Verification（验证/门禁）：对产物做检查/测试/偏差校准

融合的关键在于：明确交接产物（上一阶段输出什么文件，下一阶段在这些文件上继续）。

---

## 1.2 文档/写作簇：把“写文档”分层而非二选一

典型 skills：`prd-taskmaster`、`doc-coauthoring`、`scientific-cs-writing`、`digital-brain`、`theme-factory`

语义拆解（为什么会重叠）：
- PRD：对齐需求/范围/验收（决策与优先级）
- 工程文档：对齐方案/权衡/边界（设计与风险）
- 科研写作：对齐证据链/引用（IMRAD/claim→evidence）
- 传播写作：对齐口吻/读者（叙事与风格）
- 主题排版：对齐视觉一致性（样式变量）

融合分工（不删，分层）：
- Primary（四选一）：PRD 用 `prd-taskmaster`；工程文档用 `doc-coauthoring`；科研写作用 `scientific-cs-writing`；传播写作用 `digital-brain`
- Styling（最后叠加）：`theme-factory`

建议标准交接产物：
- `docs/<topic>/outline.md`、`docs/<topic>/draft.md`
- `docs/<topic>/references.bib`、`docs/<topic>/claims_to_evidence.md`（科研写作时）
- `docs/<topic>/theme.md`、`docs/<topic>/review_checklist.md`

### 语义级“路由字段”（维护者建议固化）

为了让文档类 skill 可组合而不抢方向，你需要把“文档请求”缩到几个可判别的字段（字段本身比 skill 名字更重要）：

- `doc_type`：PRD / 设计说明 / ADR / RFC / IMRAD / 综述 / 博客
- `audience`：PM / 工程师 / 评审 / 同行审稿 / 公众
- `decision_or_explain`：做决策（要结论）/ 做解释（要教学）
- `evidence_required`：是否需要“证据链/引用/可追溯来源”
- `styling_required`：是否需要统一主题/模板/排版

建议你把这五个字段写进团队的“请求模板”，并把它们映射到“每步一个 Primary”的执行规范。

### 组合策略：把“写文档”拆成 4 阶段（每阶段一个 Primary）

1) **结构阶段**（只产出 `outline.md`）
   - PRD：Primary=`prd-taskmaster`
   - 设计说明/ADR/RFC：Primary=`doc-coauthoring`
   - IMRAD/综述：Primary=`scientific-cs-writing`
   - 博客：Primary=`digital-brain`
2) **内容阶段**（产出 `draft.md`，并补充附属表）
   - 科研写作附属：`references.bib`、`claims_to_evidence.md`
3) **门禁阶段**（产出 `review_checklist.md`，并回改 `draft.md`）
   - 这里的关键不是换 skill，而是换视角：从“生成”切到“审稿/一致性/缺口”
4) **风格阶段**（最后再统一排版/主题）
   - Styling=`theme-factory`（原则：风格永远不当结构 Primary）

### 典型反模式（导致“触发一堆 skills”但结果更差）

- 把“PRD + 设计说明 + 论文综述 + slides”当成一个任务：这不是融合，是语义混乱
- 先做主题再写内容：主题在内容不稳定时只会反复重做
- 没有“证据链”却要求“像论文一样严谨”：应先声明 `evidence_required=true` 并产出对应表/引用

---

## 1.3 UI/前端簇：把“做 UI”拆成检索→决策→落地→验证

典型 skills：`ui-ux-pro-max`、`designer`、`web-artifacts-builder`、`theme-factory`、`webapp-testing`

语义拆解：
- 设计参数检索（颜色/字体/布局范式）≠ 审美/可用性决策 ≠ 工程产物 ≠ 自动化验证

融合分工：
- Research：`ui-ux-pro-max`（产出 design tokens / 方案枚举）
- Primary（决策收敛）：`designer`
- Primary（工程产物）：`web-artifacts-builder`（当你确实要复杂 artifact）
- Styling：`theme-factory`
- Verification：`webapp-testing`

建议标准交接产物：
- `ui/<topic>/design_tokens.md`、`ui/<topic>/component_spec.md`
- `ui/<topic>/test_report.md` + `ui/<topic>/screenshots/`

### 语义开关：UI 请求里最关键的 4 个“开关词”

为了让 UI 类 skill 的组合稳定，维护者应推动用户把请求显式落在下面四个开关之一（否则就是“既要又要”）：

- `inspiration`：要风格候选/组件范式/配色方案（Research）
- `decision`：要“取舍理由 + 交互细节”（Primary=designer）
- `build`：要“能跑起来的代码/组件/路由/状态”（Primary=web-artifacts-builder）
- `verify`：要“截图/日志/回归/Playwright”（Verification=webapp-testing）

### 融合工作流：两段式（先收敛设计，再落地验证）

阶段 A（设计收敛）：
- `ui-ux-pro-max` 产出 `design_tokens.md`（候选空间/参数化）
- `designer` 产出 `component_spec.md`（收敛到可实现的决策）

阶段 B（工程落地 + 验证）：
- `web-artifacts-builder` 产出可运行产物（项目/组件）
- `webapp-testing` 产出 `test_report.md` + `screenshots/`

### 典型反模式

- 让 `webapp-testing` 参与“应该用什么风格”的讨论：验证工具会把注意力拉到实现细节
- 不区分 demo vs production：demo 追求“可展示”，production 追求“可维护/可观测/可演进”

---

## 1.4 评测簇：Rubric 与 Pipeline 的互补

涉及 skills：`advanced-evaluation`、`evaluation`

融合分工：
- `advanced-evaluation`：rubric/偏差控制/示例边界（怎么评）
- `evaluation`：评测工程化与质量门禁（怎么跑）

建议标准交接产物：
- `eval/<topic>/rubric.md`、`eval/<topic>/evalset.jsonl`、`eval/<topic>/pipeline.md`

### 语义开关：你到底是在“定义评分语义”还是“搭建评测系统”

评测类最常见的语义混淆是把“怎么评”与“怎么跑”混为一谈。融合式写法要求强制拆开：

- **语义层（rubric）**：维度/边界/示例/偏差控制（Primary=advanced-evaluation）
- **工程层（pipeline）**：数据格式/运行方式/质量门禁/回归策略（Primary=evaluation）

建议维护者把 `rubric.md` 当作强制产物：没有 rubric 的评测几乎一定会退化为“主观点评”。

---

## 1.5 Agent/Context 工程簇：总纲做导航，专项做落地

典型 skills：`context-engineering-collection`、`context-fundamentals`、`context-optimization`、`context-compression`、`context-degradation`、`filesystem-context`、`memory-systems`、`tool-design`、`reasoning-trace-optimizer`

融合建议：
- `context-engineering-collection` 只当“地图/目录”，不当 Primary
- `context-fundamentals` 做入门建模
- `context-optimization` / `context-compression` 解决预算与成本
- `context-degradation` 做症状诊断
- `filesystem-context` / `memory-systems` 把记忆落成文件/结构
- `tool-design` 把工具接口变成可用的协议
- `reasoning-trace-optimizer` 用 trace 做系统性调优

### 维护者路由：用“症状”代替“我想优化 agent”

这个簇的冲突本质是：用户一句话里没说清“系统失败模式”。建议维护者强制用户提供其中一个：

- **成本型症状**：上下文太长、费用太高、延迟太大
- **对齐型症状**：跑偏、前后矛盾、丢中间、被噪声带偏
- **记忆型症状**：需要跨会话记住、需要可追溯、需要审计
- **工具型症状**：工具难用、接口不一致、结果不可验证
- **trace 型症状**：已经有日志/trace，想基于证据做系统性优化

当症状明确后，才选专项 skill；`context-engineering-collection` 只负责“指路”，不当 Primary。

---

# 第 2 章（使用者视角）：写法模板——让技能“协同”而不是“抢方向”

请在请求里补齐三个字段：
1) 产物：要生成哪些文件/目录（最好给路径）
2) 阶段：现在做第几步（结构/内容/风格/验证）
3) 约束：受众/风格/是否可运行/是否要回归或偏差控制

如果你愿意显式点名 skill：每一步只点名一个 Primary，其余写成“后续叠加”。

## 2.1 文档/写作：四类主导写法（融合版）
- PRD：Primary 用 `prd-taskmaster`；主题最后再用 `theme-factory`
- 工程设计说明/RFC/ADR：Primary 用 `doc-coauthoring`；要求边界条件/权衡/读者测试
- 科研写作/综述：Primary 用 `scientific-cs-writing`；要求 `references.bib` 与 claim→evidence 表
- 博客/个人表达：Primary 用 `digital-brain`；强调受众与口吻，避免混入 PRD/论文关键词

### 模板：文档类请求的“最小充分信息”

把请求写成这 6 行，系统就能稳定组合多个 skills：
1) 产物路径：`docs/<topic>/draft.md`（或你指定）
2) 文档类型：PRD / 设计说明 / IMRAD / 博客（选一）
3) 当前阶段：结构 / 内容 / 门禁 / 风格（选一）
4) 受众：谁会读
5) 证据要求：是否要引用/证据链（是/否）
6) 风格要求：是否要统一主题（是/否）

示例（科研综述，结构阶段）：
- 产物路径：`docs/rag-survey/outline.md`
- 文档类型：综述
- 当前阶段：结构
- 受众：研究生
- 证据要求：是（需要 `references.bib` + claim→evidence）
- 风格要求：否（最后再做主题）

## 2.2 UI/前端：四步写法（强推荐）
1) “先产出设计参数（design tokens）”→ `ui-ux-pro-max`
2) “再做可用性与审美取舍（component spec）”→ `designer`
3) “再落成可运行 artifact”→ `web-artifacts-builder`
4) “最后做截图/日志/回归验证”→ `webapp-testing`

### 模板：UI 请求的“两段式”

阶段 A（设计收敛）：
- 产物路径：`ui/<topic>/design_tokens.md` + `ui/<topic>/component_spec.md`
- 需求：页面类型（landing/dashboard/form）、风格关键词（bento/minimal/dark）、关键用户路径

阶段 B（落地 + 验证）：
- 产物路径：可运行项目目录 + `ui/<topic>/test_report.md`
- 约束：技术栈、是否需要路由/状态、需要哪些截图/日志

## 2.3 评测：两步写法
1) “我要 rubric + 偏差控制策略”→ `advanced-evaluation`
2) “我要 eval pipeline + 回归门禁”→ `evaluation`

### 模板：评测请求（先 rubric 再 pipeline）

阶段 A（怎么评）：
- 产物路径：`eval/<topic>/rubric.md`
- 维度：正确性/一致性/安全性/可读性（可选）
- 偏差控制：pairwise/位置偏差/盲测（按需）

阶段 B（怎么跑）：
- 产物路径：`eval/<topic>/evalset.jsonl` + `eval/<topic>/pipeline.md`
- 约束：字段协议、运行命令、通过阈值与回归策略

## 2.4 Agent/Context：先说症状，再选专项
- “上下文太长/成本太高”→ `context-optimization` / `context-compression`
- “总是跑偏/丢中间/自相矛盾”→ `context-degradation`
- “要长期记忆/可追溯”→ `filesystem-context` / `memory-systems`
- “工具接口不稳定/难用”→ `tool-design`

### 模板：Agent/Context 请求（按症状路由）

- 症状：用 1-2 句话描述失败（最好带一个例子）
- 当前阶段：诊断 / 方案 / 落地（选一）
- 产物路径：`agent/<topic>/diagnosis.md`（或 `memory_schema.md` / `tool_contract.md`）
- 约束：上下文预算、工具集合、不可用能力（例如 Codex 无 subagent）
