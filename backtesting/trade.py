"""
==========================================
Backtest Trade
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass


@dataclass
class BacktestTrade:

    symbol: str

    action: str

    entry: float

    exit: float

    profit: float
