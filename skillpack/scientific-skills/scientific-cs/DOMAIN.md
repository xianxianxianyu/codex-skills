---
name: scientific-cs
description: Codex skill router and workflow protocol for computer-science-adjacent scientific work (鎴愬儚/DICOM/WSI, 鏈哄櫒瀛︿範/娣卞害瀛︿範, 鏁版嵁鍒嗘瀽/EDA/鍙鍖? 瀹為獙鑷姩鍖?Opentrons, 绉戠爺鍐欎綔/鏂囩尞缁艰堪/寮曠敤). Use when you need a reliable multi-step plan without subagents, with checkpoints and durable runbooks.
metadata:
  author: local-skillpack
  scope: codex
---

# Scientific CS (Router + Workflow Protocol)

## What this skillpack is

This folder is a **Codex-oriented** subset + rewrite of ideas from `claude-scientific-skills-main`, focused on:
- Imaging (DICOM/WSI + analysis)
- Machine learning (classical + deep)
- Data analysis & visualization (EDA 鈫?stats 鈫?plots)
- Lab automation (Opentrons + protocol authoring)
- Scientific writing (lit review 鈫?IMRAD 鈫?citations)

Codex does **not** have subagents here. This skill makes complex workflows reliable by using:
- `update_plan` as the execution backbone
- A **runbook file** as durable memory / checkpointing

## Quick routing

Use one of these domain skills for the actual work:
- `scientific-cs-imaging`: DICOM / WSI / imaging EDA pipelines
- `scientific-cs-ml`: scikit-learn, PyTorch(+Lightning), experiment discipline
- `scientific-cs-viz`: EDA, statistics, Matplotlib/Seaborn/Plotly outputs
- `scientific-cs-lab-automation`: Opentrons protocols (OT-2/Flex), deck/labware, simulation discipline
- `scientific-cs-writing`: literature review, citations, paper/slide/poster writing workflows

If unsure, start with this router, then pick the domain skill once the task is classified.

## Codex workflow protocol (no subagents)

### Phase 0 鈥?Intake (clarify)
- Ask for: goal, input artifacts, constraints, 鈥渄efinition of done鈥?
- Decide domain skill(s).

### Phase 1 鈥?Plan (must use `update_plan`)
- Create a plan with 4鈥? steps maximum.
- Each step should produce an artifact (file, plot, table, report) or a verified observation (test run result).

### Phase 2 鈥?Execute (single-threaded)
- Execute **one plan step at a time**.
- After each step, update the runbook (below) and mark the plan step completed.

### Phase 3 鈥?Review (verification)
- Verify artifacts exist and are readable (paths, quick sanity checks).
- Summarize results + next actions.

## Runbook (durable memory)

Create and maintain a runbook file:
- `runs/YYYY-MM-DD-<topic>.md`

Template: `scientific-cs/references/runbook_template.md`

## Installation note (local 鈫?Codex)

This is intentionally stored in a local folder. To install into Codex later:
- Copy the `scientific-skills/` folder into your Codex skills directory so the final path is `~/.codex/skills/scientific-skills/SKILL.md`.

## References
- Workflow + checklists: `scientific-cs/references/phase_protocol.md`
- Runbook template: `scientific-cs/references/runbook_template.md`
- Codex tooling patterns: `scientific-cs/references/codex_tooling.md`
- Mapping from upstream skills: `scientific-cs/references/skill_mapping.md`



