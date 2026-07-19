"""
Bridge Service
"""

from .base_service import BaseService

from app.bridge.bridge_manager import BridgeManager

from app.core.application import service_manager


class BridgeService(BaseService):
    """
    OpenRoIP Bridge Service.

    Connects Radio and Audio subsystems.
    """

    def __init__(self):

        super().__init__()

        self.bridge = BridgeManager()


    def start(self):

        self.state = self.state.STARTING

        print("Starting Bridge Service...")


        radio_service = service_manager.get_service("radio")
        audio_service = service_manager.get_service("audio")


        if radio_service:

            self.bridge.set_radio(
                radio_service.radio
            )


        if audio_service:

            self.bridge.set_audio(
                audio_service.audio
            )


        self.bridge.initialize()


        self.state = self.state.RUNNING



    def stop(self):

        print("Stopping Bridge Service...")


        self.bridge.shutdown()


        self.state = self.state.STOPPED



    def start_bridge(self):

        return self.bridge.start_bridge()



    def stop_bridge(self):

        return self.bridge.stop_bridge()

    def connect(self):

        return self.bridge.connect()



    def disconnect(self):

        return self.bridge.disconnect()



    def ptt_on(self):

        return self.bridge.ptt_on()



    def ptt_off(self):

        return self.bridge.ptt_off()

    def get_status(self):

        return self.bridge.get_status()