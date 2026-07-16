"""
OpenRoIP Bridge Manager
"""

from .bridge_interface import BridgeInterface
from app.core.exceptions import RadioNotConnectedError


class BridgeManager(BridgeInterface):

    def __init__(self):
        self.connected = False
        self.ptt = False

    def initialize(self) -> None:
        print("Bridge initialized")

    def shutdown(self) -> None:
        print("Bridge stopped")

    def connect(self) -> bool:
        self.connected = True
        return True

    def disconnect(self) -> bool:
        self.connected = False
        self.ptt = False
        return True

    def get_status(self):
        return {
            "connected": self.connected,
            "ptt": self.ptt,
        }

    def ptt_on(self) -> bool:
        if not self.connected:
            raise RadioNotConnectedError()

        self.ptt = True
        return True

    def ptt_off(self) -> bool:
        self.ptt = False
        return True