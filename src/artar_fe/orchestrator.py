from pathlib import Path
from .artar_core import apply_artar_pipeline
from .case_loader import load_case
from .logger import append_log
from .planner import plan_next_step
from .replan import replan_after_verification
from .report_builder import build_report
from .state_store import init_state
from .tool_router import execute_tool
from .verifier import verify_step_result


def run_case(case_path: Path, output_dir: Path) -> dict:
    state = init_state()
    state["case"] = load_case(case_path)
    log_path = output_dir / "execution_log.jsonl"

    apply_artar_pipeline(state)

    first_step = plan_next_step(state)
    first_result = execute_tool(first_step, state)
    first_verification = verify_step_result(first_step, first_result)
    state["first_result"] = first_result
    state["history"].append({"step": first_step, "result": first_result, "verification": first_verification})
    apply_artar_pipeline(state)

    append_log(
        log_path,
        {
            "phase": "first_pass",
            "step_id": first_step["step_id"],
            "goal": first_step["goal"],
            "tool": first_step["selected_tool"],
            "tool_args": first_step["tool_args"],
            "result_summary": first_result["result_summary"],
            "hit_count": first_result["hit_count"],
            "verification": first_verification,
            "artar": {
                "omega": state["omega"],
                "reactivity": state["reactivity"],
                "l3": state["l3"],
                "l2": state["l2"],
                "l1": state["l1"],
            },
        },
    )

    if not first_verification["supported"]:
        second_step = replan_after_verification(state)
        second_result = execute_tool(second_step, state)
        second_verification = verify_step_result(second_step, second_result)
        state["second_result"] = second_result
        state["self_correction_used"] = True
        state["history"].append({"step": second_step, "result": second_result, "verification": second_verification})
        apply_artar_pipeline(state)

        append_log(
            log_path,
            {
                "phase": "replan",
                "step_id": second_step["step_id"],
                "goal": second_step["goal"],
                "tool": second_step["selected_tool"],
                "tool_args": second_step["tool_args"],
                "result_summary": second_result["result_summary"],
                "hit_count": second_result["hit_count"],
                "verification": second_verification,
                "self_correction": True,
                "artar": {
                    "omega": state["omega"],
                    "reactivity": state["reactivity"],
                    "l3": state["l3"],
                    "l2": state["l2"],
                    "l1": state["l1"],
                },
            },
        )

    report = build_report(state)
    report["artar_state"] = {
        "omega": state["omega"],
        "reactivity": state["reactivity"],
        "l3": state["l3"],
        "l2": state["l2"],
        "l1": state["l1"],
    }
    return report
