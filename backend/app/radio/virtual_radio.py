from app.radio.radio_interface import RadioInterface


class VirtualRadio(RadioInterface):

    def __init__(self):
        self.connected = True
        self.ptt = False
        self.transmitting = False
        self.receiving = False
        self.channel = "N/A"
        self.frequency = 0.0


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


        return {
            "status": "PTT ON"
        }


    def ptt_off(self):

        self.ptt = False
        self.transmitting = False


        return {
            "status": "PTT OFF"
        }