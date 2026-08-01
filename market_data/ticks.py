"""
==========================================
Live Tick Feed
Nova-Trader-BM
==========================================
"""

import time

from market_data.feed import MarketFeed


class TickFeed:

    def __init__(self):

        self.feed = MarketFeed()

    def stream(

        self,

        symbol,

        interval=1

    ):

        while True:

            tick = self.feed.tick(symbol)

            yield tick

            time.sleep(interval)
