"""
==========================================
Event Manager
Nova-Trader-BM
==========================================
"""

from events.event_bus import EventBus

from events.event import Event

from events import events


class EventManager:

    def __init__(self):

        self.bus = EventBus()

    def emit(

        self,

        event_name,

        payload=None

    ):

        self.bus.publish(

            Event(

                event_name,

                payload

            )

        )

    def subscribe(

        self,

        event_name,

        callback

    ):

        self.bus.subscribe(

            event_name,

            callback

        )
