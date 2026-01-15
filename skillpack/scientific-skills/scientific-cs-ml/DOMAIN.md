---
name: scientific-cs-ml
description: Machine learning workflows in Codex (机器学习/深度学习; scikit-learn; PyTorch/Lightning). Use for training/evaluation pipelines, metrics, reproducibility, experiment structure, and model reporting.
metadata:
  author: local-skillpack
  sources: scikit-learn, pytorch-lightning, shap, transformers, torch_geometric
---

# Scientific CS — Machine Learning

## What this skill merges (from upstream)
- `scikit-learn`: pipeline discipline, preprocessing, CV, metrics, model selection
- `pytorch-lightning`: training loop standardization, callbacks, checkpointing, logging
- Optional concepts pulled in when needed:
  - `transformers` (NLP/Vision foundation models)
  - `torch_geometric` (GNN)
  - `shap` (interpretability)

## Default workflow (no subagents)

1) **Define task contract**
- Inputs: X/y, schema, train/val/test split rules
- Output metric(s): primary + secondary, plus baseline

2) **Plan artifacts**
- `reports/ml_experiment.md` (data, model, metrics, ablations)
- `tables/metrics.csv`
- `figures/roc.png` / `figures/loss_curve.png` (as applicable)
- `models/` (checkpoints or serialized sklearn pipeline)

3) **Execution discipline**
- Start with a simple baseline (sklearn) before deep learning unless user forbids.
- Make runs reproducible: seeds, deterministic splits, config snapshot.

## Templates
- scikit-learn pipeline skeleton: `scientific-cs-ml/scripts/sklearn_pipeline_template.py`
- LightningModule skeleton: `scientific-cs-ml/scripts/lightning_module_template.py`
- Experiment report template: `scientific-cs-ml/references/experiment_report_template.md`
