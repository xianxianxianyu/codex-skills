# Codex Skills Audit Report

Generated: 2026-01-16

## Snapshot layout
- Skills root: `E:\OS\skillpack` (flattened; no extra wrapper directory)
- Scientific CS skillpack: `E:\OS\skillpack\scientific-skills`
- Note: `E:\OS\skillpack\codex-skills` has been removed after flattening.

## Inventory
- Total skills (`SKILL.md`) found under `E:\OS\skillpack`: **32**
- Scientific CS skills (`scientific-cs*`): **6**

### Non-scientific skill names
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
- folder=`Agent-Skills-for-Context-Engineering` name=`context-engineering-collection` path=`E:\OS\skillpack\Agent-Skills-for-Context-Engineering\SKILL.md`
- folder=`claude-designer-skill` name=`designer` path=`E:\OS\skillpack\claude-designer-skill\SKILL.md`
- folder=`template` name=`skill-template` path=`E:\OS\skillpack\Agent-Skills-for-Context-Engineering\template\SKILL.md`
- folder=`digital-brain-skill` name=`digital-brain` path=`E:\OS\skillpack\Agent-Skills-for-Context-Engineering\examples\digital-brain-skill\SKILL.md`
- folder=`interleaved_thinking` name=`reasoning-trace-optimizer` path=`E:\OS\skillpack\Agent-Skills-for-Context-Engineering\examples\interleaved_thinking\SKILL.md`
- folder=`scientific-skills` name=`scientific-cs` path=`E:\OS\skillpack\scientific-skills\SKILL.md`

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
