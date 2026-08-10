"""
==========================================
Backtesting Engine
Nova-Trader-BM
==========================================
"""

from simulator.engine import SimulatorEngine
from strategy.manager import StrategyManager


class Backtester:

    def __init__(self):

        self.strategy = StrategyManager()

        self.simulator = SimulatorEngine()

    def run(self, dataframe):

        results = []

        if dataframe is None or len(dataframe) < 200:

            return results

        for i in range(200, len(dataframe)):

            data = dataframe.iloc[:i + 1]

            signal = self.strategy.analyse(data)

            results.append({

                "index": i,

                "signal": signal

            })

        return results
