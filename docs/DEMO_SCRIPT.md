# Demo Script

## Goal
Show ARTAR-FE as a self-correcting, evidence-safe forensic reasoning agent for Protocol SIFT.

## Demo flow
1. Show the repository briefly
   - README
   - docs
   - src
   - demo_case

2. Run the local demo case
   - set PYTHONPATH
   - execute the demo command
   - generate report and execution outputs

3. Explain the first pass
   - initial persistence-oriented scan runs
   - result is treated as too weak
   - verification marks it as needing replan

4. Explain self-correction
   - the second step searches for stronger persistence indicators
   - the execution log marks this as self-correction

5. Show final outputs
   - report.md
   - report.json
   - findings.csv
   - execution_log.jsonl

6. Highlight result classes
   - rejected finding
   - confirmed finding
   - inferred finding requiring manual validation

7. Highlight ARTAR-style internal state
   - omega
   - reactivity
   - l3
   - l2
   - l1

## Key message
ARTAR-FE does not maximize unconstrained automation.
It prioritizes:
- evidence safety
- traceability
- explicit uncertainty
- structured self-correction
- disciplined forensic reasoning
