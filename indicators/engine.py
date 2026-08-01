"""
==========================================
Indicator Engine
Nova-Trader-BM
==========================================
"""

from indicators.snapshot import IndicatorSnapshot

from indicators.ema import EMA

from indicators.rsi import RSI

from indicators.macd import MACD

from indicators.atr import ATR

from indicators.bollinger import BollingerBands


class IndicatorEngine:

    def __init__(self):

        self.ema = EMA()

        self.rsi = RSI()

        self.macd = MACD()

        self.atr = ATR()

        self.bb = BollingerBands()

    def build(self, candles):

        snapshot = IndicatorSnapshot()

        snapshot.set("ema20", self.ema.calculate(candles, 20))

        snapshot.set("ema50", self.ema.calculate(candles, 50))

        snapshot.set("ema200", self.ema.calculate(candles, 200))

        snapshot.set("rsi14", self.rsi.calculate(candles))

        snapshot.set("macd", self.macd.calculate(candles))

        snapshot.set("atr", self.atr.calculate(candles))

        snapshot.set("bollinger", self.bb.calculate(candles))

        return snapshotq11
