from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import Dict, List

_config_path = f"{Path(__file__).resolve().parent}/config.json"

@dataclass
class ParkonConfiguration:
    url: str
    email: str
    plates: Dict[str, str]
    cantons: List[str]
    durations: List[str]

    def save_to_json(self):
        with open(_config_path, "w") as f:
            f.write(json.dumps(asdict(self), indent=4))
    
    @classmethod
    def load_from_json(cls) -> "ParkonConfiguration":
        with open(_config_path) as f:
            return cls(**json.loads(f.read()))
    
conf = ParkonConfiguration.load_from_json()
