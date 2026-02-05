Purpose: frontend 架构差分（仅补充 frontend 特有关注点）。
When to read: 阶段 2；repo 类型推断为 frontend 时，在 generic 之后读作补丁。
Inputs: 路由/页面目录、状态管理、数据请求层、构建工具、组件库等线索。
Outputs: 在 Architecture Story 中追加/补全 frontend 特有小节与检查点。
Do NOT: 不要重复 generic 的章节骨架；不要把每一点写成长文。

# Frontend 差分补丁

把下面这些点按“是否存在”追加到 Architecture Story（每点 1–3 行即可）：

- Routing：路由定义与页面结构（Next/React Router 等）
- State：全局状态（Redux/Zustand/Context）与边界
- Data Fetching：请求封装、缓存（SWR/React Query）、错误处理
- UI 体系：组件库/设计系统、样式方案（CSS Modules/Tailwind）
- Build：构建脚本、环境变量注入、打包产物

