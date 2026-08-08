"""
==========================================
Decision Engine
Nova-Trader-BM
==========================================
"""

from signals.engine import SignalEngine
from risk.engine import RiskEngine


class DecisionEngine:

    def __init__(self):

        self.signal_engine = SignalEngine()

        self.risk_engine = RiskEngine()

    def evaluate(

        self,

        trend,

        indicators,

        candle,

        support,

        resistance,

        volatility,

        balance=10,

        entry=0

    ):

        signal = self.signal_engine.generate(

            indicators

        )

        atr = indicators["atr"]

        risk = self.risk_engine.evaluate(

            decision=signal,

            balance=balance,

            entry=entry,

            atr=atr

        )

        return {

            "action": signal.action,

            "score": signal.confidence,

            "confidence": signal.confidence,

            "reason": signal.reason,

            "risk": risk

        }
