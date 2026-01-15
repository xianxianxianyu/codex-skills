# Codex Skills Audit Report

Generated: 2026-01-15 18:15

## Snapshot layout
- Codex skills copied into: `E:\OS\skillpack\codex-skills`
- Scientific CS skillpack copied into: `E:\OS\skillpack\scientific-skills`
- Note: the original `E:\OS\skillpack\scientific-cs*` folders could not be moved/deleted in this environment (missing delete permissions). Treat `scientific-skills/` as canonical.

## Inventory
- Codex skills (`SKILL.md`) found: **28**
- Scientific skills (`SKILL.md`) found: **6**

### Codex skill names
- `advanced-evaluation`
- `bdi-mental-states`
- `book-sft-pipeline`
- `comprehensive-research-agent`
- `context-compression`
- `context-degradation`
- `context-engineering-collection`
- `context-fundamentals`
- `context-optimization`
- `designer`
- `digital-brain`
- `doc-coauthoring`
- `evaluation`
- `filesystem-context`
- `hosted-agents`
- `memory-systems`
- `multi-agent-patterns`
- `prd-taskmaster`
- `project-development`
- `reasoning-trace-optimizer`
- `skill-creator`
- `skill-installer`
- `skill-template`
- `theme-factory`
- `tool-design`
- `ui-ux-pro-max`
- `web-artifacts-builder`
- `webapp-testing`

### Scientific skill names
- `scientific-cs`
- `scientific-cs-imaging`
- `scientific-cs-lab-automation`
- `scientific-cs-ml`
- `scientific-cs-viz`
- `scientific-cs-writing`

## Duplicates (same `name:`)
No duplicate `name:` values detected across the copied sets.

## Structural conflicts
Skills where folder name != `name:` (can be confusing during installation):
- pack=`codex` folder=`Agent-Skills-for-Context-Engineering` name=`context-engineering-collection` path=`E:\OS\skillpack\codex-skills\Agent-Skills-for-Context-Engineering\SKILL.md`
- pack=`codex` folder=`claude-designer-skill` name=`designer` path=`E:\OS\skillpack\codex-skills\claude-designer-skill\SKILL.md`
- pack=`codex` folder=`template` name=`skill-template` path=`E:\OS\skillpack\codex-skills\Agent-Skills-for-Context-Engineering\template\SKILL.md`
- pack=`codex` folder=`digital-brain-skill` name=`digital-brain` path=`E:\OS\skillpack\codex-skills\Agent-Skills-for-Context-Engineering\examples\digital-brain-skill\SKILL.md`
- pack=`codex` folder=`interleaved_thinking` name=`reasoning-trace-optimizer` path=`E:\OS\skillpack\codex-skills\Agent-Skills-for-Context-Engineering\examples\interleaved_thinking\SKILL.md`

## Potential scope overlaps (heuristic)
Flags skills whose `name+description` share keywords. This suggests possible trigger overlap, not duplication.

No strong overlaps detected at the current threshold.

## Recommendations
### scientific-cs-writing vs doc-coauthoring
Keep both. Use `scientific-cs-writing` for IMRAD/citations/lit-review; use `doc-coauthoring` for general product/engineering docs and decision records.

### scientific-cs-writing vs theme-factory
Keep both. Use `scientific-cs-writing` for content structure and citation hygiene; use `theme-factory` for consistent styling of docs/slides/artifacts.

### scientific-cs-viz vs UI/UX skills
`scientific-cs-viz` is for analysis/plots/reports; use `ui-ux-pro-max` / `claude-designer-skill` for UI polish, dashboards, or frontend design.


## Next improvements (optional)
- If unwanted triggering conflicts happen in practice, refine `description:` fields to be more domain-specific (e.g., add IMRAD/BibTeX/DOI to writing; DICOM/WSI to imaging).
- If you want continuous sync from upstream `claude-scientific-skills-main`, implement a generator script (?? C) that rebuilds `scientific-skills/` from an allowlist.
