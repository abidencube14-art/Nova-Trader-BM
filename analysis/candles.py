"""
==========================================
Candlestick Pattern Recognition
Nova-Trader-BM
==========================================
"""


class CandlePatterns:

    def bullish_engulfing(self, data):

        if len(data) < 2:
            return False

        previous = data.iloc[-2]

        current = data.iloc[-1]

        return (

            previous.close < previous.open

            and

            current.close > current.open

            and

            current.close > previous.open

            and

            current.open < previous.close

        )

    def bearish_engulfing(self, data):

        if len(data) < 2:
            return False

        previous = data.iloc[-2]

        current = data.iloc[-1]

        return (

            previous.close > previous.open

            and

            current.close < current.open

            and

            current.open > previous.close

            and

            current.close < previous.open

        )

    def doji(self, data):

        candle = data.iloc[-1]

        body = abs(candle.close - candle.open)

        return body <= (candle.high - candle.low) * 0.1
