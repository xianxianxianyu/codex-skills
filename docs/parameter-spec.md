# Parameter Spec

Doc-ID: PARAM-2026-01-19-001
Doc-Type: params
Owner: Moyu
Date: 2026-01-19
Version: v1.0
Status: draft
Source: subagent-skills/_shared/doc-contract.md + 本仓库使用约定

## Summary
- 本文件用于“文档化产出”的参数规范：如何生成/填写 Doc-ID、状态、输出路径与追加策略。
- 给出参数表（类型/默认值/范围/依赖）与约束规则，减少不同人写法不一致。
- 提供 safe/balanced/high 三档预设，便于按场景选择。
- 解释 4 个 feature：默认路径一致性、可追加多条记录、可审计可追踪、可渐进增强到自动化。

## Assumptions
- 你用 Git 管理这些 docs，并希望每次产出都可 review、可追溯。
- Doc-ID 由人工填写或由脚本生成（二者皆可）。

## Open Questions
- Doc-ID 是否需要强制连续递增（001/002/003）还是允许任意唯一值？

## Context
适用模块：Codex Subagent Skills 的文档输出（qa/prd/feasibility/implementation/params）与默认保存路径规范。

## Parameter Table
| name | type | default | range | unit | dependencies | notes |
|---|---|---|---|---|---|---|
| owner | string | "<your-name-or-team>" | non-empty | n/a | none | 文档责任人/维护者 |
| date | string | "YYYY-MM-DD" | ISO date | n/a | none | 建议用当天日期 |
| status | enum | draft | draft/review/final | n/a | none | 评审阶段 |
| version | string | v1.0 | v1.x | n/a | none | 文档版本 |
| doc_id_seq | int | 1 | 1-999 | n/a | date+doc_type | 当天同类型序号 |
| append_mode | enum | single | single/append | n/a | none | single=文件单条；append=同文件多条用 `---` |
| output_dir | path | docs/ | relative path | n/a | repo root | 默认输出目录 |
| qa_path | path | docs/qa-notes.md | path | n/a | output_dir | 默认 QA 文件 |
| prd_path | path | docs/prd.md | path | n/a | output_dir | 默认 PRD 文件 |
| feasibility_path | path | docs/feasibility.md | path | n/a | output_dir | 默认可行性文件 |
| implementation_path | path | docs/implementation-report.md | path | n/a | output_dir | 默认实现报告 |
| params_path | path | docs/parameter-spec.md | path | n/a | output_dir | 默认参数规范 |

## Constraint Rules
- Doc-ID 必须唯一，且符合格式：
  - qa: QA-YYYY-MM-DD-###
  - prd: PRD-YYYY-MM-DD-###
  - feasibility: FEAS-YYYY-MM-DD-###
  - implementation: IMPL-YYYY-MM-DD-###
  - params: PARAM-YYYY-MM-DD-###
- 每份文档必须包含：Required Header + Summary/Assumptions/Open Questions（Next Steps 可选）。
- append_mode=append 时：每条记录之间必须用一行 `---` 分隔。

## Preset Profiles
- safe（最稳妥/最易 review）：
  - append_mode=single（每个文件只维护一条最新记录；历史靠 Git）
  - status=draft → review → final（按 PR 流程推进）
- balanced（推荐）：
  - append_mode=append（同文件可追加多条；用 `---` 分隔）
  - 重要变更写 implementation + params，轻量问答写 qa
- high（高频迭代/重自动化预备）：
  - append_mode=append
  - 计划引入脚本自动生成 Doc-ID/校验字段（后续工作）

## Validation Notes
- 人工校验：`rg "Doc-ID:" docs`、`rg "Doc-Type:" docs` 检查字段齐全。
- Review 校验：确保 Summary 3-7 条、Open Questions 不为空时能驱动下一步。
