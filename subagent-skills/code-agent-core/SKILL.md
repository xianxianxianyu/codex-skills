---
name: code-agent-core
description: Implement code changes based on requirements and feasibility, with planning, edits, self-checks, tests, and a clear change summary. Use when the user asks to implement, modify, or debug code.
---

# Code Agent Core

## Preconditions

- Ensure requirements are clear. If missing, ask or hand off to `requirements-elicitation`.
- If feasibility is unclear or risky, hand off to `feasibility-analysis`.

## Output

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。
- Default output path: `docs/implementation-report.md` (ask the user if they prefer another location).
- Follow the Doc Contract format.

## Doc Contract

- Follow `../_shared/doc-contract.md`.

## Workflow

1. Read relevant files and gather context.
2. Propose a brief plan for non-trivial changes.
3. Apply minimal edits with tight scope.
4. Run a quick self-check (lint, build, or tests) when feasible.
5. Summarize changes, tests, and risks.

## Frontend Work

- If the task includes UI/UX or frontend layout, use `ui-ux-pro-max` for layout, palette, component patterns, and UX checks.
- If the task requires a complex web artifact (multi-component React/Tailwind/shadcn), use `web-artifacts-builder`.
- Record key design decisions in the implementation report.

## Parameter Sanity

- If the change affects runtime parameters or defaults, use `parameter-sanity` to produce a parameter spec.
- Ensure parameter defaults are conservative and internally consistent.

## Rules

- Do not change unrelated files.
- Avoid destructive commands unless explicitly requested.
- Keep edits small and reversible.
- Document assumptions and open questions.

## Output Checklist

- List modified files.
- List tests run (or "not run" with reason).
- Note risks and suggested follow-ups.

## References

- `../_shared/doc-contract.md`
- `references/change-checklist.md`
- `references/test-checklist.md`
- `references/output-example.md`
- `ui-ux-pro-max`
- `web-artifacts-builder`
- `parameter-sanity`



