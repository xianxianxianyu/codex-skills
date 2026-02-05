Purpose: 生成模块级 mini-doc 的套路与章节骨架（深入一个模块）。
When to read: 第二次提问选择“模块深挖”后；深入模式默认读，标准模式按需读。
Inputs: 目标模块路径/命名空间；模块卡；相关入口点；关键调用链/依赖。
Outputs: `MODULE_<module>_MINIDOC.md`（模块责任、关键对象、调用链、扩展点、常见坑）。
Do NOT: 不要把整个模块源码复述出来；用“结构 + 关键锚点 + 调用链”讲清楚即可。

# Module Mini-Doc（套路）

## 1. What this module is（1 段）

- Responsibility（1 行）
- In/Out：谁调用它、它依赖谁（引用 Modules 章节）

## 2. Key Concepts（3–6 条）

- 关键对象/接口/数据结构（名称 + 1 行）

## 3. Control Flow（短链路）

- 给出 1 条最关键的调用链（入口 → 关键函数 → 外部依赖）
- 若有异步/事件：标出触发点与处理器

## 4. Extension Points（若有）

- 可扩展点：hook/event/interface/registry
- 最小示例：要改哪些文件（列 3–6 个路径即可）

## 5. Pitfalls（常见坑，2–5 条）

- 典型坑：隐式依赖、初始化顺序、幂等/重试、错误吞掉、测试缺口

