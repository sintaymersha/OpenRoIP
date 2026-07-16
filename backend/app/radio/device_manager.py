class DeviceManager:


    def __init__(self):

        self.devices = []


    def scan(self):

        # Future:
        # USB scan
        # SDR detection

        self.devices = [
            {
                "name": "Virtual Radio",
                "type": "simulation"
            }
        ]

        return self.devices
