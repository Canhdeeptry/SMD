from pathlib import Path
from typing import Any, Optional
import yaml


class YAMLParser:
    def __init__(self, path: Path):
        self.path = path

    def read(self) -> dict[str, Any]:
        with self.path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)

    def write(self, data: dict[str, Any]):
        with self.path.open("w", encoding="utf-8") as f:
            f.write(yaml.dump(data))

    @staticmethod
    def ensure_list(key: str, data: dict[str, Any]) -> list[Any]:
        """Grabs the value of a key in a dict,
        and if it's not a list, make it an empty list"""
        val: Optional[list[Any]] = data.setdefault(key, [])
        if not isinstance(val, list):
            val = []
            data[key] = val
        return val
