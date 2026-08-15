"""
==========================================
Nova Multi-Pair Backtest Runner
Nova-Trader-BM
==========================================
"""

from market_data.candles import CandleFeed
from backtesting.backtester import Backtester
from backtesting.report import Report


SYMBOLS = [

    "EURUSD",

    "GBPUSD",

    "USDJPY",

    "AUDUSD"

]


def main():

    print("===================================")

    print("NOVA TRADER BM - MULTI-PAIR BACKTEST")

    print("===================================")

    market = CandleFeed()

    for symbol in SYMBOLS:

        print()

        print("-----------------------------------")

        print(
            f"BACKTESTING {symbol}"
        )

        print("-----------------------------------")

        candles = market.latest(

            symbol=symbol,

            timeframe=5,

            count=1000

        )

        if candles is None or len(candles) < 200:

            print(
                f"Not enough data for {symbol}."
            )

            continue

        print(
            f"Loaded {len(candles)} candles"
        )

        backtester = Backtester()

        backtester.run(candles)

        report = Report()

        report.generate(

            backtester.simulator

        )

    print()

    print("===================================")

    print("MULTI-PAIR BACKTEST COMPLETE")

    print("===================================")


if __name__ == "__main__":

    main()
