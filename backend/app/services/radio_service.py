from .base_service import BaseService
from .service_state import ServiceState

from app.radio.radio_manager import RadioManager


class RadioService(BaseService):

    def __init__(self):
        super().__init__()

        self.radio = RadioManager()

    def start(self):
        self.state = ServiceState.STARTING

        print("Starting Radio Service...")

        self.radio.start()

        self.state = ServiceState.RUNNING

    def stop(self):
        self.radio.stop()

        self.state = ServiceState.STOPPED

    def connect(self, device: str = "Virtual Radio"):
        """
        Connect to a radio device.
        """
        self.radio.connect(device)

    def disconnect(self):
        """
        Disconnect the current radio.
        """
        self.radio.disconnect()

    def get_status(self):
        """
        Return current radio status.
        """
        return self.radio.get_status()

    def get_state(self):
        """
        Return the RadioState object.
        """
        return self.radio.get_state()

    def ptt_on(self):
        """
        Enable Push-To-Talk.
        """
        self.radio.set_ptt(True)

    def ptt_off(self):
        """
        Disable Push-To-Talk.
        """
        self.radio.set_ptt(False)

    def set_frequency(self, frequency: float):
        """
        Set radio operating frequency.
        """
        self.radio.set_frequency(frequency)

    def set_channel(self, channel: str):
        """
        Set radio operating channel.
        """
        self.radio.set_channel(channel)

    def set_transmitting(self, enabled: bool):
        """
        Set transmission state.
        """
        self.radio.set_transmitting(enabled)

    def set_receiving(self, enabled: bool):
        """
        Set receiving state.
        """
        self.radio.set_receiving(enabled)
    def discover_serial_ports(self):
        """
        Return all detected serial ports.
        """
        return self.radio.discover_serial_ports()