Purpose: library/SDK 架构差分（仅补充“对外 API + 版本与兼容性”关注点）。
When to read: 阶段 2；repo 类型推断为 library/sdk 时，在 generic 之后读作补丁。
Inputs: public exports、入口文件、API 文档、版本策略、示例代码、测试。
Outputs: 在 Architecture Story 中追加/补全 library 特有小节与检查点。
Do NOT: 不要重复 generic 的章节骨架；不要把每一点写成长文。

# Library/SDK 差分补丁

把下面这些点按“是否存在”追加到 Architecture Story（每点 1–3 行即可）：

- Public API：对外导出点、核心对象/函数、最小用法
- Stability：稳定性承诺、breaking change 策略、deprecated 路径
- Packaging：发布方式（npm/pypi/crates/maven），以及版本号来源
- Examples：示例/README 中的“最短路径用法”

