"""
==========================================
Analysis Engine
Nova-Trader-BM
==========================================
"""

from analysis.trend import TrendAnalysis
from analysis.support_resistance import SupportResistance
from analysis.volatility import VolatilityAnalysis


class AnalysisEngine:

    def __init__(self):

        self.trend = TrendAnalysis()

        self.sr = SupportResistance()

        self.volatility = VolatilityAnalysis()

    def analyse(self, candles, indicators):

        trend = self.trend.detect(indicators)

        support, resistance = self.sr.calculate(candles)

        volatility = self.volatility.classify(

            indicators["atr"]

        )

        return {

            "trend": trend,

            "support": support,

            "resistance": resistance,

            "volatility": volatility

        }
