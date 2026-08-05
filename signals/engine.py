"""
==========================================
Signal Engine
Nova-Trader-BM
==========================================
"""

from strategy.manager import StrategyManager
from strategy.filters import trade_allowed


class SignalEngine:

    def __init__(self):

        self.strategy = StrategyManager()

    def generate(self, data):

        indicators = self.strategy.indicators.analyse(data)

        market = self.strategy.analysis.analyse(

            data,

            indicators

        )

        action = self.strategy.analyse(data)

        if not trade_allowed(indicators):

            action = "WAIT"

        return {

            "action": action,

            "market": market,

            "indicators": indicators

        }
