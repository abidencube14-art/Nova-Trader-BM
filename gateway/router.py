"""
==========================================
Gateway Router
Nova-Trader-BM
==========================================
"""

from gateway.gateway import UniversalTradingGateway


class GatewayRouter:

    def route(

        self,

        platform

    ):

        return UniversalTradingGateway(

            platform

        )
