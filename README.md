# ARTAR-FE

ARTAR-FE is a self-correcting, evidence-safe forensic reasoning agent for Protocol SIFT.

## What it does
ARTAR-FE runs a guarded forensic investigation flow with:
- structured step planning
- guarded tool routing
- explicit verification
- visible self-correction
- separated confirmed / inferred / rejected findings
- structured execution logs
- internal ARTAR-style state layers:
  - omega
  - reactivity
  - l3
  - l2
  - l1

## Current MVP behavior
The current demo case shows:
- 1 rejected hypothesis
- 1 confirmed finding
- 1 inferred finding requiring manual validation
- 1 visible self-correction sequence

## Repository structure
- `src/artar_fe` - core implementation
- `demo_case` - local demo evidence
- `artifacts/sample_runs/case_001` - generated outputs
- `tests` - local tests
- `docs` - submission documentation scaffolding

## Local run
### Windows PowerShell
```powershell
$env:PYTHONPATH = ".\src"
python -m src.artar_fe.main --case-path ".\demo_case\case_001.txt" --output-dir ".\artifacts\sample_runs\case_001"
```

## Generated outputs
After the demo run, the following files are produced:
- `artifacts/sample_runs/case_001/report.json`
- `artifacts/sample_runs/case_001/report.md`
- `artifacts/sample_runs/case_001/findings.csv`
- `artifacts/sample_runs/case_001/execution_log.jsonl`

## Test run
```powershell
$env:PYTHONPATH = ".\src"
python -m pytest .\tests -q
```

## Current limitations
- MVP coverage is intentionally narrow
- current tooling is demo-focused
- persistence confirmation is still simplified
- inferred findings still require analyst review

## License
MIT
