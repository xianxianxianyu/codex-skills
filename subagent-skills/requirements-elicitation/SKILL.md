---
name: requirements-elicitation
description: Turn a project idea or prompt into a structured PRD or requirements document. Use when the user asks for requirements, PRD, specs, proposals, scope definition, or acceptance criteria.
---

# Requirements Elicitation

## Goal

- Produce a clear, structured PRD-style requirements document.

## Output

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。
- Default output path: `docs/prd.md` (ask the user if they prefer another location).
- Follow the Doc Contract format.

## Doc Contract

- Follow `../_shared/doc-contract.md`.

## Inputs to Collect

- Problem statement and target users
- Goals and success metrics (baseline, target, timeframe)
- Scope and non-goals
- Key user stories and edge cases
- Functional and non-functional requirements
- Constraints, assumptions, and dependencies
- Risks, open questions, and timeline expectations

## Workflow

1. Ask 3-7 clarifying questions, one at a time.
2. Confirm scope and non-goals explicitly.
3. If brainstorming is needed, use `digital-brain` content module patterns to expand options and keep a short list.
4. If the domain is scientific, route through `scientific-cs` and consult the relevant `scientific-cs-*` skill for constraints and artifacts.
5. Draft the PRD using `references/prd-template.md`.
6. Write requirements as REQ-001, REQ-002, etc., each with acceptance criteria.
7. List open questions and assumptions at the end.
8. Validate with `references/prd-checklist.md`.

## Ideation and Domain Routing

- For idea expansion or brainstorming, use `digital-brain` content module patterns and capture options succinctly.
- For scientific domains, start with `scientific-cs` to choose the domain, then use these skills for constraints and artifacts:
  - Imaging: `scientific-cs-imaging`
  - ML: `scientific-cs-ml`
  - Viz/EDA: `scientific-cs-viz`
  - Lab automation: `scientific-cs-lab-automation`
  - Scientific writing: `scientific-cs-writing`

## Collaboration

- If the project uses Taskmaster, hand off to `prd-taskmaster`.
- If the user wants a guided writing workflow, use `doc-coauthoring`.

## References

- `../_shared/doc-contract.md`
- `references/prd-template.md`
- `references/requirements-questions.md`
- `references/prd-checklist.md`
- `references/output-example.md`
- `references/output-example-scientific.md`



