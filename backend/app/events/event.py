"""
OpenRoIP Event
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Event:
    """
    Generic application event.
    """

    name: str
    data: dict = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)