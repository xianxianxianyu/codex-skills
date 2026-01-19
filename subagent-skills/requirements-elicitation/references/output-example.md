# Output Example (PRD)

Doc-ID: PRD-2026-01-18-001
Doc-Type: prd
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: User prompt
Activated-Skills: requirements-elicitation

## Summary
- Define MVP scope for a customer feedback portal.
- Deliver basic auth, submission, and admin triage.
- Target launch in 6 weeks with a small pilot.

## Assumptions
- Team has an existing auth service.

## Open Questions
- Which CRM should receive escalated tickets?

## Executive Summary
Build a lightweight feedback portal for customers to submit issues and track status.

## Problem Statement
Support tickets are fragmented across email and chat, increasing response time.

## Goals (SMART)
- Reduce average response time from 3 days to 1 day in 8 weeks.

## Scope / Non-Goals
- Scope: feedback submission, status tracking, admin triage.
- Non-Goals: full CRM replacement.

## Users and Personas
- Customer support agent
- Customer administrator

## User Stories
- As a customer admin, I can submit a ticket with attachments.

## Functional Requirements
- REQ-001: Ticket submission form
  - Acceptance Criteria:
    - [ ] Users can submit title, description, and attachment.

## Non-Functional Requirements
- 99.5 percent uptime monthly.

## Constraints and Assumptions
- Use existing auth service.

## Risks and Open Questions
- CRM integration choice pending.

## Metrics and Validation
- Response time tracked weekly.

## Rollout and Milestones
- Week 1-2: MVP build.

