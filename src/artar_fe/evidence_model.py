from dataclasses import dataclass, asdict, field
from typing import List


@dataclass
class Finding:
    finding_id: str
    claim: str
    claim_type: str
    confidence: float
    source_tool: str
    source_artifact: str
    offset_or_line: str
    verification_status: str
    supporting_steps: List[str] = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)
