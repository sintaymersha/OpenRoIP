"""
OpenRoIP Radio Manager
"""

from .radio_device import RadioDevice


class RadioManager:

    def __init__(self):
        self.device = RadioDevice()

    def start(self):
        self.device.connect()

    def stop(self):
        self.device.disconnect()
