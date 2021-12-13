from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    name: str
    age: int
    id: Optional[str] = None
