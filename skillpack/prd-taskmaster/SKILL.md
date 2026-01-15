---
name: prd-taskmaster
description: "Generate a Taskmaster-ready PRD at .taskmaster/docs/prd.md and validate it. Use when the user asks for a PRD/product requirements/spec, or mentions Taskmaster/task breakdown."
---

# PRD Taskmaster (Codex)

Generate an engineer-focused PRD optimized for Taskmaster task generation, stored at `.taskmaster/docs/prd.md`.

## Outputs

- Creates/updates: `.taskmaster/docs/prd.md`
- Optionally creates: `.taskmaster/docs/task-hints.md`
- Optionally creates/updates: `.taskmaster/docs/progress.md`

## Operating Rules

- Ask clarifying questions when requirements are underspecified; ask **one question at a time**.
- Prefer multiple-choice when it helps the user answer quickly.
- Do not invent requirements, dependencies, or metrics; ask.
- Write requirements so they can become tasks: atomic, testable, measurable.

## Workflow

### 1) Detect existing PRD

Check whether `.taskmaster/docs/prd.md` already exists.

If it exists, ask the user which action to take:

1. **Update** the existing PRD (recommended)
2. **Replace** it (move old file to `.taskmaster/docs/prd.backup.<timestamp>.md`)
3. **Review only** (summarize gaps and next questions)

### 2) Ensure Taskmaster project scaffolding exists

If `.taskmaster/` does not exist, create it:

- Create directories: `.taskmaster/`, `.taskmaster/docs/`, `.taskmaster/tasks/`, `.taskmaster/reports/`, `.taskmaster/scripts/`, `.taskmaster/state/`
- Ensure `.gitignore` excludes:
  - `.taskmaster/state.json`
  - `.taskmaster/tasks/`
  - `.taskmaster/reports/`

If you want to use the bundled helper scripts, copy them into the project:

- Copy from this skill install folder:
  - Windows: `%USERPROFILE%\\.codex\\skills\\prd-taskmaster\\.taskmaster\\scripts\\*`
  - macOS/Linux: `~/.codex/skills/prd-taskmaster/.taskmaster/scripts/*`
- Copy to project: `.taskmaster/scripts/`

### 3) Requirements discovery (ask sequentially)

Collect answers for:

- **Problem & users**: who is affected, current pain, why now
- **Goals**: SMART metrics (baseline/target/timeframe)
- **Scope**: in-scope vs out-of-scope
- **User stories**: key scenarios + edge cases
- **Functional requirements**: REQ-XXX with acceptance criteria
- **Non-functional requirements**: latency/throughput, availability, security, privacy
- **Constraints**: tech stack, hosting, compliance, deadlines
- **Integrations**: APIs, data sources, auth, webhooks
- **Data**: entities, schema hints, retention
- **Observability**: logs/metrics/traces, audit logs
- **Rollout**: migration plan, feature flags, backward compatibility

### 4) Generate PRD

Use `templates/taskmaster-prd-comprehensive.md` as the base structure.

Write the PRD to: `.taskmaster/docs/prd.md`

PRD quality requirements:

- Include clear sections: Executive Summary, Problem Statement (user + business impact), Goals (SMART), User Stories, Functional Requirements (REQ-XXX), Non-Functional Requirements (with numeric targets), Technical Considerations, Roadmap, Out of Scope, Open Questions & Risks, Validation Checkpoints.
- For each `REQ-XXX`, include:
  - Description
  - Acceptance criteria (checkbox list)
  - Technical specification (API/schema/examples when applicable)
  - Task breakdown hints (Small/Medium/Large)
  - Dependencies (None or REQ-XXX)

Optionally write `task-hints.md` if it helps Taskmaster generation.

### 5) Validate before handoff

Use `reference/validation-checklist.md` as the source of truth.

Validation outcome:

- If any **required** checks fail: fix the PRD and re-validate.
- If only warnings remain: summarize warnings and suggest improvements.

### 6) Taskmaster handoff (commands to show user)

Do not run network installs automatically. Provide the commands and let the user decide:

- Install: `npm install -g task-master-ai`
- Initialize: `taskmaster init`
- Generate tasks from PRD: `taskmaster generate`

If `taskmaster` already exists, skip install and go straight to init/generate.

## Notes on Automation Modes

This Codex skill focuses on **PRD creation + validation + Taskmaster handoff**. If the user asks to execute tasks autonomously, switch to a plan (`update_plan`) and implement tasks sequentially with checkpoints.