# Codex Subagent Skills

一组独立的 Codex 子代理技能（subagents），用于文档化地完成问答、需求、可行性、代码交付和参数合理性校准。每个 skill 以文档为主要产物，遵循统一的 Doc Contract 规范，便于跨技能共享与复用。

## 特性

- QA 快速答疑 + 结构化记录
- PRD 需求分析与输出
- 可行性分析与方案推荐
- 代码实现与交付报告
- 参数合理性校准与默认值规范
- 统一文档协议、模板、检查清单与示例

## Skills 清单

| skill | 用途 | 默认产物 |
|---|---|---|
| `qa-basic` | 快速问答与记录 | `docs/qa-notes.md` |
| `requirements-elicitation` | 需求分析 / PRD | `docs/prd.md` |
| `feasibility-analysis` | 可行性报告 | `docs/feasibility.md` |
| `code-agent-core` | 代码实现与交付 | `docs/implementation-report.md` |
| `parameter-sanity` | 参数规范与默认值校准 | `docs/parameter-spec.md` |

## 目录结构

```
codex-skills/
  README.md
  subagent-skills/
    _shared/
      doc-contract.md
    qa-basic/
    requirements-elicitation/
    feasibility-analysis/
    code-agent-core/
    parameter-sanity/
```

## Doc Contract

- 位置：`subagent-skills/_shared/doc-contract.md`
- 统一文档类型：`qa` / `prd` / `feasibility` / `implementation` / `params`
- 每个输出文档必须包含统一头部与通用结构

## 使用方式

1. 将 `subagent-skills/` 放到 Codex 的技能目录或在配置中添加该路径。
2. 在对话中直接触发 skill 名称或通过需求描述触发。
3. 产物默认写入 `docs/`，如需可在任务中指定新路径。

## 内置开源技能

以下开源 skills 已内置在 `skillpack/`，并被本仓库的 subagent skills 引用：

- `Agent-Skills-for-Context-Engineering`（含 `digital-brain`、context 系列、多代理等）
- `scientific-skills`（含 `scientific-cs` 及其子技能）
- `doc-coauthoring`
- `prd-taskmaster`
- `ui-ux-pro-max`
- `web-artifacts-builder`
- `webapp-testing`
- `claude-designer-skill`
- `theme-factory`
- `tools`

## 校验（可选）

如果你已安装 skill-creator，可用其 quick_validate 对每个 skill 做结构校验：

```
python path/to/skill-creator/scripts/quick_validate.py subagent-skills/<skill-name>
```

## 贡献

- 保持 SKILL.md 简洁、触发规则清晰
- 把长模板/清单放在 `references/`
- 变更后更新对应示例与检查清单

## License

MIT License，见 `LICENSE`。
