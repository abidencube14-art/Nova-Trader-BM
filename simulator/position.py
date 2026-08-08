"""
==========================================
Simulator Position
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass


@dataclass
class Position:

    symbol: str

    action: str

    lot: float

    entry: float

    sl: float

    tp: float

    status: str = "OPEN"

    exit_price: float | None = None

    profit_loss: float = 0.0

    close_reason: str | None = None
