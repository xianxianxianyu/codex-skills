---
name: scientific-cs-imaging
description: Imaging-focused scientific workflows in Codex (成像/医学影像/DICOM, 病理WSI, 显微数据). Use for DICOM metadata/pixel extraction, anonymization, WSI tiling, pathology pipelines, imaging EDA, and generating reproducible analysis reports and figures.
metadata:
  author: local-skillpack
  sources: pydicom, pathml, exploratory-data-analysis
---

# Scientific CS — Imaging

## What this skill merges (from upstream)
- `pydicom`: DICOM read/write, tags, anonymization, pixel extraction
- `pathml`: WSI / computational pathology pipelines and ML adjacency
- `exploratory-data-analysis`: “file-first” EDA mindset (detect format → report → next steps)

## Default workflow (no subagents)

1) **Intake**
- Ask: modality (CT/MRI/X-ray/US/WSI), file types (`.dcm`, `.nii`, `.svs`, `.tiff`), expected outputs.

2) **Plan**
- Use `update_plan` with explicit artifacts:
  - `reports/imaging_overview.md` (metadata + dataset shape)
  - `figures/<...>.png` (sample slices/tiles)
  - `tables/metadata.csv` (key tags / summary)

3) **Execute**
- Prefer minimal, deterministic scripts (not notebooks) for reproducibility.

4) **Review**
- Verify: can open one file, extract pixels, render one plot.

## Practical guardrails
- Always separate **metadata** vs **pixel arrays** in outputs.
- For privacy: never print raw patient identifiers; if present, anonymize first.
- Store large binaries outside reports; reports should reference paths.

## References
- DICOM quickstart: `scientific-cs-imaging/references/dicom_quickstart.md`
- WSI quickstart: `scientific-cs-imaging/references/wsi_pathology_quickstart.md`
- Imaging EDA checklist: `scientific-cs-imaging/references/imaging_eda_checklist.md`
