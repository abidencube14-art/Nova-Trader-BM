"""
==========================================
Strategy Manager
Nova-Trader-BM
==========================================
"""

from indicators.manager import IndicatorManager

from strategy.entries import entry_signal


class StrategyManager:

    def __init__(self):

        self.indicators = IndicatorManager()

        self.name = "EMA-RSI-MACD"

    def analyse(self, data):

        values = self.indicators.analyse(data)

        return entry_signal(values)

    def current_strategy(self):

        return self.name
