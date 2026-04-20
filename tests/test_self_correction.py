from pathlib import Path
from artar_fe.orchestrator import run_case


def test_run_case_creates_report_dict(tmp_path: Path):
    case_path = tmp_path / "case.txt"
    case_path.write_text(
        "Startup folder reviewed.`n"
        "Analyst note: possible persistence.`n"
        "HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run suspicious.exe",
        encoding="utf-8",
    )
    report = run_case(case_path, tmp_path / "out")
    assert "findings" in report
