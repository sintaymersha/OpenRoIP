from .base_service import BaseService
from .service_state import ServiceState

from app.radio.radio_manager import RadioManager


class RadioService(BaseService):

    def __init__(self):

        super().__init__()

        self.radio = RadioManager()

    def start(self):

        self.state = ServiceState.STARTING

        print("Starting Radio Service...")

        self.radio.start()

        self.state = ServiceState.RUNNING

    def stop(self):

        self.radio.stop()

        self.state = ServiceState.STOPPED