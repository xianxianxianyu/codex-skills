# Scientific CS — Phase Protocol (No Subagents)

## Phase 0: Intake checklist
- Problem statement: one sentence
- Input artifacts: file paths/URLs (and which are authoritative)
- Constraints: runtime, hardware, OS, license, reproducibility requirements
- Output: what files should exist at the end
- “Stop rule”: what counts as done (MVP scope)

## Phase 1: Planning rules (Codex)
- Use `update_plan` with ≤ 7 steps.
- Each step is 2–10 minutes of work.
- Each step ends with: a file created/updated OR a command run with a recorded output.
- Prefer deterministic steps: “Generate EDA report to `reports/eda.md`”, not “Explore data”.

## Phase 2: Execution rules
- One step at a time.
- Don’t mix domains in one step (e.g., don’t train + write paper in same step).
- Always keep outputs in a predictable folder:
  - `runs/` for runbooks
  - `reports/` for markdown reports
  - `figures/` for plots
  - `tables/` for CSV/Parquet summaries
  - `notebooks/` only if explicitly requested

## Phase 3: Review rules
- Verify existence of key artifacts.
- Verify at least one “sanity command” runs (import, open file, render plot) if feasible.
- Provide a short “what changed” + “how to reproduce”.

