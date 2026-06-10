from dataclasses import dataclass
from typing import Optional

@dataclass
class TokenInfo:
    id: int
    rank: Optional[int]
    name: str
    symbol: str
    slug: str
    status: int
    is_active: Optional[int] = None
    first_historical_data: Optional[int] = None  # unix timestamp
    last_historical_data: Optional[int] = None  # unix timestamp
    platform: Optional[str] = None
