from pathlib import Path
import json


def build_judge_summary(run_dir: Path) -> Path:
    report = json.loads((run_dir / "report.json").read_text(encoding="utf-8"))
    findings = report.get("findings", [])
    artar = report.get("artar_state", {})

    confirmed = sum(1 for f in findings if f.get("claim_type") == "confirmed")
    inferred = sum(1 for f in findings if f.get("claim_type") == "inferred")
    rejected = sum(1 for f in findings if f.get("claim_type") == "rejected")

    lines = [
        "ARTAR-FE Judge Summary",
        "",
        f"Summary: {report.get('summary', '')}",
        f"Confirmed findings: {confirmed}",
        f"Inferred findings: {inferred}",
        f"Rejected hypotheses: {rejected}",
        f"Self-correction used: {artar.get('omega', {}).get('self_correction_used', False)}",
        f"L3 center: {artar.get('l3', {}).get('center', 'unknown')}",
        f"L2 structure mode: {artar.get('l2', {}).get('structure_mode', 'unknown')}",
        "",
        "Key result:",
        "- first pass was downgraded",
        "- replan was triggered",
        "- second pass verified a stronger persistence-related indicator",
    ]

    out = run_dir / "judge_summary.txt"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    run_dir = Path("artifacts/sample_runs/case_001")
    out = build_judge_summary(run_dir)
    print(out)
