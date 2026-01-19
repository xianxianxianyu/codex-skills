# Codex Subagent Skills

一组面向 Codex 的“文档产出型”技能集合：把一次对话从“回答”升级为可提交、可复盘、可追溯的文档（QA/PRD/Feasibility/Implementation/Params）。

- 统一格式：`subagent-skills/_shared/doc-contract.md`
- 默认产物：写入当前工作目录的 `docs/`（可按任务调整路径）
- 输出要求：对话输出开头需声明“已激活技能…”，文档头需填写 `Activated-Skills:`

## Skills 清单

| skill | 用途 | 默认产物 |
|---|---|---|
| `qa-basic` | 快速问答与记录（轻量，不改代码） | `docs/qa-notes.md` |
| `requirements-elicitation` | 需求分析 / PRD（REQ-xxx + 验收标准） | `docs/prd.md` |
| `feasibility-analysis` | 可行性分析（方案对比/风险/成本/周期/推荐） | `docs/feasibility.md` |
| `code-agent-core` | 代码实现与交付报告（改动/测试/风险/回滚） | `docs/implementation-report.md` |
| `parameter-sanity` | 参数合理性校准（默认值/范围/依赖/约束/预设档位） | `docs/parameter-spec.md` |

## 推荐 Pipeline

- QA → PRD → Feasibility → Implementation → Params
- 说明：先固化问题与上下文（QA），再把需求变成可验收条目（PRD），再做方案与风险决策（Feasibility），最后落到代码交付（Implementation）与参数规范（Params）。

## 目录结构（仓库）

```
codex-skills/
  README.md
  LICENSE
  AGENTS.md
  docs/                          # 模板/示例（可选；也可作为仓库自检用）
    qa-notes.md
    prd.md
    feasibility.md
    implementation-report.md
    parameter-spec.md
  subagent-skills/               # 真正的 skills 入口
    _shared/
      doc-contract.md
    qa-basic/
    requirements-elicitation/
    feasibility-analysis/
    code-agent-core/
    parameter-sanity/
    .system/                     # 可选：与 Codex 内置 .system skills 同名的副本
```

## 安装方式

下面以 Codex 默认技能目录 `~/.codex/skills/` 为例（Windows 对应 `C:\Users\<你>\.codex\skills\`）。

### 方式 A：复制安装（推荐）

优点：最简单、最稳定；`_shared/` 相对引用也能正常工作。

Windows (PowerShell)：

```powershell
# 1) 克隆（或更新）仓库到任意位置
# git clone https://github.com/xianxianxianyu/codex-skills.git E:\OS\codex-skills

# 2) 复制 skills 到 Codex 技能目录（建议排除 .system，避免覆盖内置系统技能）
$src = "E:\OS\codex-skills\subagent-skills"
$dst = "$env:USERPROFILE\.codex\skills"
robocopy $src $dst /E /XD .system

# 3) 重启 Codex 让其重新加载 skills
```

macOS/Linux：

```bash
# 复制并保留目录结构（排除 .system）
rsync -a --exclude='.system' subagent-skills/ ~/.codex/skills/
# 然后重启 Codex
```

### 方式 B：软链接安装（适合开发/经常更新）

优点：仓库更新后无需再次复制。

Windows (管理员或已开启开发者模式)：

```powershell
$repo = "E:\OS\codex-skills\subagent-skills"
$dst  = "$env:USERPROFILE\.codex\skills"

# 为每个 skill 建目录链接（示例：qa-basic）
New-Item -ItemType SymbolicLink -Path (Join-Path $dst 'qa-basic') -Target (Join-Path $repo 'qa-basic')
New-Item -ItemType SymbolicLink -Path (Join-Path $dst '_shared')  -Target (Join-Path $repo '_shared')
# 其它 skills 同理
```

macOS/Linux：

```bash
ln -s "$PWD/subagent-skills/qa-basic" ~/.codex/skills/qa-basic
ln -s "$PWD/subagent-skills/_shared"  ~/.codex/skills/_shared
# 其它 skills 同理
```

## 使用方式

- 在对话中直接提到 skill 名称触发（例如：`qa-basic`、`requirements-elicitation`）。
- 输出文档遵循 Doc Contract：`subagent-skills/_shared/doc-contract.md`。
- 每次对话输出开头需声明：`已激活技能：<skill-name[, ...]>`。
- 每份输出文档头部需填写：`Activated-Skills: <skill-name[, ...]>`。

## 校验（可选）

如果你已安装 `skill-creator`，可用其 `quick_validate` 做结构校验：

```bash
python path/to/skill-creator/scripts/quick_validate.py subagent-skills/<skill-name>
```

## 常见问题

- 如果 Codex 报 “missing YAML frontmatter delimited by ---”，通常是 `SKILL.md` 带了 UTF-8 BOM；确保文件第一个字符就是 `---`。

## License

MIT License，见 `LICENSE`。