"""
==========================================
Dashboard Data Provider
Nova-Trader-BM
==========================================
"""


class DashboardData:

    def get_status(self):

        return {

            "bot": "ONLINE",

            "mt5": "DISCONNECTED",

            "brain": "ACTIVE",

            "learning": "ACTIVE",

            "confidence": 94,

            "risk": "0.75%",

            "trades_today": 0,

            "win_rate": 0,

            "profit": 0

        }
