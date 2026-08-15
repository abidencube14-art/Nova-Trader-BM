"""
==========================================
Nova Brain
==========================================
"""

from brain.memory import TradingMemory

from brain.reasoning import Reasoning

from decision.decision_engine import DecisionEngine

from models.trading_decision import TradingDecision


class NovaBrain:

    def __init__(self):

        self.memory = TradingMemory()

        self.reason = Reasoning()

        self.engine = DecisionEngine()

    def think(

        self,
        
        symbol,

        trend,

        indicators,

        candle,

        support,

        resistance,

        volatility,

        entry=0

    ):

        decision = self.engine.evaluate(

            symbol=symbol,

            trend=trend,

            indicators=indicators,
           
            candle=candle,

            support=support,

            resistance=resistance,

            volatility=volatility,

            entry=entry

        )

        self.memory.update(

            trend,

            decision["score"],

            decision["confidence"]

        )

        explanation = self.reason.explain(

            trend,

            indicators,

            decision["confidence"]

        )

        return TradingDecision(

            action=decision["action"],

            trend=trend,

            confidence=decision["confidence"],

            score=decision["score"],

            reason=explanation,

            risk=decision["risk"]

        )
