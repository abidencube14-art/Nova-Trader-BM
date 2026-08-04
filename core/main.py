"""
==========================================
Nova-Trader-BM
Main Entry Point
==========================================
"""

from core.master_loop import MasterTradingLoop


def main():

    bot = MasterTradingLoop()

    bot.run(

        symbol="EURUSD",

        timeframe=5

    )


if __name__ == "__main__":

    main()
