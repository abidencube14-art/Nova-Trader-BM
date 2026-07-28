"""
==========================================
Backtesting Engine
Nova-Trader-BM
==========================================
"""

from strategy.manager import StrategyManager


class Backtester:

    def __init__(self):

        self.strategy = StrategyManager()

    def run(self, dataframe):

        results = []

        for i in range(200, len(dataframe)):

            data = dataframe.iloc[: i + 1]

            signal = self.strategy.analyse(data)

            results.append(signal)

        return results
