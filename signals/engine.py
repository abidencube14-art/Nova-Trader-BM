"""
==========================================
Signal Engine
Nova-Trader-BM
==========================================
"""

from signals.rules import TradingRules
from signals.confidence import ConfidenceCalculator
from signals.signal import TradingSignal


class SignalEngine:

    def __init__(self):

        self.rules = TradingRules()

        self.confidence = ConfidenceCalculator()

    def generate(self, indicators):

        score, reasons = self.rules.evaluate(
            indicators
        )

        confidence = self.confidence.calculate(
            score,
            4
        )

        rsi = indicators["rsi"]

        # ----------------------------------
        # RSI safety filters
        # ----------------------------------

        if rsi > 70:

            action = "WAIT"

            confidence = 0

            reasons.append(
                "BUY blocked: RSI above 70"
            )

        elif rsi < 30:

            action = "WAIT"

            confidence = 0

            reasons.append(
                "SELL blocked: RSI below 30"
            )

        elif confidence >= 75:

            action = "BUY"

        elif confidence <= 25:

            action = "SELL"

        else:

            action = "WAIT"

        return TradingSignal(

            action=action,

            confidence=confidence,

            reason=", ".join(reasons)

        )
