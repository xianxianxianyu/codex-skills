Purpose: 最小路由表（意图标签/同义词/优先级），用于决定读哪些 references。
When to read: 阶段 0 产出标签后；阶段 1 复核 repo 类型后可再读一次。
Inputs: 用户 prompt；阶段 0/1 产出的意图标签、repo 类型、模块候选。
Outputs: “本次要读取的 references 列表”与简短理由（1 行即可）。
Do NOT: 不要在这里写阶段流程/输出结构/长篇模板（这些属于 SKILL.md 或具体模板文件）。

# 路由表（最小可用）

优先级：用户显式 > plan/标签 > repo 类型推断。

## 意图标签 → 建议读取的 refs

- `[快速上手]` → `template_quickstart_ops.md`, `template_qa_format.md`
- `[Repo Map]` → `pass1_repo_map.md`
- `[架构梳理]` → `template_arch_generic.md`, `template_module_card.md`
- `[关键流程]` → `template_key_flows.md`
- `[Q&A]` → `template_qa_format.md`, `pass3_risks_debt.md`
- `[二开]` → `playbook_extension_guide.md`
- `[模块深挖]` → `playbook_module_minidoc.md`
- `[风险/债务]` → `pass3_risks_debt.md`

## repo 类型 → 架构差分模板（在 generic 之后作为补丁）

- backend/service → `template_arch_backend.md`
- frontend → `template_arch_frontend.md`
- library/sdk → `template_arch_library.md`
- monorepo → `template_arch_monorepo.md`
- fullstack → `template_arch_backend.md` + `template_arch_frontend.md`
- 不确定 → 只用 `template_arch_generic.md`，并在输出里声明不确定

## 同义词（只做映射，不做解释）

- “二开/扩展/插件化/二次开发/extension/plugin” → `[二开]`
- “深挖/mini-doc/模块级/深入某模块/deep dive” → `[模块深挖]`
- “怎么跑/跑起来/部署/启动/quickstart/ops/run” → `[快速上手]`
- “架构/分层/模块/依赖边界/architecture/modules” → `[架构梳理]`
- “关键流程/主链路/调用链/数据流/key flow” → `[关键流程]`
- “风险/债务/耦合/安全/性能/风险点/risks” → `[风险/债务]`

