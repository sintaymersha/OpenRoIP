"""
Audio Frame Model
"""

import time


class AudioFrame:

    def __init__(
        self,
        data: bytes,
        sample_rate: int = 8000,
        channels: int = 1,
        sample_width: int = 2,
    ):

        self.data = data
        self.sample_rate = sample_rate
        self.channels = channels
        self.sample_width = sample_width
        self.timestamp = time.time()


    def info(self):

        return {
            "size": len(self.data),
            "sample_rate": self.sample_rate,
            "channels": self.channels,
            "sample_width": self.sample_width,
            "timestamp": self.timestamp,
        }