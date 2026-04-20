from artar_fe.guardrails import validate_tool


def test_guardrails_accepts_keyword_scan():
    validate_tool("keyword_scan")
