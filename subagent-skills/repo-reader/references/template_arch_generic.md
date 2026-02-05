Purpose: 架构讲述主模板（generic），提供章节骨架、叙事顺序、必须覆盖点。
When to read: 阶段 2；所有 Mode 只要做“架构梳理/模块划分”就应读；类型差分模板在此之后读。
Inputs: Pass1 模块候选、依赖边界、入口点、构建/部署证据。
Outputs: Architecture Story 章节骨架（Layers、Modules、Runtime/Config、Integrations、Key Flows 引用点）。
Do NOT: 不要写某一种仓库类型的特有细节（交给 template_arch_* 差分）；不要把 Key Flows 细节写在这里（只保留引用点）。

# Architecture Story（Generic）

## 1. 系统边界（1 段即可）

- 这个 repo 的“系统边界”是什么：它负责什么、不负责什么

## 2. 分层/分域视角（按 repo 类型取一个合适的视角）

选择一种讲法（不要都讲）：

- Layered：`API/Handlers → Services → Domain → Persistence/Adapters`
- Modular：`packages/apps/libs` 或按业务域分组
- Pipeline：按数据流/调用链分段

## 3. Modules（模块卡）

- 从候选模块里按 Mode 输出 Top N 模块卡
- 模块卡格式见 `template_module_card.md`

## 4. Integrations（外部依赖与适配器）

- 数据库/缓存/消息队列/第三方 API/文件存储
- “依赖边界”一句话：哪些模块能直接触达外部依赖

## 5. Runtime & Config

- 运行时入口（引用 Repo Map）
- 配置来源：env/config file/flags/remote config
- 部署形态：本地/容器/集群（引用 Quickstart/Ops）

## 6. Key Flows（只放引用与列表）

- 列出将要在 Key Flows 章节展开的流程名称（细节放 `template_key_flows.md`）

