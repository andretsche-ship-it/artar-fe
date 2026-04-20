# ARTAR-FE

ARTAR-FE is a self-correcting, evidence-safe forensic reasoning agent scaffold for Protocol SIFT.

## Current status
This package now includes a minimal runnable MVP with:
- guarded keyword-scan tool routing
- two-pass planning and re-planning
- visible self-correction path
- confirmed / inferred / rejected findings
- report.json, report.md, findings.csv, execution_log.jsonl outputs

## Demo run
```bash
python -m artar_fe.main --case-path demo_case/case_001.txt --output-dir artifacts/sample_runs/case_001
```
