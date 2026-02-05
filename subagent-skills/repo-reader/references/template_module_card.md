Purpose: 模块卡片固定字段模板（“短而全”），用于 Modules 章节的输出约束。
When to read: 阶段 2 写 Modules 章节前；所有非轻量模式建议读。
Inputs: Pass1 模块候选；入口可达性；依赖边界；配置/外部依赖线索。
Outputs: N 张模块卡（Top N 由 Mode 决定）。
Do NOT: 不要写流程叙事（交给 Key Flows）；不要把同一事实在多张卡里重复。

# Module Card（模板）

每个模块 5–8 行为宜，字段缺失就写 “Unknown/推测”：

- Name：
- Responsibility（1 行）：
- Entry / Touchpoints（被谁调用/从哪里进入）：
- Key Files（2–4 个路径）：
- Depends On（上游依赖）：
- Exposes To（下游被谁用）：
- Data / State（若有）：
- Extension Points（若有）：

