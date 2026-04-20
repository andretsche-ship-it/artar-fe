from typing import Any, Dict


def build_omega(state: Dict[str, Any]) -> Dict[str, Any]:
    case = state.get("case", {})
    text = case.get("text", "")
    lines = case.get("lines", [])

    return {
        "case_length": len(text),
        "line_count": len(lines),
        "contains_startup_language": "startup" in text.lower(),
        "contains_registry_language": "hkcu" in text.lower() or "run" in text.lower(),
        "contains_task_language": "schtasks" in text.lower() or "scheduled task" in text.lower(),
        "history_count": len(state.get("history", [])),
        "self_correction_used": state.get("self_correction_used", False),
    }


def derive_reactivity(state: Dict[str, Any]) -> Dict[str, Any]:
    history = state.get("history", [])
    first_verification = None
    latest_verification = None

    if history:
        first_verification = history[0].get("verification", {})
        latest_verification = history[-1].get("verification", {})

    return {
        "first_supported": bool(first_verification.get("supported")) if first_verification else False,
        "latest_supported": bool(latest_verification.get("supported")) if latest_verification else False,
        "needs_replan": any(
            item.get("verification", {}).get("status") == "needs_replan"
            for item in history
        ),
        "history_depth": len(history),
    }


def locate_l3(state: Dict[str, Any]) -> Dict[str, Any]:
    reactivity = state.get("reactivity", {})
    omega = state.get("omega", {})

    if reactivity.get("needs_replan") and reactivity.get("latest_supported"):
        center = "verified_persistence_center"
    elif reactivity.get("needs_replan"):
        center = "unstable_persistence_probe"
    elif omega.get("contains_registry_language") or omega.get("contains_task_language"):
        center = "direct_persistence_signal_center"
    else:
        center = "weak_signal_probe"

    return {
        "center": center,
        "confidence_mode": "stabilized" if reactivity.get("latest_supported") else "exploratory",
    }


def derive_l2(state: Dict[str, Any]) -> Dict[str, Any]:
    l3 = state.get("l3", {})
    return {
        "structure_mode": "two_pass_verification"
        if l3.get("center") == "verified_persistence_center"
        else "single_pass_probe",
        "verification_required": True,
    }


def build_l1(state: Dict[str, Any]) -> Dict[str, Any]:
    omega = state.get("omega", {})
    l2 = state.get("l2", {})
    return {
        "ground_truth_window": {
            "startup_language": omega.get("contains_startup_language", False),
            "registry_language": omega.get("contains_registry_language", False),
            "task_language": omega.get("contains_task_language", False),
        },
        "execution_shape": l2.get("structure_mode", "unknown"),
    }


def apply_artar_pipeline(state: Dict[str, Any]) -> None:
    state["omega"] = build_omega(state)
    state["reactivity"] = derive_reactivity(state)
    state["l3"] = locate_l3(state)
    state["l2"] = derive_l2(state)
    state["l1"] = build_l1(state)
