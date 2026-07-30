"""
==========================================
Broker Factory
Nova-Trader-BM
==========================================
"""

from broker.adapters.simulator import SimulatorAdapter
from broker.adapters.mt5 import MT5Adapter


class BrokerFactory:

    @staticmethod
    def create(name):

        if name == "SIMULATOR":

            return SimulatorAdapter()

        elif name == "MT5":

            return MT5Adapter()

        elif name == "MT4":

            raise NotImplementedError(

                "MT4 adapter coming soon."

            )

        elif name == "CTRADER":

            raise NotImplementedError(

                "cTrader adapter coming soon."

            )

        raise ValueError(

            "Unsupported platform."

        )
