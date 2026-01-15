---
name: scientific-cs-lab-automation
description: Lab automation workflows for Codex (实验自动化/Opentrons/OT-2/Flex). Use for authoring Opentrons protocols, deck/labware planning, simulation discipline, and generating reproducible protocol artifacts and runbooks.
metadata:
  author: local-skillpack
  sources: opentrons-integration, pylabrobot, protocolsio-integration, benchling-integration
---

# Scientific CS — Lab Automation

## What this skill merges (from upstream)
- `opentrons-integration`: Protocol API v2 structure, labware/deck, pipetting patterns, simulation mindset
- `pylabrobot`: multi-vendor abstraction (use only if needed)
- `protocolsio-integration`: aligning code with documented wet-lab steps
- `benchling-integration`: experiment record hygiene (optional)

## Default workflow (no subagents)

1) **Protocol spec**
- robot: OT-2 vs Flex, apiLevel, modules, labware definitions
- volumes, tips, mixing, timing, temperature constraints

2) **Plan artifacts**
- `protocols/<name>.py` (Opentrons protocol)
- `reports/protocol_spec.md` (deck map + assumptions)
- `runs/...` runbook

3) **Verification**
- At minimum: “protocol imports” and passes basic static sanity checks.

## Templates
- Opentrons protocol skeleton: `scientific-cs-lab-automation/references/opentrons_protocol_template.py`
- Protocol spec template: `scientific-cs-lab-automation/references/protocol_spec_template.md`
