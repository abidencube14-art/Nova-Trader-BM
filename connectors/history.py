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

            # ----------------------------------
            # Market regime
            # ----------------------------------

            if i < count * 0.25:

                # Bullish phase
                trend = 0.000015

            elif i < count * 0.50:

                # Sideways phase
                trend = 0.0

            elif i < count * 0.75:

                # Bearish phase
                trend = -0.000018

            else:

                # Recovery / bullish phase
                trend = 0.000012

            # ----------------------------------
            # Market movement
            # ----------------------------------

            wave = math.sin(i / 7) * 0.00015

            volatility = (

                0.00008

                + abs(math.sin(i / 11)) * 0.00007

            )

            close = (

                previous_close

                + trend

                + wave

            )

            open_price = previous_close

            high = (

                max(open_price, close)

                + volatility

            )

            low = (

                min(open_price, close)

                - volatility

            )

            rows.append({

                "open": open_price,

                "high": high,

                "low": low,

                "close": close,

                "tick_volume": 100

            })

            previous_close = close

        return pd.DataFrame(rows)
