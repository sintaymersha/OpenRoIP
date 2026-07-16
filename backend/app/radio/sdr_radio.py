from app.radio.radio_interface import RadioInterface


class SDRRadio(RadioInterface):

    def __init__(self):

        self.connected = False
        self.device = "No SDR Device"


    def connect(self):

        # Future:
        # Detect RTL-SDR / HackRF / USRP

        self.connected = True
        self.device = "SDR Device"

        return {
            "status": "connected",
            "device": self.device
        }


    def get_status(self):

        return {
            "connected": self.connected,
            "device": self.device,
            "ptt": False,
            "transmitting": False,
            "receiving": False
        }


    def ptt_on(self):

        return {
            "status": "SDR PTT ON"
        }


    def ptt_off(self):

        return {
            "status": "SDR PTT OFF"
        }
