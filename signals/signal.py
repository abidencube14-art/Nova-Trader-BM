"""
==========================================
Trading Signal
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass


@dataclass
class TradingSignal:

    action: str

    score: int

    confidence: int

    reason: str
