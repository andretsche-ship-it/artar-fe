# Accuracy Report

## Scope
This report covers the current MVP2 demo run of ARTAR-FE using the local repository demo case.

## Demo case result
The current run produced:
- 1 rejected hypothesis
- 1 confirmed finding
- 1 inferred finding requiring manual validation
- 1 visible self-correction sequence

## Expected findings
Expected investigation behavior for the demo case:
- weak first-pass persistence suspicion should not be accepted as confirmed
- a replan step should search for stronger persistence indicators
- a stronger second-pass result should be surfaced
- uncertainty should remain explicit where evidence is not fully closed

## Actual findings
Observed output:
- F-001 rejected: initial persistence hypothesis was too weak to confirm
- F-002 confirmed: suspicious persistence-related indicator detected in the case text
- F-003 inferred: suspicious indicator may be tied to user-level autorun persistence

## False positives
Current known false-positive exposure:
- confirmation is still driven by simplified keyword-based logic
- the confirmed result is suitable for MVP demonstration, but not yet full forensic-grade confirmation

## Missed artifacts
Current known misses:
- no deep artifact parsing yet
- no registry hive parsing
- no scheduled task artifact parsing
- no disk, memory, or timeline-native evidence extraction yet

## Hallucination / overclaim control
The MVP already includes:
- explicit rejection of unsupported first-pass suspicion
- separation between confirmed, inferred, and rejected findings
- visible self-correction in the execution log
- preserved uncertainty instead of collapsing all signals into confirmed output

## Evidence integrity approach
Current MVP approach:
- local demo evidence is read-only input
- no destructive modification path is implemented
- guarded tool routing restricts the current tool surface
- unsupported claims are downgraded instead of silently promoted

## Current limitations
- dataset is intentionally small
- artifact coverage is narrow
- persistence confirmation is simplified
- inferred outputs still require analyst review
- broader Protocol SIFT integration is still ahead of the current MVP stage
