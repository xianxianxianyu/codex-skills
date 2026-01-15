---
name: scientific-skills
description: Scientific CS workflow router for Codex: imaging (DICOM/WSI), ML (scikit-learn/PyTorch), EDA & visualization, lab automation (Opentrons), and scientific writing (lit review/IMRAD/BibTeX). Use when you want reliable plan→artifact execution with runbooks/checkpoints.
---

# Scientific Skills (Scientific CS)

## How to use
1) Intake: goal, inputs, constraints, definition of done.
2) Route to a domain playbook:
   - Imaging: `scientific-cs-imaging/DOMAIN.md`
   - ML: `scientific-cs-ml/DOMAIN.md`
   - Viz/EDA: `scientific-cs-viz/DOMAIN.md`
   - Lab automation: `scientific-cs-lab-automation/DOMAIN.md`
   - Writing: `scientific-cs-writing/DOMAIN.md`
3) Plan with `update_plan` (<= 4 steps); each step produces an artifact (report/table/figure/script/protocol).
4) Keep a runbook as durable memory: `runs/YYYY-MM-DD-<topic>.md` (template: `scientific-cs/references/runbook_template.md`).
5) Execute one plan step at a time; verify artifacts exist and are readable.

## Notes
- Prefer “file-first” outputs (reports/tables/figures) over long chat prose.
- If unsure which domain applies, start with the protocol in `scientific-cs/DOMAIN.md`.
