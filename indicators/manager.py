"""
==========================================
Indicator Manager
Nova-Trader-BM
==========================================
"""

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.atr import calculate_atr
from indicators.macd import calculate_macd


class IndicatorManager:

    def analyse(self, data):

        ema50 = calculate_ema(data, 20)
        
        ema50 = calculate_ema(data, 50)

        ema200 = calculate_ema(data, 200)

        rsi = calculate_rsi(data)

        atr = calculate_atr(data)

        macd, signal, histogram = calculate_macd(data)

        return {

            "ema20": ema20.iloc[-1],

            "ema50": ema50.iloc[-1],

            "ema200": ema200.iloc[-1],

            "rsi": rsi.iloc[-1],

            "atr": atr.iloc[-1],

            "macd": macd.iloc[-1],

            "signal": signal.iloc[-1],

            "histogram": histogram.iloc[-1]

        }
