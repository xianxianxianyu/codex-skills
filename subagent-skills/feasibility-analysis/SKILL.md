---
name: feasibility-analysis
description: Convert a PRD or requirements into a technical feasibility analysis with options, risks, cost and timeline estimates, and a recommendation. Use when the user asks "is this feasible" or wants a feasibility report.
---

# Feasibility Analysis

## Goal

- Produce a technical feasibility document based on the PRD.

## Output

- Default output path: `docs/feasibility.md` (ask the user if they prefer another location).
- Follow the Doc Contract format.

## Doc Contract

- Follow `../_shared/doc-contract.md`.

## Inputs to Confirm

- PRD or requirements doc
- Current stack, constraints, and team capabilities
- Timeline and budget expectations

## Workflow

1. Identify 2-3 implementation options.
2. For option ideation, use `digital-brain` if helpful and keep a short list.
3. For scientific domains, route through `scientific-cs` and consult the relevant `scientific-cs-*` skill.
4. For each option, list dependencies and assumptions.
5. Estimate cost, timeline, and complexity.
6. Build a risk matrix and list unknowns.
7. Recommend a path and outline an MVP plan.
8. Validate with `references/feasibility-checklist.md`.

## Ideation and Domain Routing

- Use `digital-brain` to expand and capture alternative approaches when needed.
- For scientific domains, start with `scientific-cs` to choose the domain, then use these skills for constraints and artifacts:
  - Imaging: `scientific-cs-imaging`
  - ML: `scientific-cs-ml`
  - Viz/EDA: `scientific-cs-viz`
  - Lab automation: `scientific-cs-lab-automation`
  - Scientific writing: `scientific-cs-writing`

## Collaboration

- Use `project-development` for project structure or cost framing.
- Use `evaluation` to define success metrics or quality gates.
- Use `tool-design` if tool interfaces are a key risk.

## References

- `../_shared/doc-contract.md`
- `references/feasibility-template.md`
- `references/risk-matrix.md`
- `references/feasibility-checklist.md`
- `references/output-example.md`
- `references/output-example-scientific.md`

