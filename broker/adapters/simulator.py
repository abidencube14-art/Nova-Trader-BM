"""
==========================================
Paper Trading Adapter
Nova-Trader-BM
==========================================
"""

from broker.adapters.base import BrokerAdapter


class SimulatorAdapter(BrokerAdapter):

    def connect(self):
        return True

    def disconnect(self):
        return True

    def get_balance(self):
        return 10000

    def get_positions(self):
        return []

    def buy(self, symbol, lot, sl, tp):

        print(f"SIM BUY {symbol}")

    def sell(self, symbol, lot, sl, tp):

        print(f"SIM SELL {symbol}")
