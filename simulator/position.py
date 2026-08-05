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
