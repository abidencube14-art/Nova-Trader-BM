"""
==========================================
Decision Engine
Nova-Trader-BM
==========================================
"""

from decision.scoring import DecisionScore

from decision.confidence import Confidence


class DecisionEngine:

    def evaluate(

        self,

        trend,

        indicators,

        candle,

        support,

        resistance,

        volatility

    ):

        score = DecisionScore()

        if trend != "SIDEWAYS":

            score.add("Trend", 25)

        if indicators["rsi"] > 55 or indicators["rsi"] < 45:

            score.add("Momentum", 20)

        if candle:

            score.add("Candlestick", 20)

        if support:

            score.add("Support", 15)

        if resistance:

            score.add("Resistance", 10)

        if volatility:

            score.add("Volatility", 10)

        confidence = Confidence()

        return {

            "score": score.total(),

            "confidence":

            confidence.level(score.total()),

            "details":

            score.report()

        }
