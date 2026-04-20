# Dataset Documentation

## Dataset used in MVP2
Current MVP2 uses a small local demo evidence file included directly in the repository:

- `demo_case/case_001.txt`

## Dataset purpose
This demo case exists to validate and demonstrate:
- guarded two-pass forensic reasoning
- explicit downgrade of weak initial evidence
- a visible replan / self-correction step
- a stronger second-pass persistence-oriented result
- reproducible local execution for judges

## Current evidence signals inside the demo case
The included case text contains:
- startup-related language
- a weak persistence suspicion note
- HKCU Run registry wording
- suspicious.exe wording
- scheduled task / schtasks wording

## Expected recoverable outputs
The current MVP is expected to recover:
- one rejected first-pass hypothesis
- one confirmed persistence-related finding after replan
- one inferred persistence-related finding still requiring manual validation

## Why this dataset is used
This dataset is intentionally:
- small
- transparent
- reproducible
- easy to inspect manually
- suitable for demonstrating self-correction behavior in a controlled way

## Current limitations
This dataset is not intended to represent:
- full-scale incident response data
- complete registry artifacts
- full forensic disk images
- memory analysis
- broad artifact coverage across many evidence types

It is an MVP validation dataset for controlled competition demonstration.
