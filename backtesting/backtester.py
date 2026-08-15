"""
==========================================
Backtesting Engine
Nova-Trader-BM
==========================================
"""

from indicators.manager import IndicatorManager
from analysis.engine import AnalysisEngine
from brain.brain import NovaBrain
from simulator.engine import SimulatorEngine


class Backtester:

    def __init__(self):

        self.indicators = IndicatorManager()

        self.analysis = AnalysisEngine()

        self.brain = NovaBrain()

        self.simulator = SimulatorEngine()

    def run(self, dataframe, symbol="BACKTEST"):

        if dataframe is None or len(dataframe) < 200:

            return []

        results = []

        open_trade = None

        for i in range(200, len(dataframe)):

            candles = dataframe.iloc[:i + 1]

            indicators = self.indicators.analyse(
                candles
            )

            latest = candles.iloc[-1]

            market = self.analysis.analyse(
                candles,
                indicators
            )

            if open_trade is not None:

                open_trade = self.simulator.check_exit(

                    open_trade,

                    high=latest["high"],

                    low=latest["low"]

                )

                if open_trade.status == "CLOSED":

                    open_trade = None

            if open_trade is None:

                decision = self.brain.think(

                    trend=market["trend"],

                    indicators=indicators,

                    candle=latest,

                    support=market["support"],

                    resistance=market["resistance"],

                    volatility=market["volatility"],

                    entry=latest["close"],

                    symbol=symbol

                )

                trade = self.simulator.execute(

                    symbol=symbol,

                    decision=decision,

                    risk=decision.risk,

                    entry=latest["close"]

                )

                if trade is not None:

                    open_trade = trade

            results.append({

                "index": i,

                "balance":
                    self.simulator.account.get_balance(),

                "trade": open_trade

            })

        return results
