# Security Guardrails

## Current MVP2 guardrail model

ARTAR-FE currently enforces a narrow, controlled investigation surface for the demo flow.

## Tool allowlist
The current MVP only permits explicitly allowed tools through guarded routing.

Current allowed tool set:
- `keyword_scan`

Any tool outside the allowlist is rejected.

## Destructive action prevention
The current MVP is designed around read-only local demo evidence.
No destructive evidence mutation path is implemented.

In addition, text safety checks currently reject destructive patterns such as:
- `rm `
- `del `
- `format `
- `shutdown `
- `powershell -enc`

## Unsupported-claim control
ARTAR-FE does not treat the first weak persistence suspicion as confirmed.
Instead:
- weak evidence is downgraded
- verification can force a replan step
- unsupported claims remain rejected or inferred
- uncertainty is preserved in the final report

## Evidence linkage
Each finding in the output includes structured evidence context such as:
- finding id
- claim type
- source tool
- source artifact
- verification status
- supporting steps
- notes

## Self-correction visibility
The execution log records:
- first pass result
- verification downgrade
- replan step
- second-pass verification
- self-correction marker

## Current limitation
This guardrail model is still MVP-stage.
It is intentionally narrow and focused on:
- controlled demo execution
- transparent output classes
- reduced overclaim risk
- visible evidence-aware re-evaluation
