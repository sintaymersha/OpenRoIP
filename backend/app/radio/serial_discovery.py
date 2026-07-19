from serial.tools import list_ports


class SerialDiscovery:

    @staticmethod
    def discover():
        ports = []

        for port in list_ports.comports():

            # Ignore inactive legacy UARTs
            if port.device.startswith("/dev/ttyS") and port.description == "n/a":
                continue

            ports.append({
                "device": port.device,
                "name": port.name,
                "description": port.description,
                "manufacturer": port.manufacturer,
                "hwid": port.hwid,
                "serial_number": port.serial_number,
                "vid": port.vid,
                "pid": port.pid,
            })

        return ports