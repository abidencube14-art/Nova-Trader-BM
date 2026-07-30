"""
==========================================
Market Connector
Nova-Trader-BM
==========================================
"""

from connectors.mt5_connector import mt5


class MarketConnector:

    def symbol(self, name):

        if mt5 is None:

            return None

        return mt5.symbol_info(name)

    def tick(self, name):

        if mt5 is None:

            return None

        return mt5.symbol_info_tick(name)
