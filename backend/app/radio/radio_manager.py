"""
OpenRoIP Radio Manager
"""

from app.core.application import event_bus
from app.events.event import Event
from app.events.radio_events import RADIO_STATE_CHANGED

from .radio_state import RadioState


class RadioManager:

    def __init__(self):
        self.state = RadioState()

    def _notify_state_changed(self):
        """
        Publish a radio state change event.
        """
        event_bus.publish(
            Event(
                name=RADIO_STATE_CHANGED,
                data=self.get_status(),
            )
        )

    def start(self):
        """
        Initialize the radio subsystem.
        """
        print("Initializing Radio...")
        self.connect("Virtual Radio")
        print("Radio initialized")

    def stop(self):
        """
        Stop the radio subsystem.
        """
        self.disconnect()
        print("Radio stopped")

    def connect(self, device="Virtual Radio"):
        """
        Connect to a radio device.
        """
        self.state.connected = True
        self.state.device = device
        self.state.touch()

        self._notify_state_changed()

    def disconnect(self):
        """
        Disconnect the radio device.
        """
        self.state.connected = False
        self.state.ptt = False
        self.state.transmitting = False
        self.state.receiving = False
        self.state.touch()

        self._notify_state_changed()

    def set_ptt(self, enabled: bool):
        """
        Enable or disable Push-To-Talk.
        """
        if not self.state.connected:
            return

        self.state.ptt = enabled

        if enabled:
            self.state.transmitting = True
            self.state.receiving = False
        else:
            self.state.transmitting = False

        self.state.touch()

        self._notify_state_changed()

    def set_transmitting(self, enabled: bool):
        """
        Enable or disable transmission.
        """
        if not self.state.connected:
            return

        self.state.transmitting = enabled

        if enabled:
            self.state.receiving = False

        self.state.touch()

        self._notify_state_changed()

    def set_receiving(self, enabled: bool):
        """
        Enable or disable reception.
        """
        if not self.state.connected:
            return

        self.state.receiving = enabled

        if enabled:
            self.state.transmitting = False

        self.state.touch()

        self._notify_state_changed()

    def set_frequency(self, frequency: float):
        """
        Set operating frequency.
        """
        self.state.frequency = frequency
        self.state.touch()

        self._notify_state_changed()

    def set_channel(self, channel: str):
        """
        Set operating channel.
        """
        self.state.channel = channel
        self.state.touch()

        self._notify_state_changed()

    def get_state(self):
        """
        Return the RadioState object.
        """
        return self.state

    def get_status(self):
        """
        Return the radio status as a dictionary.
        """
        return self.state.to_dict()