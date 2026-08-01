"""
==========================================
Market Candles
Nova-Trader-BM
==========================================
"""

from connectors.history import HistoryConnector


class CandleFeed:

    def __init__(self):

        self.history = HistoryConnector()

    def latest(

        self,

        symbol,

        timeframe,

        count=200

    ):

        return self.history.candles(

            symbol,

            timeframe,

            count

        )
