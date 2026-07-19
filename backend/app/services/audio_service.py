from .base_service import BaseService
from .service_state import ServiceState

from app.audio.audio_manager import AudioManager


class AudioService(BaseService):
    """
    OpenRoIP Audio Service.

    Manages audio input and output operations.
    """

    def __init__(self):
        super().__init__()

        self.audio = AudioManager()

    def start(self):
        self.state = ServiceState.STARTING

        print("Starting Audio Service...")

        self.state = ServiceState.RUNNING

    def stop(self):
        self.audio.stop_rx_audio()
        self.audio.stop_tx_audio()

        self.state = ServiceState.STOPPED

    def start_rx(self):
        """
        Start receiving audio.
        """
        return self.audio.start_rx_audio()

    def stop_rx(self):
        """
        Stop receiving audio.
        """
        return self.audio.stop_rx_audio()

    def start_tx(self):
        """
        Start transmitting audio.
        """
        return self.audio.start_tx_audio()

    def stop_tx(self):
        """
        Stop transmitting audio.
        """
        return self.audio.stop_tx_audio()

    def get_status(self):
        """
        Return current audio status.
        """
        return self.audio.get_status()

    def get_state(self):
        """
        Return Audio Service state.
        """
        return self.state