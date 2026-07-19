from app.audio.virtual_audio import VirtualAudio


class AudioManager:
    """
    Manages OpenRoIP audio devices.
    """

    def __init__(self):
        self.audio = VirtualAudio()

    def start_rx_audio(self):
        """
        Start receiving audio.
        """
        return self.audio.start_input()

    def stop_rx_audio(self):
        """
        Stop receiving audio.
        """
        return self.audio.stop_input()

    def start_tx_audio(self):
        """
        Start transmitting audio.
        """
        return self.audio.start_output()

    def stop_tx_audio(self):
        """
        Stop transmitting audio.
        """
        return self.audio.stop_output()

    def get_status(self):
        """
        Return audio status.
        """
        return self.audio.get_status()