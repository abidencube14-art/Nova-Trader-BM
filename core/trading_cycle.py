"""
==========================================
Trading Cycle
Nova-Trader-BM
==========================================
"""

from brain.brain import NovaBrain


class TradingCycle:

    def __init__(self):

        self.brain = NovaBrain()

    def execute(

        self,

        indicators,

        balance,

        entry,

        atr

    ):

        decision = self.brain.think(

            indicators,

            balance,

            entry,

            atr

        )

        return decision
