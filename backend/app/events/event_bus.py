"""
OpenRoIP Event Bus
"""


class EventBus:

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_name: str, callback):

        if event_name not in self._subscribers:
            self._subscribers[event_name] = []

        self._subscribers[event_name].append(callback)

    def publish(self, event):

        callbacks = self._subscribers.get(event.name, [])

        for callback in callbacks:
            callback(event)