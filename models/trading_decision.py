"""
==========================================
Trading Decision Model
Nova-Trader-BM
==========================================
"""

from dataclasses import dataclass


@dataclass
class TradingDecision:

    action: str

    trend: str

    confidence: int

    score: int

    reason: str

    risk: dict | None = None
