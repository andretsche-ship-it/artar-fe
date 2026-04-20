ALLOWED_TOOLS = {"keyword_scan"}
FORBIDDEN_PATTERNS = {"rm ", "del ", "format ", "shutdown ", "powershell -enc"}


def validate_tool(tool_name: str) -> None:
    if tool_name not in ALLOWED_TOOLS:
        raise ValueError(f"Tool not allowed: {tool_name}")


def validate_text_safety(text: str) -> None:
    lower = text.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in lower:
            raise ValueError(f"Forbidden content detected: {pattern}")
