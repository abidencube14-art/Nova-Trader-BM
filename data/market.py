"""
==========================================
Market Data
Nova-Trader-BM
==========================================
"""

import pandas as pd


class MarketData:

    def __init__(self):

        self.data = pd.DataFrame()

    def load(self, dataframe):

        self.data = dataframe

    def latest(self):

        return self.data.iloc[-1]

    def candles(self):

        return self.data
