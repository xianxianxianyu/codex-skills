Purpose: 生成二开指南（Extension Guide）的套路与章节骨架，帮助回答“如何扩展/插件化/二次开发”。
When to read: 第二次提问选择“生成二开指南”后；深入模式默认读，标准模式按需读。
Inputs: 模块卡；依赖边界；配置与入口点；事件/Hook/接口定义线索；构建/发布方式。
Outputs: `EXTENSION_GUIDE.md` 的章节骨架（Extension Points、How to Add Feature、Constraints、Rollback）。
Do NOT: 不要重复 Repo Map 的运行方式与目录注释；只引用。

# Extension Guide（套路）

## 1. Extension Surface（扩展面）

- “可插入”的位置：路由/handler、service、pipeline、UI 插槽、CLI 子命令
- 机制：interface/abstract class、hook、event、plugin registry、DI container（存在啥写啥）

## 2. How to Add a New <Feature>（最短路径）

- 选择一个“最小扩展案例”（1 个 endpoint / 1 个 job / 1 个 UI 页面 / 1 个 SDK 方法）
- 以步骤列出：新增文件 → 注册/路由 → 配置 → 测试 → 运行验证

## 3. Constraints（约束）

- 边界：哪些层允许访问外部依赖；哪些模块不该被直接依赖
- 配置：env/config 的约束与默认值来源（引用 Quickstart/Ops）

## 4. Rollback / Safety（回滚与安全）

- Feature flag/开关（若存在）
- 回滚策略：兼容旧行为、配置回退、迁移回滚（若适用）

