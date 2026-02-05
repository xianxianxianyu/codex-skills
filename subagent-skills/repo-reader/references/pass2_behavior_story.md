Purpose: Pass2（Behavior Story）检查清单 + 产物骨架，聚焦能力/用例/失败路径/可观测性。
When to read: 阶段 2；深入模式必读，标准模式按需读。
Inputs: Pass1 的入口点/模块候选；API 路由/命令/作业定义；日志/指标/trace；错误处理线索。
Outputs: Behavior Story 骨架（Capabilities、Use Cases、Failure Paths、Observability、Key Flows 候选）。
Do NOT: 不要重复 Key Flows 的详细流程叙事（交给 template_key_flows.md）；不要替代架构模板的分层叙事（交给 template_arch_generic.md）。

# Pass2：Behavior Story（检查清单 + 骨架）

## 能力与用例（Capabilities / Use Cases）

- 这个 repo 对外提供什么“能力”（API、CLI、库函数、UI）
- 最常见的 2–5 个用例（按真实入口点/路由/命令推断）

## 失败路径（Failure Paths）

- 典型失败点：配置缺失、鉴权失败、依赖不可用、外部 API 超时、数据不一致
- 每类失败的“用户可见结果”与“系统处理方式”（重试/降级/告警）

## 可观测性（Observability）

- 日志：关键日志点在哪里（目录/中间件/拦截器）
- 指标/trace：是否有 metrics/tracing，入口在哪里
- 调试手段：本地 debug、mock、fixtures

## Key Flows 候选（只列候选，不讲细节）

- 从用例中挑 2–5 个“最关键/最能代表系统”的流程候选
- 细节交给 `template_key_flows.md` 输出

