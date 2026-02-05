Purpose: backend/service 架构差分（仅补充 backend 特有关注点）。
When to read: 阶段 2；repo 类型推断为 backend/service 时，在 generic 之后读作补丁。
Inputs: 路由/handlers、中间件、鉴权、持久化、后台任务、消息系统等线索。
Outputs: 在 Architecture Story 中追加/补全 backend 特有小节与检查点。
Do NOT: 不要重复 generic 的章节骨架；不要把每一点写成长文。

# Backend/Service 差分补丁

把下面这些点按“是否存在”追加到 Architecture Story（每点 1–3 行即可）：

- API 边界：REST/gRPC/Webhook；路由表在哪里
- AuthN/AuthZ：鉴权中间件、权限模型、token/session
- Persistence：ORM/SQL 层、迁移、事务边界
- Background Jobs：cron/queue/worker 的入口与重试语义
- Caching：缓存层与一致性策略（若存在）
- Consistency：幂等键/重试/去重（若存在）

