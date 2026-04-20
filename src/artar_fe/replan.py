def replan_after_verification(state: dict) -> dict:
    return {
        "step_id": "S-002",
        "phase": "replan",
        "goal": "Re-check the evidence for stronger indicators such as schtasks, registry run keys, or startup paths",
        "selected_tool": "keyword_scan",
        "tool_args": {"keywords": ["schtasks", "HKCU", "Run", "Startup", "AppData", "suspicious.exe"]},
        "expected_artifact": "secondary_persistence_hits",
    }
