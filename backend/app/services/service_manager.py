"""
OpenRoIP Service Manager

Controls startup and shutdown
of application services.
"""


class ServiceManager:

    def __init__(self):
        self.services = []


    def register(self, service):
        self.services.append(service)


    def start_all(self):

        print("Starting OpenRoIP services...")

        for service in self.services:
            service.start()


    def stop_all(self):

        print("Stopping OpenRoIP services...")

        for service in self.services:
            service.stop()
