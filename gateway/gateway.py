"""
==========================================
Universal Trading Gateway
Nova-Trader-BM
==========================================
"""

from broker.factory import BrokerFactory


class UniversalTradingGateway:

    def __init__(

        self,

        platform

    ):

        self.platform = platform

        self.adapter = BrokerFactory.create(

            platform

        )

    def connect(self):

        return self.adapter.connect()

    def disconnect(self):

        return self.adapter.disconnect()

    def buy(

        self,

        symbol,

        lot,

        sl,

        tp

    ):

        return self.adapter.buy(

            symbol,

            lot,

            sl,

            tp

        )

    def sell(

        self,

        symbol,

        lot,

        sl,

        tp

    ):

        return self.adapter.sell(

            symbol,

            lot,

            sl,

            tp

        )
