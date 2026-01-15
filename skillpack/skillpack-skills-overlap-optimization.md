# Skillpack skills 重叠/冲突分析与优化建议

你这个 `D:\\code\\Maestrom engine\\skillpack` 里目前一共 **27 个可索引的 skills（SKILL.md）**，`name:` 没有重复（不会直接互相覆盖），但确实存在“触发重叠/抢触发/上下文膨胀”的冲突点，以及一些“Codex skills 规范/可移植性”问题。

- **结构/索引风险（不是冲突，但会影响可维护性）**
  - 目录名 ≠ `name:`（安装/拷贝时容易混乱）：`context-engineering-collection`、`designer`、`digital-brain`、`reasoning-trace-optimizer`、`skill-template`（对应路径在 `skillpack/Agent-Skills-for-Context-Engineering/...` 和 `skillpack/claude-designer-skill/...`）。
  - 有 5 个 skill 的 frontmatter **不止 `name/description`**：`web-artifacts-builder`、`webapp-testing`、`theme-factory`（`license`），`digital-brain`、`book-sft-pipeline`（`version`）。如果你后续用严格的“技能打包/校验器”（很多只接受 name+description），这些会踩雷。

- **主要重叠/冲突簇（最容易同时触发一堆 skills）**
  - **文档类冲突**：`prd-taskmaster` ↔ `doc-coauthoring` ↔ `theme-factory` ↔ `scientific-skills`（写作）↔ `digital-brain`（写 post）
    - 常见场景：你说“写 PRD/写 spec/写文档/做 slides”，会同时命中好几个。
  - **UI/前端类冲突**：`ui-ux-pro-max` ↔ `designer` ↔ `web-artifacts-builder` ↔ `theme-factory` ↔ `webapp-testing`
    - `ui-ux-pro-max` 的 description 覆盖面极广（而且很长），很容易“只要提到 UI/页面/React/Tailwind 就触发”。
  - **评测类冲突**：`evaluation` ↔ `advanced-evaluation`
    - 两个 description 都包含 *rubrics*、*LLM-as-judge*、*evaluation pipelines* 等，属于典型重复触发。
  - **Context/Agent 工程类冲突**：`context-engineering-collection` ↔（`context-*`/`tool-design`/`memory-systems`/`multi-agent-patterns`/`hosted-agents`…）
    - 这里最大的问题是 `context-engineering-collection` 太“总纲”，很容易在你聊 agent/system 相关时被动加载，导致总是额外占上下文。

- **更实际的“可用性冲突”（比触发重叠更致命）**
  - `doc-coauthoring` 的正文里大量引用 Claude/Artifacts 工具（如 `create_file`/`str_replace`/connectors/subagents），跟 Codex CLI 的工具体系（`apply_patch`/`shell_command`/`update_plan`）不一致，容易把你带偏。
  - `ui-ux-pro-max` 的正文示例命令写的是 `python3 .codex/scripts/search.py`，但你实际文件在 `skillpack/ui-ux-pro-max/scripts/search.py`（路径不一致会直接跑不起来）。

## 综合优化建议（按收益从高到低）

1) **把“总纲/合集”类 skill 去索引化**：建议别让 `skillpack/Agent-Skills-for-Context-Engineering/SKILL.md`（`context-engineering-collection`）自动触发；改成“文档/索引文件”（例如重命名 `SKILL.md` 为 `COLLECTION.md`），只保留下面那些“具体技能”可触发。这样能显著减少上下文膨胀与抢触发。

2) **UI/文档/评测三大簇各保留一个“自动触发主力”，其余改成“手动点名”**（通过把 description 写得更窄来实现）：
   - PRD：只留 `prd-taskmaster` 自动触发；`doc-coauthoring` 收敛到“非 PRD 的工程文档（ADR/RFC/设计说明）”；`theme-factory` 收敛到“仅当用户说 theme/配色/风格统一/套模板”才触发。
   - UI：在 `ui-ux-pro-max` vs `designer` 里选一个当“自动触发”；另一个改成“只有点名或特定关键词才触发”。`web-artifacts-builder` 保持“要做复杂多组件 artifact 才触发”；`webapp-testing` 保持“Playwright/测试/截图/日志”触发即可。
   - 评测：建议 `advanced-evaluation` 负责 LLM-as-judge/偏差/成对比较；`evaluation` 只保留“评测框架/质量门禁/agent regression testing”，从 description 里去掉 LLM-as-judge 相关关键词，避免双触发。

3) **把 tool 指令对齐到 Codex CLI**：优先修 `doc-coauthoring`（替换掉 `create_file/str_replace` 之类的工具叙述）和 `ui-ux-pro-max`（把示例命令路径改成 `python scripts/search.py ...` 或给出正确相对路径）。

4) **清理 frontmatter 到只剩 `name/description`**（至少对你会打包/迁移的那批）：把 `license:`/`version:` 从 frontmatter 移到正文里，避免被严格解析器拒绝。

## 可选执行策略

- A) **保守**：只做“去索引化总纲 + 修正明显跑不起来的指令（doc-coauthoring / ui-ux-pro-max）”
- B) **激进**：再进一步把每个冲突簇的 description 收敛，确保默认只会触发 1 个主力 skill（其余手动点名）
