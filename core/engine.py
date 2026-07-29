"""
==========================================
Trading Engine
Nova-Trader-BM
==========================================
"""

from core.logger import info

from state.system_state import SystemState


class TradingEngine:


    def __init__(self):

        self.state = SystemState()

        info(

            "Nova Engine Initialized"

        )


    def start(self):

        self.state.update(

            "bot_status",

            "ONLINE"

        )


        self.state.update(

            "brain_status",

            "ACTIVE"

        )


        info(

            "Nova-Trader-BM Started"

        )
