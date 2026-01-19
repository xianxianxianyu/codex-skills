---
name: qa-basic
description: Answer quick, lightweight questions and record a short QA note. Use when the user wants a fast explanation, definition, or comparison, and does not request code changes or long-form docs.
---

# QA Basic

## Scope

- Provide concise answers from existing knowledge.
- Write a short QA note using the Doc Contract.
- Ask at most 1-2 clarifying questions.

## Output

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。
- Default path: `docs/qa-notes.md` (ask to change if needed).
- Append one entry per question.

## Doc Contract

- Follow `../_shared/doc-contract.md`.

## Triage

- If the user wants a PRD or requirements doc, hand off to `requirements-elicitation`.
- If the user wants feasibility analysis, cost, risk, or approach comparison, hand off to `feasibility-analysis`.
- If the user wants code changes, debugging, or implementation, hand off to `code-agent-core`.
- If the question is about context engineering concepts, consider `context-fundamentals` or `context-engineering-collection`.

## Guardrails

- Only edit the QA note file.
- Do not run commands unless explicitly asked.
- Do not produce long multi-step plans.

## Response Pattern

1. Answer in 3-8 sentences or bullets.
2. If key info is missing, ask one short question.
3. Offer an optional next step when appropriate.

## References

- `../_shared/doc-contract.md`
- `references/qa-triage.md`
- `references/qa-checklist.md`
- `references/output-example.md`



