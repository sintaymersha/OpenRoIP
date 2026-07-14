from .base_service import BaseService
from .service_state import ServiceState


class SystemService(BaseService):

    def start(self):

        self.state = ServiceState.STARTING

        print("System service started")

        self.state = ServiceState.RUNNING

    def stop(self):

        print("System service stopped")

        self.state = ServiceState.STOPPED