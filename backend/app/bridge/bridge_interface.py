"""
Bridge interface for OpenRoIP.

Defines the operations that every bridge implementation
must provide, regardless of the underlying radio hardware.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BridgeInterface(ABC):

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the bridge."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the bridge."""
        pass

    @abstractmethod
    def connect(self) -> bool:
        """Connect to the radio."""
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from the radio."""
        pass

    @abstractmethod
    def get_status(self) -> Dict[str, Any]:
        """Return the current radio status."""
        pass

    @abstractmethod
    def ptt_on(self) -> bool:
        """Enable Push-To-Talk."""
        pass

    @abstractmethod
    def ptt_off(self) -> bool:
        """Disable Push-To-Talk."""
        pass