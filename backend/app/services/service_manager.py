"""
OpenRoIP Service Manager

Responsible for registering, starting, stopping,
and monitoring application services.
"""

from .service_state import ServiceState


class ServiceManager:

    def __init__(self):
        self.services = {}

    def register(self, name: str, service):
        """
        Register or replace a service.
        """
        if name in self.services:
            print(f"Replacing service: {name}")

        self.services[name] = service

    def start_all(self):
        """
        Start all registered services.
        """
        print("Starting OpenRoIP services...")

        for service in self.services.values():
            service.start()

    def stop_all(self):
        """
        Stop all registered services.
        """
        print("Stopping OpenRoIP services...")

        for service in self.services.values():
            service.stop()

    def get_status(self):
        """
        Return the current status of all services.
        """
        return {
            name: service.get_state().value
            for name, service in self.services.items()
        }

    def get_service(self, name: str):
        """
        Return a registered service by name.
        """
        return self.services.get(name)

    def is_running(self, name: str):
        """
        Check whether a service is running.
        """
        service = self.get_service(name)

        if service is None:
            return False

        return service.get_state() == ServiceState.RUNNING