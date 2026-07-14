from .radio_interface import RadioInterface


class RadioDevice(RadioInterface):

    def connect(self):
        print("Radio connected")

    def disconnect(self):
        print("Radio disconnected")

    def transmit(self, data: bytes):
        print(f"Transmitting {len(data)} bytes")

    def receive(self):
        print("Receiving data...")
        return b""
