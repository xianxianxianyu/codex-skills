# PRD

Doc-ID: PRD-2026-01-19-001
Doc-Type: prd
Owner: Moyu
Date: 2026-01-19
Version: v1.0
Status: draft
Source: codex-skills 仓库维护目标（移除 skillpack + 补齐文档）

## Summary
- 目标：让 codex-skills 在不内置 `skillpack/` 的情况下仍可用，并用 5 份 docs 统一产出格式。
- 核心 pipeline：QA → PRD → Feasibility → Implementation → Params → QA（闭环）。
- 输出：README 的 Skills 清单对应的 5 个 `docs/*.md` 示例/模板 + 外部依赖 skills 清单。
- 解释 4 个 feature：统一 Doc Contract、可验收 REQ、风险驱动决策、参数默认值治理。

## Assumptions
- 仓库面向的读者是“会用 Git 的工程师/研究者”，需要可复制的模板与流程。
- `skillpack/` 已从仓库移除（或将移除），外部 skills 通过独立安装/引用。

## Open Questions
- 外部依赖 skills 的最小集合是什么（必须 vs 可选）？
- 是否需要 CI/脚本校验 docs 的 Doc Contract 格式（后续可选）？

## Executive Summary
本 PRD 定义“文档化的子代理技能工作流”在仓库层面的交付要求：每次任务至少沉淀 QA/PRD/Feasibility/Implementation/Params 五类文档之一，并遵循统一 Doc Contract，形成可追溯、可检索、可复用的交付链路。

## Problem Statement
仅靠对话容易丢信息：需求边界、取舍原因、风险评估、参数默认值、回滚策略等无法稳定复现，导致“同样的问题重复沟通/重复踩坑”。

## Goals (SMART)
- 1 周内：补齐 `docs/` 目录与 5 个文档模板，使新成员可在 10 分钟内理解并开始使用工作流。
- 2 周内：将外部依赖 skills 清单写清楚（必选/可选、用途、安装方式），减少环境差异导致的失败率。

## Scope / Non-Goals
- Scope：
  - 提供 5 个 `docs/*.md`（示例/模板），严格遵循 Doc Contract v1。
  - README 中明确：哪些是仓库内置 subagent skills，哪些是外部依赖 skills。
- Non-Goals：
  - 不在本 PRD 中引入复杂自动化生成器/CI（可作为后续迭代）。

## Users and Personas
- 维护者：需要可控的仓库体积、清晰依赖边界、可 review 的交付物。
- 使用者：希望快速得到“能落地”的文档/计划/实现记录，不想每次从零组织结构。

## User Stories
- 作为维护者，我希望删除 `skillpack/` 后仓库仍清晰可用，且文档告诉我需要安装哪些外部 skills。
- 作为使用者，我希望每次任务都能按固定模板输出文档，方便提交/复盘/交接。

## Functional Requirements
- REQ-001: 提供 5 个默认路径文档（若不存在则创建）
  - Acceptance Criteria:
    - [ ] 存在 `docs/qa-notes.md`
    - [ ] 存在 `docs/prd.md`
    - [ ] 存在 `docs/feasibility.md`
    - [ ] 存在 `docs/implementation-report.md`
    - [ ] 存在 `docs/parameter-spec.md`
- REQ-002: 五个文档均包含 Doc Contract v1 的 Required Header + Required Sections
  - Acceptance Criteria:
    - [ ] 每份文档包含 Summary/Assumptions/Open Questions（并可选 Next Steps）
- REQ-003: 每份文档用中文说明“主要逻辑 + 主要 pipeline + 3-4 个 feature”
  - Acceptance Criteria:
    - [ ] 每份文档均包含 pipeline 描述与 feature 解释
- REQ-004: README 明确外部依赖 skills（必选/可选）与用途
  - Acceptance Criteria:
    - [ ] 至少列出 `doc-coauthoring`、`prd-taskmaster`、`ui-ux-pro-max`、`web-artifacts-builder` 的用途与获取方式（若你实际依赖更多可再加）

## Non-Functional Requirements
- 文档结构稳定：review 时易 diff，避免大段无结构文本。
- 可检索：关键字段（Doc-ID、REQ-xxx）可被文本搜索命中。

## Constraints and Assumptions
- 统一格式来自 `subagent-skills/_shared/doc-contract.md`，以仓库为准。

## Risks and Open Questions
- 依赖 skills 版本漂移：外部技能升级后描述可能不一致。
- 用户不按模板填写：导致“看起来有文档但不可复现”。

## Metrics and Validation
- 指标：新成员在 10 分钟内能找到 5 份文档模板并写出一条合格记录。
- 验证：PR Review 时检查 Doc Contract 字段是否齐全；用 `rg "Doc-ID:" docs` 检查一致性。

## Rollout and Milestones
- M1：新增 `docs/` 与 5 文件并推送。
- M2：README 更新外部依赖 skills 清单与安装说明。
- M3（可选）：增加脚本/CI 校验 Doc Contract。

Feature 解释（示例 4 个）：
- 统一 Doc Contract：降低沟通成本，保证交付物“看得懂、能复盘”。
- 可验收 REQ：把需求拆成 REQ-xxx + AC，减少“做了但不算完成”的争议。
- 风险驱动决策：Feasibility 强制 A/B 方案与风险矩阵，避免拍脑袋。
- 参数治理：Params 文档把默认值、范围、依赖与预设档位固化，减少线上事故。
