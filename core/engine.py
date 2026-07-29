"""
==========================================
Trading Engine
Nova-Trader-BM
==========================================
"""

from core.logger import info

from core.event_manager import EventManager

from events import events


class TradingEngine:

    def __init__(self):

        self.events = EventManager()

        info(

            "Trading Engine Ready"

        )

    def start(self):

        info(

            "Engine Started"

        )

        self.events.emit(

            events.BOT_STARTED,

            "Nova-Trader-BM"

        )
