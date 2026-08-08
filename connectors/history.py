"""
==========================================
History Connector
Nova-Trader-BM
==========================================
"""

import math
import pandas as pd

from connectors.mt5_connector import mt5


class HistoryConnector:

    def candles(
        self,
        symbol,
        timeframe,
        count
    ):

        # ----------------------------------
        # Real MT5 market data
        # ----------------------------------

        if mt5 is not None:

            rates = mt5.copy_rates_from_pos(
                symbol,
                timeframe,
                0,
                count
            )

            if rates is not None and len(rates) > 0:

                return pd.DataFrame(rates)

        # ----------------------------------
        # Simulation fallback
        # ----------------------------------

        return self._simulation_candles(count)

    def _simulation_candles(self, count):

        rows = []

        previous_close = 1.1000

        for i in range(count):

            close = (
                1.1000
                + (i * 0.00002)
                + (math.sin(i / 8) * 0.00015)
            )

            open_price = previous_close

            high = max(open_price, close) + 0.00008

            low = min(open_price, close) - 0.00008

            rows.append({
                "open": open_price,
                "high": high,
                "low": low,
                "close": close,
                "tick_volume": 100
            })

            previous_close = close

        return pd.DataFrame(rows)
