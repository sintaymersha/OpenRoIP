from app.radio.radio_interface import RadioInterface


class VirtualRadio(RadioInterface):

    def __init__(self):

        self.connected = True
        self.ptt = False
        self.transmitting = False
        self.receiving = False
        self.channel = "N/A"
        self.frequency = 0.0


    def connect(self):

        self.connected = True

        return {
            "status": "connected"
        }


    def disconnect(self):

        self.connected = False
        self.ptt = False
        self.transmitting = False
        self.receiving = False

        return {
            "status": "disconnected"
        }


    def transmit(self, data=None):

        if not self.connected:
            return {
                "status": "radio disconnected"
            }

        self.transmitting = True

        return {
            "status": "transmitting"
        }


    def receive(self):

        if not self.connected:
            return {
                "status": "radio disconnected"
            }

        self.receiving = True

        return {
            "status": "receiving"
        }


    def get_status(self):

        return {
            "connected": self.connected,
            "device": "Virtual Radio",
            "ptt": self.ptt,
            "transmitting": self.transmitting,
            "receiving": self.receiving,
            "channel": self.channel,
            "frequency": self.frequency
        }


    def ptt_on(self):

        self.ptt = True
        self.transmitting = True
        self.receiving = False

        return {
            "status": "PTT ON"
        }


    def ptt_off(self):

        self.ptt = False
        self.transmitting = False

        return {
            "status": "PTT OFF"
        }