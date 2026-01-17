---
name: scientific-cs-ml
description: Machine learning workflows for Codex (scikit-learn/PyTorch). Use for baselines, pipelines, metrics/CV, experiment hygiene, and reproducible training/evaluation runs.
---

# Scientific CS: Machine Learning

## Scope
- Problem framing, dataset splits, baselines, metrics, and error analysis.
- scikit-learn pipelines (preprocessing + model + CV).
- PyTorch training loops or Lightning-style structure when appropriate.

## Workflow (Codex, no subagents)
1) Confirm data shape/labels, target metric, and constraints.
2) Plan with `update_plan` (<= 4 steps) where each step produces an artifact (notebook/script, metrics table, figure, model card).
3) Run and verify locally; keep logs/results in a stable folder (e.g., `runs/<topic>/`).
4) Write a brief runbook entry for reproducibility (see `../scientific-cs/references/runbook_template.md`).

Use the detailed playbook in `DOMAIN.md`.
