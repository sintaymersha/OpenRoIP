"""
OpenRoIP Audio Manager

Manages audio devices, RX/TX streaming,
and audio frame buffering.
"""

import threading
import time
from queue import Empty

from app.audio.virtual_audio import VirtualAudio
from app.audio.audio_queue import AudioQueue
from app.audio.audio_frame import AudioFrame


class AudioManager:
    """
    Manages OpenRoIP audio devices and streaming.
    """

    def __init__(self):

        self.audio = VirtualAudio()

        self.queue = AudioQueue()

        self.rx_running = False
        self.tx_running = False

        self.rx_thread = None
        self.tx_thread = None


    def rx_worker(self):
        """
        Audio capture worker.
        """

        print("RX audio thread started")

        while self.rx_running:

            # Future:
            # frame = self.audio.read_input()

            frame = AudioFrame(
                data=b"virtual pcm data"
            )

            self.queue.put(frame)

            time.sleep(0.02)


        print("RX audio thread stopped")



    def tx_worker(self):
        """
        Audio playback worker.
        """

        print("TX audio thread started")

        while self.tx_running:

            try:

                frame = self.queue.get(
                    timeout=1
                )

                if frame:

                    print(
                        "Playing audio frame:",
                        frame.info()
                    )


            except Empty:

                continue


            time.sleep(0.02)


        print("TX audio thread stopped")



    def start_rx_audio(self):
        """
        Start receiving audio.
        """

        self.audio.start_input()


        if not self.rx_running:

            self.rx_running = True

            self.rx_thread = threading.Thread(
                target=self.rx_worker,
                daemon=True,
            )

            self.rx_thread.start()


        return {
            "rx": "started"
        }



    def stop_rx_audio(self):
        """
        Stop receiving audio.
        """

        self.rx_running = False

        self.audio.stop_input()


        return {
            "rx": "stopped"
        }



    def start_tx_audio(self):
        """
        Start transmitting audio.
        """

        self.audio.start_output()


        if not self.tx_running:

            self.tx_running = True

            self.tx_thread = threading.Thread(
                target=self.tx_worker,
                daemon=True,
            )

            self.tx_thread.start()


        return {
            "tx": "started"
        }



    def stop_tx_audio(self):
        """
        Stop transmitting audio.
        """

        self.tx_running = False

        self.audio.stop_output()


        return {
            "tx": "stopped"
        }



    def push_frame(self, frame):
        """
        Push an audio frame into the queue.
        """

        self.queue.put(frame)



    def pop_frame(self):
        """
        Retrieve an audio frame.
        """

        try:

            return self.queue.get(
                timeout=1
            )

        except Empty:

            return None



    def get_status(self):
        """
        Return audio status.
        """

        status = self.audio.get_status()

        status.update(
            {
                "queue_size": self.queue.size(),
                "rx_thread": self.rx_running,
                "tx_thread": self.tx_running,
            }
        )

        return status