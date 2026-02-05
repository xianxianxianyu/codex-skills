Purpose: Pass3（Risks/Debt + Q&A）检查清单 + 骨架，聚焦约束/耦合/风险债务，并把兴趣点问题化。
When to read: 阶段 3；深入模式必读，标准模式按需读。
Inputs: Pass1/2 产物；依赖边界；配置/部署方式；历史遗留迹象（TODO/FIXME、deprecated）。
Outputs: Risks/Debt 骨架 + Q&A 问题列表（按优先级）。
Do NOT: 不要复述 Repo Map/Modules/Key Flows 的事实；在 Q&A 中尽量引用锚点，而不是重复解释。

# Pass3：Risks/Debt + Q&A（检查清单 + 骨架）

## 约束与耦合（Constraints / Coupling）

- 强耦合点：跨层调用、全局状态、隐式依赖（环境变量/单例）
- 运行约束：必须的外部依赖、初始化顺序

## 风险与债务（Risks / Debt）

- 可靠性：重试/幂等/超时/资源泄露
- 安全：鉴权边界、密钥管理、输入校验
- 性能：热点路径、缓存策略、N+1、并发瓶颈
- 维护性：模块边界不清、重复逻辑、测试缺口

## 兴趣点 → Q&A（只生成问题列表 + 排序）

- 把用户兴趣点拆成 5–15 个“可回答的问题”
- 按优先级排序（用户显式 > 高风险 > 高频用例）
- 回答格式交给 `template_qa_format.md`

