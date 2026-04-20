def build_narrative(state: dict) -> str:
    report = state.get("report_context", {})
    confirmed = report.get("confirmed_count", 0)
    inferred = report.get("inferred_count", 0)
    rejected = report.get("rejected_count", 0)

    ending = (
        "The first pass was downgraded because the evidence was too weak, "
        "and the second pass produced an inferred persistence indicator that still requires analyst validation."
        if confirmed == 0
        else
        "The first pass was downgraded because the evidence was too weak, "
        "then a second pass produced stronger persistence-related evidence."
    )

    return (
        "ARTAR-FE executed a guarded investigation flow. "
        f"Confirmed findings: {confirmed}. "
        f"Inferred findings: {inferred}. "
        f"Rejected hypotheses: {rejected}. "
        f"{ending}"
    )
