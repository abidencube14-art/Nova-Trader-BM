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

        return self._simulation_candles(
            symbol,
            count
        )

    def _simulation_candles(
        self,
        symbol,
        count
    ):

        rows = []

        # ----------------------------------
        # Symbol-specific market settings
        # ----------------------------------

        settings = {

            "EURUSD": {
                "price": 1.1000,
                "trend": 0.000015,
                "wave": 0.00015,
                "volatility": 0.00008
            },

            "GBPUSD": {
                "price": 1.2700,
                "trend": 0.000020,
                "wave": 0.00022,
                "volatility": 0.00012
            },

            "USDJPY": {
                "price": 150.00,
                "trend": 0.012,
                "wave": 0.18,
                "volatility": 0.10
            },

            "AUDUSD": {
                "price": 0.6600,
                "trend": 0.000012,
                "wave": 0.00013,
                "volatility": 0.00007
            }

        }

        # ----------------------------------
        # Default settings
        # ----------------------------------

        market = settings.get(

            symbol,

            {
                "price": 1.0000,
                "trend": 0.000010,
                "wave": 0.00010,
                "volatility": 0.00006
            }

        )

        previous_close = market["price"]

        # ----------------------------------
        # Generate candles
        # ----------------------------------

        for i in range(count):

            # ----------------------------------
            # Market regime
            # ----------------------------------

            if i < count * 0.25:

                # Bullish phase
                trend = market["trend"]

            elif i < count * 0.50:

                # Sideways phase
                trend = 0.0

            elif i < count * 0.75:

                # Bearish phase
                trend = -market["trend"]

            else:

                # Recovery phase
                trend = market["trend"] * 0.8

            # ----------------------------------
            # Market movement
            # ----------------------------------

            wave = (

                math.sin(i / 7)

                * market["wave"]

            )

            volatility = (

                market["volatility"]

                + (

                    abs(

                        math.sin(i / 11)

                    )

                    * market["volatility"]

                    * 0.8

                )

            )

            close = (

                previous_close

                + trend

                + wave

            )

            open_price = previous_close

            high = (

                max(

                    open_price,

                    close

                )

                + volatility

            )

            low = (

                min(

                    open_price,

                    close

                )

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
