from artar_fe.report_builder import build_report


def test_report_contains_summary_and_findings():
    report = build_report({"case": {"case_path": "demo"}})
    assert "summary" in report
    assert "findings" in report
