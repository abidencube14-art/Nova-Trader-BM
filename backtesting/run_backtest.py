"""
==========================================
Nova Backtest Runner
Nova-Trader-BM
==========================================
"""

from market_data.candles import CandleFeed
from backtesting.backtester import Backtester
from backtesting.report import Report


def main():

    print("===================================")
    print("NOVA TRADER BM - BACKTEST")
    print("===================================")

    market = CandleFeed()

    candles = market.latest(

        symbol="EURUSD",

        timeframe=5,

        count=1000

    )

    if candles is None or len(candles) < 200:

        print("Not enough historical candle data.")

        return

    print(

        f"Loaded {len(candles)} candles"

    )

    backtester = Backtester()

    backtester.run(candles)

    report = Report()

    report.generate(

        backtester.simulator

    )


if __name__ == "__main__":

    main()
