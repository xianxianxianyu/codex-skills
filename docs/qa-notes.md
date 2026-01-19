# QA Notes

Doc-ID: QA-2026-01-19-001
Doc-Type: qa
Owner: Moyu
Date: 2026-01-19
Version: v1.0
Status: draft
Source: codex-skills 仓库维护/使用说明

## Summary
- 本文件是 `qa-basic` 的输出示例/模板，用于把一次问答沉淀成可追溯文档。
- 采用 Doc Contract v1：统一头部 + Summary/Assumptions/Open Questions。
- 主流程（pipeline）与其它 4 类文档互相衔接：PRD → Feasibility → Implementation → Params → QA。
- 解释了 4 个核心 feature：可追溯 Doc-ID、可追加多条记录、可检索结构、可作为后续实施输入。

## Assumptions
- 你希望把“临时对话”固化成可提交到 Git 的文档记录。
- 同一个文件可能追加多条 QA 记录（用 `---` 分隔）。

## Open Questions
- Owner 字段采用个人名还是团队名？
- 是否需要在 QA 里强制记录命令与输出（用于可复现）？

## Next Steps
- 若 QA 已明确需求，进入 `docs/prd.md` 产出 PRD；若仅需快速修复，进入 `docs/implementation-report.md`。

## Question
如何在维护/使用 codex-skills 时，把一次对话结果沉淀成“可复用”的文档？主要逻辑和 pipeline 是什么？

## Answer
主要逻辑：把“问题→结论→依据/上下文→后续动作”结构化记录，保证之后任何人（或新的模型实例）只看文档也能复现结论与决策原因。

主要 pipeline（建议顺序）：
1. QA（本文件）：快速澄清问题/结论/上下文，记录关键约束与未决问题。
2. PRD（docs/prd.md）：把需求变成可验收的条目（REQ-xxx + AC）。
3. Feasibility（docs/feasibility.md）：对实现路径做 A/B 方案、风险、成本、时间评估，给推荐。
4. Implementation（docs/implementation-report.md）：记录实际改动、测试、风险与回滚。
5. Params（docs/parameter-spec.md）：若涉及参数/默认值，沉淀参数表、约束规则、预设档位。

Feature 解释（示例 4 个）：
- Doc-ID 可追溯：每条记录都有唯一编号，便于引用、审计、回滚讨论。
- 结构统一可检索：固定章节让后续用 `rg`/搜索快速定位“结论/假设/未决问题”。
- 允许多条追加：同一文件持续沉淀知识，用 `---` 分隔，适合长期项目。
- 可作为下游输入：QA 的 Open Questions/Assumptions 直接喂给 PRD/Feasibility，减少信息丢失。

## Context
典型场景：同步 GitHub 仓库、处理 `git pull` 冲突、删除目录（如 skillpack）并补齐文档后推送。

## References
- subagent-skills/_shared/doc-contract.md
- subagent-skills/qa-basic/ (checklist + triage)
