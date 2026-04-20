def verify_step_result(step: dict, tool_result: dict) -> dict:
    hits = tool_result.get("hits", [])
    phase = step.get("phase", "first_pass")

    if phase == "first_pass":
        return {
            "supported": False,
            "status": "needs_replan",
            "reason": "Initial indicators were weak or generic; stronger evidence required",
        }

    strong_terms = {"schtasks", "hkcu", "run", "appdata", "suspicious.exe"}
    strong_hit = False
    for hit in hits:
        matched = {m.lower() for m in hit.get("matched_keywords", [])}
        if matched & strong_terms:
            strong_hit = True
            break

    if strong_hit:
        return {
            "supported": True,
            "status": "verified",
            "reason": "Stronger persistence indicators found during the verification pass",
        }

    return {
        "supported": False,
        "status": "needs_manual_validation",
        "reason": "Even after replanning, the evidence remains too weak for confirmation",
    }
