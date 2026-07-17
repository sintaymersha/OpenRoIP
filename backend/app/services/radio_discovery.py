"""
OpenRoIP Radio Discovery Service

Responsible for discovering available radio devices.
"""

from .service_state import ServiceState


class RadioDiscoveryService:

    def __init__(self):
        self.state = ServiceState.STOPPED

    def start(self):
        print("Starting Radio Discovery Service...")
        self.state = ServiceState.RUNNING

    def stop(self):
        print("Stopping Radio Discovery Service...")
        self.state = ServiceState.STOPPED

    def get_state(self):
        return self.state

    def discover(self):
        return [
            {
                "id": "radio0",
                "type": "virtual",
                "name": "Virtual Radio",
                "status": "available",
            }
        ]