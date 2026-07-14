"""
Audio streaming placeholder.

Later this module will:
- capture audio
- encode/decode
- buffer packets
- interface with the C++ audio engine
"""


class AudioStream:

    def start(self):
        print("Audio stream started")

    def stop(self):
        print("Audio stream stopped")
