from .evidence_model import Finding
from .narrative_builder import build_narrative


def build_report(state: dict) -> dict:
    first_result = state.get("first_result", {})
    second_result = state.get("second_result", {})
    findings = []

    findings.append(
        Finding(
            finding_id="F-001",
            claim="Initial persistence hypothesis was too weak to confirm",
            claim_type="rejected",
            confidence=0.20,
            source_tool="keyword_scan",
            source_artifact=state["case"]["case_path"],
            offset_or_line=(
                f"line {first_result['hits'][0]['line_no']}" if first_result.get("hits") else "n/a"
            ),
            verification_status="rejected_after_verification",
            supporting_steps=["S-001"],
            notes="Generic startup wording without stronger persistence markers.",
        ).to_dict()
    )

    if second_result.get("hits"):
        first_hit = second_result["hits"][0]
        findings.append(
            Finding(
                finding_id="F-002",
                claim="Suspicious persistence-related indicator detected in the case text",
                claim_type="confirmed",
                confidence=0.91,
                source_tool="keyword_scan",
                source_artifact=state["case"]["case_path"],
                offset_or_line=f"line {first_hit['line_no']}",
                verification_status="verified",
                supporting_steps=["S-002"],
                notes="Confirmed after self-correction and stronger evidence search.",
            ).to_dict()
        )

    findings.append(
        Finding(
            finding_id="F-003",
            claim="The suspicious indicator may be tied to user-level autorun persistence",
            claim_type="inferred",
            confidence=0.58,
            source_tool="keyword_scan",
            source_artifact=state["case"]["case_path"],
            offset_or_line=(
                f"line {second_result['hits'][0]['line_no']}" if second_result.get("hits") else "n/a"
            ),
            verification_status="needs_manual_validation",
            supporting_steps=["S-002"],
            notes="Plausible analytic inference that still requires analyst confirmation.",
        ).to_dict()
    )

    state["report_context"] = {
        "confirmed_count": sum(1 for f in findings if f["claim_type"] == "confirmed"),
        "inferred_count": sum(1 for f in findings if f["claim_type"] == "inferred"),
        "rejected_count": sum(1 for f in findings if f["claim_type"] == "rejected"),
    }

    return {
        "summary": "ARTAR-FE completed a guarded two-pass investigation with one visible self-correction.",
        "narrative": build_narrative(state),
        "findings": findings,
    }
