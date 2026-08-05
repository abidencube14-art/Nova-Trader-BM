"""
==========================================
Simulator Position
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Position:

    symbol: str

    action: str

    lot: float

    entry: float

    sl: float

    tp: float

    status: str = "OPEN"

    profit: float = 0.0

    opened_at: datetime | None = None

    closed_at: datetime | None = None
