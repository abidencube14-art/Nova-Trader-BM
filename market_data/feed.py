"""
==========================================
Market Feed
Nova-Trader-BM
==========================================
"""

from connectors.market import MarketConnector


class MarketFeed:

    def __init__(self):

        self.market = MarketConnector()

    def tick(self, symbol):

        return self.market.tick(symbol)

    def symbol(self, symbol):

        return self.market.symbol(symbol)
