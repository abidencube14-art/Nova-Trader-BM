"""
==========================================
Market Watchlist
Nova-Trader-BM
==========================================
"""


class Watchlist:

    def __init__(self):

        self.symbols = [

            "EURUSD",

            "GBPUSD",

            "USDJPY",

            "XAUUSD"

        ]

    def all(self):

        return self.symbols

    def add(self, symbol):

        if symbol not in self.symbols:

            self.symbols.append(symbol)
