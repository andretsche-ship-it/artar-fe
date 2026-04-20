from artar_fe.evidence_model import Finding


def test_finding_has_core_fields():
    finding = Finding("F-1", "c", "confirmed", 1.0, "t", "a", "line 1", "verified")
    data = finding.to_dict()
    assert data["finding_id"] == "F-1"
    assert data["verification_status"] == "verified"
