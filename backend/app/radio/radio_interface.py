"""
OpenRoIP Radio Interface

Defines the contract that every radio implementation
must follow.
"""

from abc import ABC, abstractmethod


class RadioInterface(ABC):

    @abstractmethod
    def connect(self):
        """Connect to the radio device."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from the radio device."""
        pass

    @abstractmethod
    def transmit(self, data: bytes):
        """Transmit audio/data."""
        pass

    @abstractmethod
    def receive(self):
        """Receive audio/data."""
        pass
