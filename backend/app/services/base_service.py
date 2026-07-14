from abc import ABC, abstractmethod

from .service_state import ServiceState


class BaseService(ABC):

    def __init__(self):

        self.state = ServiceState.STOPPED

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_state(self):

        return self.state