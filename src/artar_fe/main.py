import argparse
import csv
import json
from pathlib import Path
from .orchestrator import run_case


def write_markdown(report: dict, output_dir: Path) -> None:
    md = output_dir / "report.md"
    with md.open("w", encoding="utf-8") as f:
        f.write("# ARTAR-FE Report\n\n")
        f.write(report.get("summary", "") + "\n\n")
        f.write(report.get("narrative", "") + "\n\n")
        f.write("## Findings\n\n")
        for finding in report.get("findings", []):
            f.write(f"- **{finding['finding_id']}** [{finding['claim_type']}] {finding['claim']} ({finding['verification_status']})\n")


def write_csv(report: dict, output_dir: Path) -> None:
    path = output_dir / "findings.csv"
    findings = report.get("findings", [])
    if not findings:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=findings[0].keys())
        writer.writeheader()
        writer.writerows(findings)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-path", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report = run_case(Path(args.case_path), output_dir)
    with (output_dir / "report.json").open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    write_markdown(report, output_dir)
    write_csv(report, output_dir)


if __name__ == "__main__":
    main()
