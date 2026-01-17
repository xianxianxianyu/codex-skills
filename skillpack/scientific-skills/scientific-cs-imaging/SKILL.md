---
name: scientific-cs-imaging
description: Medical imaging & digital pathology (DICOM/WSI) workflows for Codex. Use for pydicom/pathology tiling/QC, anonymization, feature extraction, and reproducible image EDA reports.
---

# Scientific CS: Imaging

## Scope
- DICOM IO, metadata/tag inspection, de-identification, pixel extraction.
- WSI (whole-slide images), tiling, patch datasets, basic QC and stats.
- Imaging-focused EDA reports and figure generation.

## Workflow (Codex, no subagents)
1) Confirm inputs (file paths, formats), constraints (privacy, compute), and deliverables (report/figures/scripts).
2) Create a short plan with `update_plan` (<= 4 steps).
3) Execute step-by-step and write artifacts to disk (prefer `reports/`, `figures/`, `scripts/`).
4) Record decisions and outputs in a runbook (see `../scientific-cs/references/runbook_template.md`).

Use the detailed playbook in `DOMAIN.md`.
