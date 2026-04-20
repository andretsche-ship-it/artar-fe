def plan_next_step(state: dict) -> dict:
    return {
        "step_id": "S-001",
        "goal": "Search for suspicious startup persistence indicators in the case text",
        "selected_tool": "keyword_scan",
        "tool_args": {"keywords": ["autorun", "startup", "run key", "persistence"]},
        "expected_artifact": "initial_persistence_hits",
    }
