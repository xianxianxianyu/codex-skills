Purpose: quickstart/ops 输出模板（如何跑起来/部署/CI 线索），为 Repo Map 与 Ops 相关问题服务。
When to read: 阶段 1（如果用户关心“跑起来/部署”或轻量模式也需要 quickstart）；阶段 2 只引用不复述。
Inputs: README、package scripts/Makefile、Dockerfile/compose/k8s、CI 文件、.env.example。
Outputs: Quickstart/Ops 小节（Local Run、Config、Docker、CI/Deploy）。
Do NOT: 不要写架构分层；不要写 Key Flows。

# Quickstart / Ops（模板）

## Local Run（最短路径）

- Prereqs：语言版本/工具链（1 行）
- Commands：3–6 条命令（尽量来自 README/package scripts）
- Config：列出关键 env/config 名称（不需要解释每个含义）

## Docker / Compose（若存在）

- 构建与启动命令（最短路径）
- 依赖服务（db/cache/queue）列表

## CI / Deploy（若存在）

- CI 入口：workflow 文件路径/任务名
- Deploy 形态：container/k8s/VM（1–2 行）

