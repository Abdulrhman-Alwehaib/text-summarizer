from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:
    root_dir: Path
    source_URL_hugging_face: str
    localDataFolder: Path