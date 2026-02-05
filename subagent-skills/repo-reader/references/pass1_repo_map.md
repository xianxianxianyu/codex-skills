Purpose: Pass1（Repo Map）检查清单 + 产物骨架，聚焦入口/目录/依赖边界/如何跑。
When to read: 阶段 1；标准/深入模式必读，轻量模式按需读。
Inputs: README/入口文件/构建配置/依赖文件/顶层目录枚举/运行方式线索。
Outputs: Repo Map 章节骨架（Entry Points、Run/Build、Dir Notes、Deps/Boundaries、Modules候选）。
Do NOT: 不要写架构分层长文；不要写 Key Flows 的流程叙事（交给 template_key_flows.md）。

# Pass1：Repo Map（检查清单 + 骨架）

## 需要看的证据（按存在性）

- README/Quickstart（如果没有，就从构建文件推断运行方式）
- 构建/依赖：语言对应的 lockfile / build file（见 SKILL.md 列表）
- 入口点：`main.*`、`app.*`、`index.*`、`cmd/*`、`src/main.*`、框架约定入口
- 配置：`.env.example`、`config/*`、`settings.*`、`values.yaml` 等
- 部署/CI：`Dockerfile`、`docker-compose*.yml`、`.github/workflows/*`

## Repo Map 产物骨架（建议顺序）

### Entry Points

- 列出 1–3 个入口点（文件路径/命令名）
- 每个入口点 1 行说明“它做什么/启动什么”

### How to Run / Build（可选，按意图与 Mode）

- 本地运行（最短路径）
- 关键环境变量/配置文件（列出名字即可）

### Directory Notes（高密度，不超过 12 行）

- 只注释“关键目录/关键文件”
- 不要贴完整 tree；避免噪音

### Dependencies & Boundaries

- 关键外部依赖（数据库/消息队列/第三方 API/云服务）
- 模块边界（哪些目录是 core，哪些是 adapters/integrations）

### Module Candidates（给后续阶段用）

- 输出一个“候选模块列表”（Top N 由 Mode 决定）
- 每个候选模块：目录/命名空间 + 1 行责任猜测（不确定就标注）

## 阶段 1 结束时必须做的两件事

1) 重新校验 repo 类型（必要时切换阶段 2 模板，并写“切换原因”）
2) 发出第二次提问：二开指南 + 模块深挖两个开关（含 fallback）

