# Output Example (Implementation)

Doc-ID: IMPL-2026-01-18-001
Doc-Type: implementation
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: docs/prd.md, docs/feasibility.md
Activated-Skills: code-agent-core

## Summary
- Added ticket submission API.
- Updated database schema for attachments.
- Added basic tests for validation.

## Assumptions
- Existing auth middleware remains unchanged.

## Open Questions
- Should attachments be stored in S3 or local disk?

## Plan Summary
- Add API route and validation.
- Update schema and migrations.
- Add tests for happy path and validation errors.

## Changes (by file/module)
- src/routes/tickets.ts: new POST endpoint
- src/db/migrations/20260118_add_attachments.sql: new table

## Tests Run
- npm test -- tickets

## Risks and Rollback Notes
- Migration is additive; rollback by dropping attachments table.

## Follow-ups
- Add pagination to ticket list.

