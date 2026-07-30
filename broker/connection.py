"""
==========================================
Broker Connection
Nova-Trader-BM
==========================================
"""

from broker.factory import BrokerFactory


class BrokerConnection:

    def __init__(

        self,

        broker="SIMULATOR"

    ):

        self.adapter = BrokerFactory.create(

            broker

        )

    def connect(self):

        return self.adapter.connect()

    def disconnect(self):

        return self.adapter.disconnect()
