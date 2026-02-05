## Skills（仓库内置）

本仓库将可用技能（skills）放在 `subagent-skills/` 下；每个 skill 都有一个 `SKILL.md` 作为入口文档。

### Available skills

| skill | 用途 | 默认产物 | 入口文件 |
|---|---|---|---|
| `qa-basic` | 快速问答与记录（轻量、不改代码） | `docs/qa-notes.md` | `subagent-skills/qa-basic/SKILL.md` |
| `repo-reader` | 生成 repo 阅读/讲解文档（Repo Map/架构/关键流程/Q&A），可选二开指南与模块 mini-doc | `docs/REPO_OVERVIEW.md` | `subagent-skills/repo-reader/SKILL.md` |
| `requirements-elicitation` | 需求分析 / PRD（REQ-xxx + 验收标准） | `docs/prd.md` | `subagent-skills/requirements-elicitation/SKILL.md` |
| `feasibility-analysis` | 可行性分析（方案对比/风险/成本/周期/推荐） | `docs/feasibility.md` | `subagent-skills/feasibility-analysis/SKILL.md` |
| `code-agent-core` | 代码实现与交付报告（改动/测试/风险/回滚） | `docs/implementation-report.md` | `subagent-skills/code-agent-core/SKILL.md` |
| `parameter-sanity` | 参数合理性校准（默认值/范围/依赖/约束/预设档位） | `docs/parameter-spec.md` | `subagent-skills/parameter-sanity/SKILL.md` |

### Shared contract

- Doc Contract：`subagent-skills/_shared/doc-contract.md`

### Routing（触发与分流）

- 仅需快速解释/定义/对比：用 `qa-basic`
- 需要讲解/阅读一个 repo、快速上手、架构梳理、关键流程、二开/扩展、模块深挖：用 `repo-reader`
- 需要写 PRD/需求/范围/验收标准：用 `requirements-elicitation`
- 需要可行性、方案对比、成本/周期、风险矩阵：用 `feasibility-analysis`
- 需要改代码/实现功能/修 bug：用 `code-agent-core`
- 需要参数默认值/配置调优/组合合理性校验：用 `parameter-sanity`

### 标准 pipeline（推荐）

- Repo Reader（可选）→ QA → PRD → Feasibility → Implementation → Params
- 说明：当你不熟悉一个 repo 时，先用 Repo Reader 生成可追溯的 Repo Map/架构/关键流程；再固化问题与上下文（QA），把需求变成可验收条目（PRD），做方案与风险决策（Feasibility），最后落到代码与交付记录（Implementation）以及参数规范（Params）。

### 文档语言规则（重要）

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。
- 每次对话输出开头需声明：已激活技能：<skill-name>（如同时使用其它 skills，按逗号补充）。
- 每份输出文档的 Required Header 需填写：Activated-Skills: <skill-name[, ...]>。

