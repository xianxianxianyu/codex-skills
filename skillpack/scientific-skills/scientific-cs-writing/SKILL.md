---
name: scientific-cs-writing
description: Scientific writing workflows for Codex. Use for literature review, IMRAD drafting, citation hygiene (BibTeX), and peer-review checklists with file-first outputs.
---

# Scientific CS: Scientific Writing

## Scope
- Literature search/synthesis and structured notes.
- IMRAD drafting (paper/report), related work organization, and claims-to-evidence tracking.
- Citation hygiene (BibTeX/DOI), and reviewer-style critique checklists.

## Workflow (Codex, no subagents)
1) Clarify target venue/audience, format constraints, and sources.
2) Plan with `update_plan` (<= 4 steps) where each step writes an artifact (outline, related-work table, draft section, references file).
3) Keep outputs in `manuscript/` and `references/` and update a runbook for decisions.
4) Run a “peer review” pass using checklists before calling it done.

Use the detailed playbook in `DOMAIN.md`.
