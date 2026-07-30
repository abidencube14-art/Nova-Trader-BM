"""
==========================================
MetaTrader 5 Adapter
Nova-Trader-BM
==========================================
"""

from broker.adapters.base import BrokerAdapter


class MT5Adapter(BrokerAdapter):

    def connect(self):

        print("Connecting to MT5...")

        return True

    def disconnect(self):

        return True

    def get_balance(self):

        return 0

    def get_positions(self):

        return []

    def buy(self, symbol, lot, sl, tp):

        print(f"BUY {symbol}")

    def sell(self, symbol, lot, sl, tp):

        print(f"SELL {symbol}")
