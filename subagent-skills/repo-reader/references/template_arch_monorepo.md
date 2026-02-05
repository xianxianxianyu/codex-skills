Purpose: monorepo 架构差分（仅补充 workspace、包图与构建/test 编排关注点）。
When to read: 阶段 2；repo 类型推断为 monorepo 时，在 generic 之后读作补丁。
Inputs: workspace 文件、packages/apps/services 结构、构建编排脚本、共享依赖策略。
Outputs: 在 Architecture Story 中追加/补全 monorepo 特有小节与检查点。
Do NOT: 不要重复 generic 的章节骨架；不要把每一点写成长文。

# Monorepo 差分补丁

把下面这些点按“是否存在”追加到 Architecture Story（每点 1–3 行即可）：

- Workspace：pnpm/yarn/turbo/nx 等工具与入口命令
- Package Graph：apps vs packages/shared 的依赖方向（只画 Top 层）
- Build/Test：一键构建与增量构建策略；CI 如何跑
- Shared：共享 config、lint、types、UI/SDK 的位置

