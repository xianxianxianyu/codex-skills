---
name: scientific-cs-lab-automation
description: Experiment automation workflows for Codex (Opentrons Protocol API v2). Use for protocol drafting, deck/labware planning, simulation, and reproducible automation runbooks.
---

# Scientific CS: Lab Automation

## Scope
- Opentrons protocol authoring (API v2), labware/deck layout, pipetting logic.
- Simulation-first workflow and safety checks (volumes, tip usage, labware).
- Protocol documentation and runbook discipline.

## Workflow (Codex, no subagents)
1) Confirm hardware (robot/pipettes), labware, reagents, volumes, and constraints.
2) Plan with `update_plan` (<= 4 steps): deck plan → protocol draft → simulation checks → final report.
3) Produce artifacts: `protocols/<name>.py`, `deck_plan.md`, `runbook.md`.
4) Record assumptions, calibration notes, and versioning in a runbook (see `../scientific-cs/references/runbook_template.md`).

Use the detailed playbook in `DOMAIN.md`.
