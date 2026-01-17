# Skill Mapping: `claude-scientific-skills-main` → `E:\OS\skillpack`

This skillpack intentionally **merges** many upstream skills to keep Codex’s always-on context small.

## Installation note (Codex)
This repo stores these skills as a pack under `E:\OS\skillpack\scientific-skills`. When installing into `~/.codex/skills`, copy each `scientific-cs*` folder as its own top-level skill directory (each contains a `SKILL.md`).

## Router
- `scientific-cs`
  - New: phase protocol + runbook pattern (Codex has no subagents)

## Imaging
- `scientific-cs-imaging` merges:
  - `pydicom` (DICOM read/write, tags, anonymization, pixel extraction)
  - `pathml` (WSI / pathology workflows, tiling discipline, ML adjacency)
  - `exploratory-data-analysis` (file-first EDA mindset; report artifacts)

## Machine learning
- `scientific-cs-ml` merges:
  - `scikit-learn` (pipelines, preprocessing, CV/metrics, baselines)
  - `pytorch-lightning` (training structure, checkpointing/logging discipline)
  - Optional concepts (only when asked): `transformers`, `torch_geometric`, `shap`

## Data analysis & visualization
- `scientific-cs-viz` merges:
  - `exploratory-data-analysis` (EDA report mindset)
  - `matplotlib`, `seaborn`, `plotly` (figure production)
  - `polars`, `dask` (scale-up knobs)
  - `statistical-analysis` (basic statistical reporting)

## Lab automation
- `scientific-cs-lab-automation` merges:
  - `opentrons-integration` (Protocol API v2, deck/labware, simulation discipline)
  - Optional: `pylabrobot` (multi-vendor abstraction)
  - Optional hygiene: `protocolsio-integration`, `benchling-integration`

## Writing
- `scientific-cs-writing` merges:
  - `literature-review` (search/synthesis discipline)
  - `citation-management` (BibTeX accuracy)
  - `scientific-writing` (IMRAD drafting)
  - `peer-review` (review checklist)
  - Optional deliverables: `scientific-slides`, `latex-posters`, `venue-templates`, `scientific-schematics`

