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

        if name == "MT5":

            return MT5Adapter()

        raise ValueError(

            "Unsupported broker"

        )
