from pathlib import Path


def load_case(case_path: Path) -> dict:
    text = case_path.read_text(encoding="utf-8")
    return {
        "case_path": str(case_path),
        "case_name": case_path.name,
        "text": text,
        "raw_text": text,
        "lines": text.splitlines(),
        "status": "loaded",
    }
