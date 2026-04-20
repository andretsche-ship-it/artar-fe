from .guardrails import validate_tool, validate_text_safety


def execute_tool(step: dict, state: dict) -> dict:
    tool_name = step["selected_tool"]
    validate_tool(tool_name)
    raw_text = state.get("case", {}).get("raw_text", "")
    validate_text_safety(raw_text)
    keywords = step.get("tool_args", {}).get("keywords", [])
    lines = state.get("case", {}).get("lines", [])

    hits = []
    for idx, line in enumerate(lines, start=1):
        lower = line.lower()
        matched = [kw for kw in keywords if kw.lower() in lower]
        if matched:
            hits.append(
                {
                    "line_no": idx,
                    "line": line,
                    "matched_keywords": matched,
                }
            )

    return {
        "tool": tool_name,
        "ok": True,
        "result_summary": f"Found {len(hits)} matching lines",
        "artifact_ref": state.get("case", {}).get("case_path", "unknown"),
        "hits": hits,
        "hit_count": len(hits),
    }
