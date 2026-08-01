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

    def decide(

        self,

        indicators,

        balance,

        entry,

        atr

    ):

        signal = self.signal_engine.generate(

            indicators

        )

        risk = self.risk_engine.evaluate(

            signal,

            balance,

            entry,

            atr

        )

        return {

            "signal": signal,

            "risk": risk

        }
