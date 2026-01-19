# Doc Contract v1

Use this contract for all subagent output documents.

## Required Header

Doc-ID: <unique id>
Doc-Type: qa | prd | feasibility | implementation | params
Owner: <name or team>
Date: YYYY-MM-DD
Version: v1.x
Status: draft | review | final
Source: <user prompt or input docs>

## Doc-ID Format

- qa: QA-YYYY-MM-DD-###
- prd: PRD-YYYY-MM-DD-###
- feasibility: FEAS-YYYY-MM-DD-###
- implementation: IMPL-YYYY-MM-DD-###
- params: PARAM-YYYY-MM-DD-###

## Required Sections

## Language

- 文档正文用中文撰写；术语/字段名/命令/代码/路径/标识符等可以保留英文原样。

## Summary
- 3 to 7 concise bullets

## Assumptions
- List assumptions or write "None"

## Open Questions
- List open questions or write "None"

## Next Steps
- Optional

## Doc-Type Sections

### QA (qa)
- Question
- Answer
- Context (optional)
- References (optional)

### PRD (prd)
- Executive Summary
- Problem Statement
- Goals (SMART)
- Scope / Non-Goals
- Users and Personas
- User Stories
- Functional Requirements (REQ-XXX + Acceptance Criteria)
- Non-Functional Requirements
- Constraints and Assumptions
- Risks and Open Questions
- Metrics and Validation
- Rollout and Milestones

### Feasibility (feasibility)
- Inputs and Assumptions
- Options (A/B/...) with Pros/Cons
- Comparison
- Risk Matrix
- Cost and Timeline
- Recommendation
- MVP Path
- Open Questions

### Implementation (implementation)
- Plan Summary
- Changes (by file/module)
- Tests Run (or Not Run + reason)
- Risks and Rollback Notes
- Follow-ups

### Parameters (params)
- Context (system/module)
- Parameter Table (name, type, default, range, unit, dependencies)
- Constraint Rules
- Preset Profiles (safe/balanced/high)
- Validation Notes

## Length and Structure

- If the doc exceeds 200 lines or ~2 pages, add a TL;DR at the top.
- Keep details in an Appendix section when possible.

## Default Paths

- qa: `docs/qa-notes.md`
- prd: `docs/prd.md`
- feasibility: `docs/feasibility.md`
- implementation: `docs/implementation-report.md`
- params: `docs/parameter-spec.md`

## Multi-Entry Files

- If appending multiple entries in one file, separate entries with a line: "---".
- Each entry must include the Required Header and Required Sections.


