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

    confidence: int

    reason: str
