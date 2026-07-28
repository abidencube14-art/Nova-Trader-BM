"""
==========================================
Trade Model
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass


@dataclass

class Trade:

    symbol: str

    direction: str

    entry: float

    stop_loss: float

    take_profit: float

    lot: float

    status: str = "OPEN"
