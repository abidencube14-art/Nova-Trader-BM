"""
==========================================
Analysis Engine
Nova-Trader-BM
==========================================
"""

from analysis.trend import TrendAnalysis
from analysis.support_resistance import SupportResistance
from analysis.volatility import VolatilityAnalysis
from analysis.market_structure import MarketStructure
from analysis.trend_strength import TrendStrength

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

    structure = self.structure.trend(

        candles

    )

    strength = self.strength.calculate(

        indicators

    )

    return {

        "trend": trend,

        "structure": structure,

        "strength": strength,

        "support": support,

        "resistance": resistance,

        "volatility": volatility

    }
