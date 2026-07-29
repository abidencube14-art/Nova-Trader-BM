"""
==========================================
System State
Nova-Trader-BM
==========================================
"""


class SystemState:

    def __init__(self):

        self.data = {

            "bot_status": "OFFLINE",

            "mt5_status": "DISCONNECTED",

            "brain_status": "IDLE",

            "confidence": 0,

            "current_signal": "NONE",

            "symbol": "NONE",

            "risk": "0%",

            "trades_today": 0,

            "profit": 0,

            "win_rate": 0

        }


    def update(self, key, value):

        if key in self.data:

            self.data[key] = value


    def get(self):

        return self.data
