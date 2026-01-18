# Parameter Spec Template

Doc-ID: PARAM-YYYY-MM-DD-###
Doc-Type: params
Owner: <name or team>
Date: YYYY-MM-DD
Version: v1.x
Status: draft | review | final
Source: <input docs or code paths>

## Summary
- 3 to 7 concise bullets

## Assumptions
- List assumptions or write "None"

## Open Questions
- List open questions or write "None"

## Context
Describe the system or module this spec applies to.

## Parameter Table
| name | type | default | range | unit | dependencies | notes |
|---|---|---|---|---|---|---|
| example_param | int | 16 | 1-64 | none | none | baseline |

## Constraint Rules
- example_param must be <= max_items
- If mode=fast, disable expensive_feature

## Preset Profiles
- safe: conservative defaults
- balanced: recommended defaults
- high: performance-optimized defaults

## Validation Notes
- Describe checks or tests used to validate the parameters.
