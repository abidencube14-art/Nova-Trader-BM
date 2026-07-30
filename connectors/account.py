"""
==========================================
Account Connector
Nova-Trader-BM
==========================================
"""

from connectors.mt5_connector import mt5


class AccountConnector:

    def info(self):

        if mt5 is None:

            return None

        return mt5.account_info()
