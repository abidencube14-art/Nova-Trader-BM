"""
==========================================
Dashboard Data Provider
Nova-Trader-BM
==========================================
"""


class DashboardData:


    def get_status(self):


        return {


            "bot":
            "ONLINE",


            "mt5":
            "CONNECTING",


            "brain":
            "ACTIVE",


            "learning":
            "ACTIVE",


            "confidence":
            94,


            "risk":
            "0.75%",


            "trades_today":
            7,


            "win_rate":
            82,


            "profit":
            "£43.50",


            "market":

            [

                {
                    "symbol":"EURUSD",
                    "status":"BULLISH"
                },

                {
                    "symbol":"GBPUSD",
                    "status":"WAITING"
                },

                {
                    "symbol":"XAUUSD",
                    "status":"VOLATILE"
                }

            ],


            "analysis":

            [

                "Trend: Bullish",

                "Momentum: Strong",

                "Risk: Acceptable",

                "Setup Match: 78%"

            ]

        }
