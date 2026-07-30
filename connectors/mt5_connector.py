"""
==========================================
MetaTrader 5 Connector
Nova-Trader-BM
==========================================
"""

try:

    import MetaTrader5 as mt5

except ImportError:

    mt5 = None


class MT5Connector:

    def initialize(self):

        if mt5 is None:

            return False

        return mt5.initialize()

    def shutdown(self):

        if mt5:

            mt5.shutdown()

    def connected(self):

        return mt5 is not None
