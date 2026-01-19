---
name: parameter-sanity
description: Validate and calibrate default parameter sets for code outputs. Use when users ask for reasonable defaults, safe parameter combinations, config tuning, or sanity checks after code changes.
---

# Parameter Sanity

## Goal

- Produce a parameter specification that is conservative, consistent, and valid.

## Output

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。
- Default output path: `docs/parameter-spec.md` (ask the user if they prefer another location).
- Follow the Doc Contract format with Doc-Type `params`.

## Doc Contract

- Follow `../_shared/doc-contract.md`.

## Inputs to Collect

- Parameter list and current defaults from code or config.
- Allowed ranges, units, and data types.
- Dependencies or constraints between parameters.
- Environment limits (hardware, latency, memory).

## Workflow

1. Read code or config to confirm parameter names and current defaults.
2. Build a parameter table with type, default, range, unit, and dependencies.
3. Define constraint rules and invalid combinations.
4. Propose 2-4 preset profiles (safe, balanced, high).
5. If combinations are unreasonable, adjust to conservative values and explain why.
6. Validate with `references/parameter-checklist.md`.

## Rules

- Do not invent parameters not present in code or explicit user input.
- Prefer conservative defaults and monotonic scaling.
- Avoid mutually exclusive or contradictory combinations.
- Record any assumptions or unknown constraints.

## References

- `../_shared/doc-contract.md`
- `references/parameter-template.md`
- `references/parameter-logic.md`
- `references/parameter-checklist.md`
- `references/output-example.md`


