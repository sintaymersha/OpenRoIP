from abc import ABC, abstractmethod


class AudioInterface(ABC):
    """
    Abstract interface for all audio implementations.
    Hardware-specific audio drivers must inherit from this class.
    """

    @abstractmethod
    def start_input(self):
        """
        Start receiving audio input.
        """
        pass

    @abstractmethod
    def stop_input(self):
        """
        Stop receiving audio input.
        """
        pass

    @abstractmethod
    def start_output(self):
        """
        Start audio output.
        """
        pass

    @abstractmethod
    def stop_output(self):
        """
        Stop audio output.
        """
        pass

    @abstractmethod
    def get_status(self):
        """
        Return current audio status.
        """
        pass