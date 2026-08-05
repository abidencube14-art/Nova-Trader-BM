"""
==========================================
Master Trading Loop
Nova-Trader-BM
==========================================
"""

from market_data.candles import CandleFeed
from indicators.manager import IndicatorManager
from brain.brain import NovaBrain
from simulator.engine import SimulatorEngine
from analysis.engine import AnalysisEngine

class MasterTradingLoop:

    def __init__(self):

        self.market = CandleFeed()

        self.indicators = IndicatorManager()

        self.analysis = AnalysisEngine()

        self.brain = NovaBrain()

        self.simulator = SimulatorEngine()

    def run(

        self,

        symbol,

        timeframe

    ):

        print(

            f"Starting trading loop for {symbol}"

        )

        candles = self.market.latest(

            symbol,

            timeframe,

            200

        )

        if candles is None or len(candles) == 0:

            print(

                "No candle data."

            )

            return

        analysis = self.indicators.analyse(

            candles

        )

        latest = candles.iloc[-1]

        market = self.analysis.analyse(

    candles,

    analysis

)

decision = self.brain.think(

    trade = self.simulator.execute(

    symbol=symbol,

    decision=decision,

    risk=decision.risk,

    entry=latest["close"]

    )

    trend=market["trend"],

    indicators=analysis,

    candle=latest,

    support=market["support"],

    resistance=market["resistance"],

    volatility=market["volatility"]

)
        print()

print("========== TRADE DECISION ==========")

print(decision)

print()

print("========== EXECUTION ==========")

print(trade)
