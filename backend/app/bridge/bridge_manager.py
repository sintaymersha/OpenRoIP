"""
OpenRoIP Bridge Manager

Coordinates communication between Radio and Audio subsystems.
"""

import threading
import time

from .bridge_interface import BridgeInterface

from app.core.exceptions import RadioNotConnectedError


class BridgeManager(BridgeInterface):

    def __init__(self):

        self.connected = False
        self.ptt = False

        self.running = False
        self.thread = None

        self.radio = None
        self.audio = None


    def initialize(self) -> None:
        """
        Initialize bridge.
        """

        print("Bridge initialized")



    def shutdown(self) -> None:
        """
        Shutdown bridge.
        """

        self.stop_streaming()

        self.connected = False
        self.ptt = False

        print("Bridge stopped")



    def connect(self) -> bool:
        """
        Connect bridge.
        """

        self.connected = True

        return True



    def disconnect(self) -> bool:
        """
        Disconnect bridge.
        """

        self.stop_streaming()

        self.connected = False
        self.ptt = False

        return True



    def set_radio(self, radio):

        self.radio = radio



    def set_audio(self, audio):

        self.audio = audio



    def start_bridge(self):

        self.connect()

        self.start_streaming()

        return True



    def stop_bridge(self):

        self.stop_streaming()

        self.disconnect()

        return True



    def start_streaming(self):

        if self.running:
            return


        self.running = True


        self.thread = threading.Thread(
            target=self.rx_loop,
            daemon=True
        )


        self.thread.start()



    def stop_streaming(self):

        self.running = False



    def rx_loop(self):
        """
        Radio RX -> Audio Queue
        """

        print("Bridge RX loop started")


        while self.running:

            if self.radio and self.audio:

                frame = self.radio.receive_audio()


                if frame:

                    self.audio.push_frame(frame)

                    print(
                        "Radio audio frame pushed:",
                        frame.info()
                    )


            time.sleep(0.02)



    def get_status(self):

        return {
            "connected": self.connected,
            "ptt": self.ptt,
            "running": self.running,
            "radio_attached": self.radio is not None,
            "audio_attached": self.audio is not None,
        }



    def ptt_on(self) -> bool:

        if not self.connected:

            raise RadioNotConnectedError()


        self.ptt = True

        return True



    def ptt_off(self) -> bool:

        self.ptt = False

        return True