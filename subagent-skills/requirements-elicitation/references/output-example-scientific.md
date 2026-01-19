# Output Examples (Scientific PRD)

## Imaging PRD Example

Doc-ID: PRD-2026-01-18-IM-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Build a DICOM ingestion and QC pipeline.
- Support de-identification and basic QC reporting.
- Target a pilot dataset in 4 weeks.

## Assumptions
- DICOM studies are available on a shared drive.

## Open Questions
- Final list of required DICOM tags for de-id.

## Executive Summary
Implement a pipeline to ingest DICOM studies, remove PHI, and produce QC reports.

## Problem Statement
Manual QC is slow and inconsistent, delaying imaging analysis.

## Goals (SMART)
- Process 500 studies per week with under 2 hours latency.

## Scope / Non-Goals
- Scope: ingestion, de-id, QC report.
- Non-Goals: model training.

## Users and Personas
- Imaging analyst

## User Stories
- As an analyst, I can run de-id and receive a QC report.

## Functional Requirements
- REQ-001: DICOM ingestion with tag validation
  - Acceptance Criteria:
    - [ ] Reject studies with missing required tags

## Non-Functional Requirements
- QC report generation under 10 minutes per study.

## Constraints and Assumptions
- Use pydicom for tag parsing.

## Risks and Open Questions
- Variability in vendor tag usage.

## Metrics and Validation
- QC completion rate and error counts.

## Rollout and Milestones
- Week 1-2: ingestion + de-id
- Week 3-4: QC report

---

## ML PRD Example

Doc-ID: PRD-2026-01-18-ML-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Train a baseline classifier for triage.
- Provide metrics and error analysis.
- Target AUC >= 0.80 on validation.

## Assumptions
- Labels are available and stable.

## Open Questions
- Final metric preference for release gate.

## Executive Summary
Deliver a baseline ML model and evaluation pipeline.

## Problem Statement
No consistent baseline exists for triage automation.

## Goals (SMART)
- Achieve AUC 0.80 in 6 weeks.

## Scope / Non-Goals
- Scope: baseline, evaluation, model card.
- Non-Goals: production deployment.

## Users and Personas
- Data scientist

## User Stories
- As a scientist, I can run training and review metrics.

## Functional Requirements
- REQ-001: Train baseline model
  - Acceptance Criteria:
    - [ ] Metrics table produced with AUC, F1, recall

## Non-Functional Requirements
- Training run must complete within 2 hours.

## Constraints and Assumptions
- Use scikit-learn baseline models.

## Risks and Open Questions
- Class imbalance severity.

## Metrics and Validation
- AUC, F1, recall, calibration error.

## Rollout and Milestones
- Week 1-2: data split + baseline
- Week 3-4: evaluation + error analysis

---

## Viz/EDA PRD Example

Doc-ID: PRD-2026-01-18-VIZ-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Build EDA reports for study datasets.
- Generate standard plots and tables.
- Deliver a reproducible report template.

## Assumptions
- Data is provided as CSV files.

## Open Questions
- Preferred plotting library for final report.

## Executive Summary
Create an automated EDA report generator.

## Problem Statement
Manual EDA is inconsistent across teams.

## Goals (SMART)
- Generate a report in under 10 minutes per dataset.

## Scope / Non-Goals
- Scope: summary stats and plots.
- Non-Goals: model training.

## Users and Personas
- Data analyst

## User Stories
- As an analyst, I can run one command to produce a report.

## Functional Requirements
- REQ-001: Generate summary tables
  - Acceptance Criteria:
    - [ ] Output tables for missingness and distributions

## Non-Functional Requirements
- Report must be reproducible from a script.

## Constraints and Assumptions
- Use matplotlib or seaborn.

## Risks and Open Questions
- Large datasets may exceed memory.

## Metrics and Validation
- Report completion time.

## Rollout and Milestones
- Week 1: template
- Week 2: automation

---

## Lab Automation PRD Example

Doc-ID: PRD-2026-01-18-LAB-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Draft an Opentrons protocol for sample prep.
- Produce a deck plan and simulation report.
- Validate volumes and tip usage.

## Assumptions
- Opentrons OT-2 with standard labware.

## Open Questions
- Final reagent volumes per sample.

## Executive Summary
Automate a sample prep protocol on OT-2.

## Problem Statement
Manual prep is error-prone and slow.

## Goals (SMART)
- Reduce manual prep time by 50 percent.

## Scope / Non-Goals
- Scope: OT-2 protocol and simulation.
- Non-Goals: hardware purchase.

## Users and Personas
- Lab technician

## User Stories
- As a technician, I can run the protocol safely.

## Functional Requirements
- REQ-001: Generate OT-2 protocol
  - Acceptance Criteria:
    - [ ] Simulation passes without errors

## Non-Functional Requirements
- Protocol runtime under 45 minutes.

## Constraints and Assumptions
- Use Protocol API v2.

## Risks and Open Questions
- Labware compatibility.

## Metrics and Validation
- Simulation success rate.

## Rollout and Milestones
- Week 1: deck plan
- Week 2: protocol draft

---

## Scientific Writing PRD Example

Doc-ID: PRD-2026-01-18-WR-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Draft IMRAD outline for a methods paper.
- Produce a literature table with citations.
- Deliver a reviewer checklist.

## Assumptions
- Target venue is a methods journal.

## Open Questions
- Final list of related work sources.

## Executive Summary
Create an IMRAD draft and citation-ready references.

## Problem Statement
The team lacks a consistent writing workflow.

## Goals (SMART)
- Produce a draft in 3 weeks.

## Scope / Non-Goals
- Scope: outline, related work table, draft sections.
- Non-Goals: journal submission.

## Users and Personas
- Research lead

## User Stories
- As a lead, I can review an outline and draft sections.

## Functional Requirements
- REQ-001: IMRAD outline
  - Acceptance Criteria:
    - [ ] Outline aligns with IMRAD structure

## Non-Functional Requirements
- Citations in BibTeX format.

## Constraints and Assumptions
- Use BibTeX for citations.

## Risks and Open Questions
- Citation coverage completeness.

## Metrics and Validation
- Draft completion percent per week.

## Rollout and Milestones
- Week 1: outline
- Week 2: related work table
- Week 3: draft sections
