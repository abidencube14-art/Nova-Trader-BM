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

    def run(self, dataframe):

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

            # ----------------------------------
            # Check existing trade
            # ----------------------------------

            if open_trade is not None:

                open_trade = self.simulator.check_exit(

                    open_trade,

                    high=latest["high"],

                    low=latest["low"]

                )

                if open_trade.status == "CLOSED":

                    open_trade = None

            # ----------------------------------
            # Find new trade
            # ----------------------------------

            if open_trade is None:

                decision = self.brain.think(

                    trend=market["trend"],

                    indicators=indicators,

                    candle=latest,

                    support=market["support"],

                    resistance=market["resistance"],

                    volatility=market["volatility"],

                    entry=latest["close"]

                )

                trade = self.simulator.execute(

                    symbol="BACKTEST",

                    decision=decision,

                    risk=decision.risk,

                    entry=latest["close"]

                )

                if trade is not None:

                    open_trade = trade

            # ----------------------------------
            # Account statistics
            # ----------------------------------

            account = self.simulator.account

            results.append({

                "index": i,

                "balance":
                    account.get_balance(),

                "peak_balance":
                    account.get_peak_balance(),

                "drawdown":
                    account.get_max_drawdown(),

                "return_percent":
                    account.get_return_percent(),

                "trade": open_trade

            })

        return results
