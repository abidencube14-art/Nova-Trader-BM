"""
==========================================
Market Structure
Nova-Trader-BM
==========================================
"""


class MarketStructure:

    def trend(self, data):

        highs = data["high"].tail(5)

        lows = data["low"].tail(5)

        if highs.is_monotonic_increasing and lows.is_monotonic_increasing:

            return "UPTREND"

        if highs.is_monotonic_decreasing and lows.is_monotonic_decreasing:

            return "DOWNTREND"

        return "RANGE"
