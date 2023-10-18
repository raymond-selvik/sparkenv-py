from dataclasses import dataclass
from pathlib import Path

@dataclass
class SparkVersion:
    name: str
    install_path: Path
