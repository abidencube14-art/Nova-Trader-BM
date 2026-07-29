"""
==========================================
Advanced Candle Patterns
Nova-Trader-BM
==========================================
"""


class CandlePatterns:

    def body(self, candle):

        return abs(candle.close - candle.open)

    def bullish_engulfing(self, data):

        if len(data) < 2:

            return False

        p = data.iloc[-2]

        c = data.iloc[-1]

        return (

            p.close < p.open

            and

            c.close > c.open

            and

            c.open < p.close

            and

            c.close > p.open

        )

    def bearish_engulfing(self, data):

        if len(data) < 2:

            return False

        p = data.iloc[-2]

        c = data.iloc[-1]

        return (

            p.close > p.open

            and

            c.close < c.open

            and

            c.open > p.close

            and

            c.close < p.open

        )

    def hammer(self, data):

        c = data.iloc[-1]

        body = abs(c.close - c.open)

        lower = min(c.close, c.open) - c.low

        return lower > body * 2

    def shooting_star(self, data):

        c = data.iloc[-1]

        body = abs(c.close - c.open)

        upper = c.high - max(c.close, c.open)

        return upper > body * 2

    def doji(self, data):

        c = data.iloc[-1]

        body = abs(c.close - c.open)

        return body <= (c.high - c.low) * 0.1
