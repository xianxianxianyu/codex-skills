---
name: scientific-cs-viz
description: Data analysis + visualization workflows for Codex. Use for EDA, statistical summaries, plotting (matplotlib/seaborn/plotly), and publication-quality figures/reports.
---

# Scientific CS: Data Analysis & Visualization

## Scope
- EDA, profiling, missingness/outliers, summary tables.
- Plots with clear labels, units, and reproducible styling.
- “File-first” reporting: write `report.md` + `figures/` rather than long chat outputs.

## Workflow (Codex, no subagents)
1) Clarify dataset location/format and desired outputs (tables/figures/report).
2) Plan with `update_plan` (<= 4 steps).
3) Implement with scripts/notebooks; emit figures to `figures/` and tables to `tables/`.
4) Keep assumptions and caveats in a runbook (see `../scientific-cs/references/runbook_template.md`).

Use the detailed playbook in `DOMAIN.md`.
