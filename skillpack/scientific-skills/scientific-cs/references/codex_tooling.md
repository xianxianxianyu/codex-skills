# Codex Tooling Patterns (No Subagents)

## The 3 primitives

1) `update_plan` 鈥?your 鈥渟cheduler鈥?- Keep 鈮?7 steps.
- Exactly one `in_progress` at a time.
- Each step ends with an artifact or a verified command output.

2) `shell_command` 鈥?your 鈥渋nstrumentation鈥?- Prefer read-only recon first (`rg`, `Get-Content`, `Get-ChildItem`).
- For execution steps, record the command and short outcome in the runbook.

3) `apply_patch` 鈥?your 鈥渁tomic writer鈥?- Patch files in one cohesive change per step.
- Avoid mixing unrelated edits in a single patch.

## No-subagent workflow pattern

Replace 鈥減lanner agent / executor agent / reviewer agent鈥?with phases:
- **Plan**: create/refresh `update_plan` + write runbook header
- **Execute**: do exactly one plan step
- **Review**: verify the artifact, then mark step done

## Recommended project folders (when doing actual work)

- `runs/` 鈥?durable runbooks
- `reports/` 鈥?markdown reports
- `figures/` 鈥?plots
- `tables/` 鈥?CSV/Parquet summaries
- `scripts/` 鈥?reproducible scripts (preferred over notebooks)

## Installing this local skillpack into Codex later

Codex typically loads skills from `~/.codex/skills/<skill-name>/SKILL.md`.

Examples:
- Windows: `C:\\Users\\<YOU>\\.codex\\skills\\scientific-skills\\SKILL.md`
- macOS/Linux: `~/.codex/skills/scientific-skills/SKILL.md`

Copy the `scientific-skills/` folder into that location (folder name should match `name:` in frontmatter).



