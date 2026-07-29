"""
==========================================
Trading Memory
Nova-Trader-BM
==========================================
"""


class TradingMemory:

    def __init__(self):

        self.last_signal = None

        self.last_score = 0

        self.last_confidence = ""

        self.last_trade = None

    def update(

        self,

        signal,

        score,

        confidence

    ):

        self.last_signal = signal

        self.last_score = score

        self.last_confidence = confidence

    def state(self):

        return {

            "signal": self.last_signal,

            "score": self.last_score,

            "confidence": self.last_confidence

        }
