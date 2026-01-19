# Output Example (Parameters)

Doc-ID: PARAM-2026-01-18-001
Doc-Type: params
Owner: Example
Date: 2026-01-18
Version: v1.0
Status: draft
Source: src/config.ts
Activated-Skills: parameter-sanity

## Summary
- Normalized defaults for batch processing.
- Defined safe, balanced, and high presets.
- Added constraint rules for memory usage.

## Assumptions
- 16 GB RAM on the target machine.

## Open Questions
- Confirm maximum input size.

## Context
Batch processing module for file ingestion.

## Parameter Table
| name | type | default | range | unit | dependencies | notes |
|---|---|---|---|---|---|---|
| batch_size | int | 32 | 1-128 | items | none | scale with memory |
| timeout_sec | int | 60 | 10-300 | seconds | batch_size | increase with batch |
| max_file_mb | int | 50 | 1-200 | MB | none | input cap |
| enable_cache | bool | true | true/false | none | none | reduce reprocessing |

## Constraint Rules
- batch_size <= 2 * cpu_cores
- If max_file_mb > 100, set timeout_sec >= 120

## Preset Profiles
- safe: batch_size=16, timeout_sec=60, max_file_mb=25
- balanced: batch_size=32, timeout_sec=90, max_file_mb=50
- high: batch_size=64, timeout_sec=150, max_file_mb=100

## Validation Notes
- Checked memory usage with a 1k file sample.
