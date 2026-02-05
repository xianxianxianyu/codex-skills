Purpose: 工程化收口清单（存在性、覆盖、限额、重复率控制），用于交付前自检。
When to read: 交付前；每次输出结束时必读。
Inputs: 已生成的文档草稿；本次选择的 Mode、repo 类型、意图标签。
Outputs: 一份简短自检结果（3–8 条），必要时回到对应阶段修正。
Do NOT: 不要引入新流程；这是收尾检查，不是再写一遍文档。

# Checklist（交付前自检）

## 结构与流程

- 是否按顺序输出：Repo Map → Architecture → Key Flows → Q&A
- 是否在阶段 0 与阶段 1 结束各做了一次提问（含 fallback）

## references 存在性

- `SKILL.md` 列出的每个 `references/*.md` 是否都存在
- `references/index.md` 是否保持“最小可用”（不含阶段流程长文）

## Mode 限额

- 模块卡数量是否符合 Mode（Top 3/6/10）
- Key Flows 数量是否符合 Mode（1+替代 / 2 / 3–5）
- Q&A 数量是否符合 Mode（≤ 5/10/15）

## 低重复率

- Repo Map/Modules/Key Flows 是否各司其职（事实只出现一次）
- Q&A 是否优先引用锚点而非复述

## 输出示例对齐

- 是否对照 `output-example.md` 调整“密度、长度、节奏”

