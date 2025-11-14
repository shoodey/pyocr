from dataclasses import dataclass, field
from enum import Enum

class DatasetType(Enum):
    FAST = "fast"
    BEST = "best"
    LEGACY = "legacy"

@dataclass
class Config:
    dataset_type: DatasetType = DatasetType.BEST
    debug: bool = False
    timeout: int = 10
    languages: list[str] = field(default_factory=lambda: ["eng"])
    
    @property
    def datasets(self) -> str:
        suffix = f"_{self.dataset_type.value}"
        return "+".join([f"{lang}{suffix}" for lang in self.languages])

config = Config()