---
name: scientific-cs-writing
description: Scientific communication workflows in Codex (科研写作/文献综述/引用管理/BibTeX/论文). Use for literature review, citation hygiene, IMRAD drafting, peer-review style critique, and producing LaTeX/Markdown artifacts (paper/slides/posters) with reproducible provenance.
metadata:
  author: local-skillpack
  sources: scientific-writing, literature-review, citation-management, peer-review, scientific-slides, scientific-schematics, latex-posters, venue-templates
---

# Scientific CS — Writing

## What this skill merges (from upstream)
- `literature-review`: structured search + synthesis + output discipline
- `citation-management`: BibTeX accuracy + DOI/PMID/arXiv metadata hygiene
- `scientific-writing`: IMRAD drafting discipline
- `peer-review`: critique checklist (clarity, novelty, evaluation, limitations)
- Optional “deliverables” skills:
  - `scientific-slides`, `latex-posters`, `venue-templates`, `scientific-schematics`

## Default workflow (no subagents)

1) **Scope + claims**
- Define: what you are claiming, what evidence you need, evaluation plan (CS papers).

2) **Plan artifacts**
- `reports/lit_review.md`
- `reports/paper_draft.md` or `paper/main.tex` (if LaTeX requested)
- `refs/references.bib`

3) **Citations**
- Never fabricate citations; if metadata is incomplete, mark as TODO and request missing DOI/URL.

## Templates
- IMRAD skeleton: `scientific-cs-writing/references/imrad_template.md`
- Literature review skeleton: `scientific-cs-writing/references/lit_review_template.md`
- Citation hygiene rules: `scientific-cs-writing/references/citation_rules.md`
