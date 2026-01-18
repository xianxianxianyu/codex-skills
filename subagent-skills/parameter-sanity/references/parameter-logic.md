# Parameter Logic Guide

## Dependency Patterns

- Upper bound: param_a <= param_b
- Conditional enable: if mode=fast then disable slow_feature
- Coupled scaling: if batch_size increases, adjust timeout

## Default Strategy

- Prefer conservative defaults that work on minimal hardware.
- Only raise defaults when the environment is confirmed.
- Avoid multiple extreme values at the same time.

## Common Failure Modes

- Incompatible flags enabled together
- Defaults too large for memory constraints
- Missing units or mismatched units
- Hidden dependencies not documented
