"""
OpenRoIP Radio State

Represents the current state of the radio subsystem.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RadioState:
    """
    Current radio status.
    """

    connected: bool = False
    device: str = "Unknown"

    ptt: bool = False
    transmitting: bool = False
    receiving: bool = False

    channel: str = "N/A"
    frequency: float = 0.0

    last_updated: datetime = field(default_factory=datetime.utcnow)

    def touch(self):
        """Update the timestamp whenever the state changes."""
        self.last_updated = datetime.utcnow()

    def to_dict(self):
        """Return the state as a dictionary."""
        return {
            "connected": self.connected,
            "device": self.device,
            "ptt": self.ptt,
            "transmitting": self.transmitting,
            "receiving": self.receiving,
            "channel": self.channel,
            "frequency": self.frequency,
            "last_updated": self.last_updated.isoformat()
        }
