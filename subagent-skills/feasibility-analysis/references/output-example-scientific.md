# Output Examples (Scientific Feasibility)

## Imaging Feasibility Example

Doc-ID: FEAS-2026-01-18-IM-001
Doc-Type: feasibility
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md

## Summary
- Two pipeline options evaluated for DICOM de-id + QC.
- Option A (batch scripts) is faster to deliver.
- Recommend Option A for MVP with a migration plan.

## Assumptions
- Shared storage is available.

## Open Questions
- Final compliance requirements for PHI handling.

## Inputs and Assumptions
Current stack: Python, shared NAS storage.

## Options
Option A: Batch scripts + report generator
- Pros: low cost, quick to implement
- Cons: limited scalability

Option B: Service-based pipeline
- Pros: scalable, real-time processing
- Cons: higher maintenance

## Comparison
Option A meets MVP timeline with lower risk.

## Risk Matrix
- PHI policy changes (Likelihood 3, Impact 4)

## Cost and Timeline
- Option A: 4 weeks, 1 engineer
- Option B: 8 weeks, 2 engineers

## Recommendation
Proceed with Option A for MVP.

## MVP Path
Batch scripts, then evaluate service in phase 2.

## Open Questions
- Confirm PHI policy.

---

## ML Feasibility Example

Doc-ID: FEAS-2026-01-18-ML-001
Doc-Type: feasibility
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md

## Summary
- Baseline model is feasible with current data.
- Main risk is class imbalance.
- Recommend a baseline + resampling MVP.

## Assumptions
- Labels are consistent across datasets.

## Open Questions
- Final evaluation metric for release gate.

## Inputs and Assumptions
Stack: scikit-learn, single GPU optional.

## Options
Option A: Logistic regression baseline
- Pros: fast, interpretable
- Cons: lower ceiling

Option B: Gradient boosting
- Pros: higher accuracy
- Cons: more tuning

## Comparison
Option A is best for first MVP.

## Risk Matrix
- Label noise (Likelihood 4, Impact 3)

## Cost and Timeline
- Option A: 2 weeks
- Option B: 4 weeks

## Recommendation
Start with Option A, add Option B in iteration 2.

## MVP Path
Baseline + evaluation + model card.

## Open Questions
- Metric selection.

---

## Viz/EDA Feasibility Example

Doc-ID: FEAS-2026-01-18-VIZ-001
Doc-Type: feasibility
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md

## Summary
- EDA report generator is feasible with current tooling.
- Main risk is data size.
- Recommend a scripted pipeline with caching.

## Assumptions
- Datasets fit in memory after sampling.

## Open Questions
- Final report format requirement.

## Inputs and Assumptions
Stack: pandas, matplotlib.

## Options
Option A: Jupyter-based template
- Pros: flexible
- Cons: less automated

Option B: Scripted report generator
- Pros: repeatable
- Cons: more upfront work

## Comparison
Option B provides repeatability with acceptable effort.

## Risk Matrix
- Large dataset memory pressure (Likelihood 3, Impact 3)

## Cost and Timeline
- Option B: 2 weeks

## Recommendation
Build scripted generator and cache tables.

## MVP Path
Tables + 5 core plots.

## Open Questions
- Final plot list.

---

## Lab Automation Feasibility Example

Doc-ID: FEAS-2026-01-18-LAB-001
Doc-Type: feasibility
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md

## Summary
- OT-2 protocol is feasible with current labware.
- Main risk is pipette capacity.
- Recommend a two-step protocol MVP.

## Assumptions
- OT-2 and labware are available.

## Open Questions
- Final sample volume per well.

## Inputs and Assumptions
Hardware: OT-2 with P300 and P20.

## Options
Option A: Single-pass protocol
- Pros: faster
- Cons: risk of volume limits

Option B: Two-step protocol
- Pros: safer volumes
- Cons: longer runtime

## Comparison
Option B reduces volume risks.

## Risk Matrix
- Tip usage overflow (Likelihood 3, Impact 4)

## Cost and Timeline
- Option B: 3 weeks

## Recommendation
Proceed with Option B for MVP.

## MVP Path
Deck plan + protocol + simulation.

## Open Questions
- Confirm volumes.

---

## Scientific Writing Feasibility Example

Doc-ID: FEAS-2026-01-18-WR-001
Doc-Type: feasibility
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md

## Summary
- IMRAD draft is feasible with current sources.
- Main risk is citation gaps.
- Recommend a staged outline + literature table.

## Assumptions
- Access to key papers.

## Open Questions
- Target venue requirements.

## Inputs and Assumptions
Tools: BibTeX manager and markdown.

## Options
Option A: Outline first then sections
- Pros: fast alignment
- Cons: requires early decisions

Option B: Related work first
- Pros: grounded citations
- Cons: slower start

## Comparison
Option A with a short literature table is optimal.

## Risk Matrix
- Citation gaps (Likelihood 4, Impact 3)

## Cost and Timeline
- Option A: 3 weeks

## Recommendation
Start with outline, then literature table.

## MVP Path
Outline + 2 sections draft.

## Open Questions
- Venue constraints.
