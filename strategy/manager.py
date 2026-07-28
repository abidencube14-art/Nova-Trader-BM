"""
==========================================
Strategy Manager
Nova-Trader-BM
==========================================
"""

from strategy.entries import entry_signal


class StrategyManager:

    def __init__(self):

        self.name = "EMA-RSI-MACD"

    def analyse(self, data):

        return entry_signal(data)

    def current_strategy(self):

        return self.name
