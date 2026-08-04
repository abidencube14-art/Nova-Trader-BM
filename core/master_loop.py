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


class MasterTradingLoop:

    def __init__(self):

        self.market = CandleFeed()

        self.indicators = IndicatorManager()

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

        decision = self.brain.think(

            trend="UNKNOWN",

            indicators=analysis,

            candle=latest,

            support=None,

            resistance=None,

            volatility=analysis["atr"]

        )

        print(decision)
