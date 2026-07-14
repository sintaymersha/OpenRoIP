"""
OpenRoIP Bridge Manager
"""

from .bridge_interface import BridgeInterface


class BridgeManager(BridgeInterface):

    def initialize(self):
        print("Bridge initialized")

    def shutdown(self):
        print("Bridge stopped")
