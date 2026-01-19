# Feasibility

Doc-ID: FEAS-2026-01-19-001
Doc-Type: feasibility
Owner: Moyu
Date: 2026-01-19
Version: v1.0
Status: draft
Source: docs/prd.md (PRD-2026-01-19-001)

## Summary
- 目标：在移除 `skillpack/` 后，仍能让仓库可用，并用 docs 模板明确流程与依赖。
- 评估了 3 个方案：纯文档模板、文档+轻量校验脚本、继续内置大包（不推荐）。
- 推荐：先落地“纯文档模板 + README 依赖清单”，后续再加自动校验。
- 解释 3 个关键 feature：低风险迭代、可回滚、可扩展到自动化。

## Assumptions
- 你当前优先级是“快速可用并能 push”，而不是立刻做重度工程化。

## Open Questions
- 是否需要在仓库里增加脚本来自动生成 Doc-ID/模板（后续可选）？

## Inputs and Assumptions
- 输入：PRD-2026-01-19-001
- 约束：不内置 `skillpack/`（减小仓库体积/减少重复拷贝），外部 skills 由使用者安装。

## Options
Option A: 仅提供 5 份 docs 模板（最小改动）
- Pros：最快、最少依赖、review 简单
- Cons：靠人工保证格式正确；Doc-ID/字段可能填错

Option B: docs 模板 + 轻量校验脚本（例如 pre-commit/CI 检查 Doc Contract 字段）
- Pros：格式更稳定，降低“文档不合规”概率
- Cons：多一点维护成本，需要 Python/Node 环境

Option C: 继续内置 skillpack（把外部 skills 直接拷贝进仓库）
- Pros：开箱即用
- Cons：仓库体积大、同步困难、版本漂移与重复维护风险高（与当前目标冲突）

## Comparison
- 速度：A > B >> C
- 风险：A（中） / B（低） / C（高）
- 长期维护：B 最优；A 可作为过渡；C 不建议

## Risk Matrix
- 文档不合规导致无法复用（Likelihood 3, Impact 3）：A 更明显；B 可缓解
- 外部依赖技能缺失导致执行失败（Likelihood 3, Impact 4）：需 README 清单明确（A/B 都要做）

## Cost and Timeline
- Option A：0.5 天（写文档+提交）
- Option B：1-2 天（加脚本+校验+文档）
- Option C：不确定且持续成本高

## Recommendation
- 先做 Option A：补齐 5 份 docs 模板 + README 外部依赖 skills 清单。
- 后续如果团队开始规模化使用，再升级到 Option B。

## MVP Path
1. 创建 `docs/` 与 5 文件（模板/示例）。
2. README 写清楚：必装 skills + 可选 skills + 用途。
3. 推送后让新成员试用一次，基于反馈再加校验脚本。

## Open Questions
- 是否要在 README 明确“如何追加多条记录（---）”的规范？
