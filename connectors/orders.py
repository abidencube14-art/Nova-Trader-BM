"""
==========================================
Order Connector
Nova-Trader-BM
==========================================
"""

from connectors.mt5_connector import mt5


class OrderConnector:

    def send(self, request):

        if mt5 is None:

            return None

        return mt5.order_send(request)
