from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:
    root_dir: Path
    source_URL_hugging_face: str
    localDataFolder: Path


@dataclass(frozen=True)
class DataValidationConfiguration:
    root_dir: Path
    inputData: Path
    STATUS_FILE: str
    REQUIRED_FILES: str