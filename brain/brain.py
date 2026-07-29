"""
==========================================
Nova Brain
==========================================
"""

from brain.memory import TradingMemory

from brain.reasoning import Reasoning

from decision.decision_engine import DecisionEngine


class NovaBrain:

    def __init__(self):

        self.memory = TradingMemory()

        self.reason = Reasoning()

        self.engine = DecisionEngine()

    def think(

        self,

        trend,

        indicators,

        candle,

        support,

        resistance,

        volatility

    ):

        decision = self.engine.evaluate(

            trend,

            indicators,

            candle,

            support,

            resistance,

            volatility

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

        return {

            "decision": trend,

            "score": decision["score"],

            "confidence":

            decision["confidence"],

            "reason":

            explanation

        }
