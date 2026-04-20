from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    case_path: Path
    output_dir: Path
