"""
==========================================
Strategy Manager
Nova-Trader-BM
==========================================
"""

from indicators.manager import IndicatorManager

from strategy.entries import entry_signal

from analysis.engine import AnalysisEngine

class StrategyManager:

    def __init__(self):

        self.indicators = IndicatorManager()

        self.name = "EMA-RSI-MACD"

        self.analysis = AnalysisEngine()

    def analyse(self, data):

        values = self.indicators.analyse(data)

market = self.analysis.analyse(

    data,

    values

)

return entry_signal(

    values,

    market

)
    def current_strategy(self):

        return self.name
