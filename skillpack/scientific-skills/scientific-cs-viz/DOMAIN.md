---
name: scientific-cs-viz
description: Data analysis and visualization workflows in Codex (数据分析/EDA/统计/可视化). Use for EDA, statistical summaries, large dataset handling, and producing publication-ready plots with matplotlib/seaborn/plotly, plus markdown reports and tables.
metadata:
  author: local-skillpack
  sources: exploratory-data-analysis, matplotlib, seaborn, plotly, polars, dask, statistical-analysis
---

# Scientific CS — Data Analysis & Visualization

## What this skill merges (from upstream)
- `exploratory-data-analysis`: file-first EDA + markdown report mindset
- `matplotlib` / `seaborn` / `plotly`: plotting and figure hygiene
- `polars` / `dask`: scale-up knobs when pandas is too slow
- `statistical-analysis`: basic statistical tests and reporting

## Default workflow (no subagents)
- Produce `reports/eda.md` and keep it as the single source of truth for:
  - dataset schema
  - missingness
  - distributions
  - key plots (linked)
  - modeling/next-step recommendations

## Artifacts checklist
- `reports/eda.md`
- `tables/schema.csv` and/or `tables/summary.csv`
- `figures/` with deterministic filenames (no random timestamps)

## References
- Report template: `scientific-cs-viz/references/eda_report_template.md`
- Plotting rules: `scientific-cs-viz/references/plotting_guidelines.md`
- Scaling notes: `scientific-cs-viz/references/scaling_notes.md`
