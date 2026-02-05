---
name: repo-reader
description: 为一个代码仓库生成高信息密度的阅读/讲解文档（Repo Map、Architecture Story、Key Flows、Q&A），并可选生成二开指南（extension guide）与模块深挖 mini-doc。适用于“讲解这个 repo / onboarding / 读代码 / 架构梳理 / 模块划分 / 关键流程 / 如何跑起来 / 如何扩展/插件化 / 深挖某模块”等需求；支持 backend、frontend、library/SDK、monorepo、fullstack 等仓库形态，并用轻量/标准/深入三档控制输出规模。
---

# Repo Reader

## 目标

把“我该怎么看懂这个 repo”变成稳定、可复用、低重复率的输出流程：

- 阶段 0：意图对齐（兴趣点候选 + 默认路线说明）
- 阶段 1：Repo Map（Pass1 外科医生）
- 阶段 2：Architecture Story（Pass2 产品经理）
- 阶段 3：Risks + Q&A（Pass3 架构师）

并在阶段 1 后强制做第二次提问，闭环二开与模块深挖。

## 输出（默认）

- 默认输出目录：`docs/`（用户未指定则不追问）
- 主文档：`docs/REPO_OVERVIEW.md`
- 可选二开指南：`docs/EXTENSION_GUIDE.md`
- 可选模块深挖：`docs/MODULE_<module>_MINIDOC.md`

输出规范：

- 对话输出开头声明：已激活技能：repo-reader（如同时使用其它 skills，按逗号补充）
- 文档结构遵循 `../_shared/doc-contract.md`（建议使用 `Doc-Type: qa` 承载“Repo Overview/Guide/Mini-Doc”）

写作约束（降低重复率）：

- 先结构后细节：先 Repo Map，再讲架构，再 Q&A。
- 一处定义，多处引用：同一事实只出现一次，其它地方用章节锚点引用（例如：“见 Repo Map > Entry Points”）。
- Mode 用“输出限额”控复杂度（见下）。

## Mode（轻量/标准/深入）

Mode 不新增 frontmatter 字段：只通过用户话术与 repo 规模启发决定。

- 轻量：模块卡 Top 3；Key Flows：1 条 + 1 条“依赖/调用链替代”；Q&A ≤ 5 条
- 标准（默认）：模块卡 Top 6；Key Flows：2 条；Q&A ≤ 10 条
- 深入：模块卡 Top 10 + 附录列出剩余模块；Key Flows：3–5 条；Q&A ≤ 15 条；可选二开/mini-doc

触发建议：

- 用户说“快速/概览/一句话/quick answer” → 轻量
- 用户说“深入/审计/二开方案/重构/性能安全” → 深入
- repo 很大（顶层条目很多或明显 monorepo）也可从深入降级到标准/轻量，并在文档开头声明“为控制输出规模采用 X Mode”

## 核心机制：流程路由（不是运行时代码路由）

默认方案不依赖脚本：完全靠本 `SKILL.md` 的流程指令，要求 agent 在需要时去读 `references/` 中的模板与清单。

`references/index.md` 只维护：

- 意图标签 → refs 列表
- 同义词表（中英映射）
- 一行优先级规则（用户显式 > plan 标签 > repo 推断）

## 路由算法（可执行、可复用）

1) 解析用户 prompt，抽取意图标签（可多选）与用户显式模块名（如 `auth`, `payments`）
2) 先定 Mode（轻量/标准/深入）
3) 推断 repo 类型（backend/service、frontend、library/sdk、monorepo、fullstack；在阶段 1 结束后重新校验一次）
4) 读取 `references/index.md`，根据“用户显式 + 标签 + repo 类型”组装本次要读的 refs 列表
5) 按四阶段执行；每个阶段只产生“该阶段该有的东西”，避免跨阶段抢活（见各 references 文件顶部的 Purpose/Do NOT）

## repo 类型推断（证据与规则）

先扫描/打开这些证据文件（存在即读）：

- Node/前端/TS：`package.json`、`pnpm-workspace.yaml`/`yarn.lock`、`tsconfig.json`、`vite.config.*`/`next.config.*`
- Python：`pyproject.toml`、`setup.cfg`、`requirements.txt`
- Go：`go.mod`
- Rust：`Cargo.toml`
- Java：`pom.xml`、`build.gradle`/`build.gradle.kts`
- .NET：`*.sln`、`*.csproj`
- 通用部署：`Dockerfile`、`docker-compose*.yml`、`k8s/*.yaml`、CI（`.github/workflows/*`, `.gitlab-ci.yml`）

推断规则（简化版）：

- 同时存在 `packages/*` + workspace 文件（pnpm/yarn）→ monorepo
- 存在服务入口（如 `main.go` 启 server、`app.py`/`main.py` 启动 ASGI/WSGI、Node 有 express/fastify/nest 依赖）+ Docker/compose/k8s 任一 → service/backend
- 存在 next/vite/react 等框架配置 + `src/pages`/`routes` → frontend
- 以 exports/main/module 形式对外发布，且无服务启动迹象 → library/sdk

冲突处理：

- 命中多个语言构建文件且存在 `packages/apps/services`：直接判 monorepo；阶段 2 用 monorepo 模板
- “服务 + 前端”同仓但无 monorepo 结构：判 fullstack；阶段 2 同时应用 backend + frontend 差分
- 重新校验时机写死：阶段 1 Repo Map 完成后，基于入口点/构建证据重新判断一次；若切换模板，必须在文档里写“模板切换原因”

## 两次提问（必须闭环）

第一次提问（阶段 0 末尾）：

- 输出固定格式的“兴趣点候选清单”（编号 + 短标签）
- 明确：不选也行，我会按默认路径继续
- 默认兴趣点：入口/依赖/关键流程/模块卡/风险/快速上手

第二次提问（阶段 1 结束）：

- 开关 1：要不要生成二开指南（Extension Guide）
- 开关 2：要不要针对某模块深挖（Module Mini-Doc）
  - 用户给模块名：用该模块
  - 用户不给：自动选一个模块，并必须输出一行解释“默认选择 <module> 的原因：Reachability=… / RefCount=… / NameHeuristic=…”

fallback（写死）：

- 用户不回复：继续阶段 2/3（不生成二开/mini-doc）
- 只选二开：生成 `docs/EXTENSION_GUIDE.md`
- 只选深挖：生成 `docs/MODULE_<module>_MINIDOC.md`
- 两个都选：两个都生成

## 默认模块选择算法（用于 mini-doc）

按以下优先级（从上到下取第一个可用的候选）：

1) 用户显式指定模块
2) 入口点可达的“核心业务模块”（从入口文件可达、并位于核心目录如 `src/`/`server/`/`app/`/`services/`）
3) 引用/依赖频次更高的模块（允许用 `rg`/IDE 全局搜索做粗计数；可忽略 test/fixtures/vendor）
4) 名称启发（`auth`, `payment`, `order`, `user`, `core`, `api` 等）
5) monorepo：优先 `apps/*` 的入口应用，其次 `packages/*` 的 shared lib

输出必须包含“可解释输出”的一行总结（不需要复杂数学；可用粗评分即可）。

## 参考文件（必须从这里直接可达）

- `references/index.md`
- `references/pass1_repo_map.md`
- `references/pass2_behavior_story.md`
- `references/pass3_risks_debt.md`
- `references/template_arch_generic.md`
- `references/template_arch_backend.md`
- `references/template_arch_frontend.md`
- `references/template_arch_library.md`
- `references/template_arch_monorepo.md`
- `references/template_quickstart_ops.md`
- `references/template_module_card.md`
- `references/template_key_flows.md`
- `references/template_qa_format.md`
- `references/playbook_extension_guide.md`
- `references/playbook_module_minidoc.md`
- `references/checklist.md`
- `references/output-example.md`

## 工程化收口（执行结束前自检）

按 `references/checklist.md` 自检，并对照 `references/output-example.md` 纠偏输出的“长度、密度、引用方式”。
