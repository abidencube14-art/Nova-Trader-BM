"""
==========================================
History Connector
Nova-Trader-BM
==========================================
"""

from connectors.mt5_connector import mt5


class HistoryConnector:

    def candles(

        self,

        symbol,

        timeframe,

        count

    ):

        if mt5 is None:

            return []

        return mt5.copy_rates_from_pos(

            symbol,

            timeframe,

            0,

            count

        )
