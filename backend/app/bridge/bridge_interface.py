"""
Bridge interface for OpenRoIP.
"""

from abc import ABC, abstractmethod


class BridgeInterface(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
