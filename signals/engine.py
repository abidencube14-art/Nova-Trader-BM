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

        self.signal_count = 0

    def generate(self, indicators):

        score, direction, reasons = self.rules.evaluate(
            indicators
        )

        confidence = self.confidence.calculate(
            score,
            4
        )

        if direction == "BUY" and confidence >= 75:

            action = "BUY"

        elif direction == "SELL" and confidence >= 75:

            action = "SELL"

        else:

            action = "WAIT"

        # ----------------------------------
        # Diagnostic output
        # ----------------------------------

        self.signal_count += 1

        if action != "WAIT" and self.signal_count <= 10:

            print()
            print("-----------------------------------")
            print("NOVA SIGNAL DIAGNOSTIC")
            print("-----------------------------------")

            print(
                f"EMA20   : {indicators['ema20']}"
            )

            print(
                f"EMA50   : {indicators['ema50']}"
            )

            print(
                f"EMA200  : {indicators['ema200']}"
            )

            print(
                f"RSI     : {indicators['rsi']:.2f}"
            )

            print(
                f"MACD    : {indicators['macd']}"
            )

            print(
                f"Signal  : {indicators['signal']}"
            )

            print(
                f"Histogram: {indicators['histogram']}"
            )

            print()

            print(
                f"Direction : {direction}"
            )

            print(
                f"Score     : {score}/4"
            )

            print(
                f"Confidence: {confidence}%"
            )

            print(
                f"Action    : {action}"
            )

            print(
                "Reasons:"
            )

            for reason in reasons:

                print(
                    f"  - {reason}"
                )

            print("-----------------------------------")

        return TradingSignal(

            action=action,

            score=score,

            confidence=confidence,

            reason=", ".join(reasons)

                 )
