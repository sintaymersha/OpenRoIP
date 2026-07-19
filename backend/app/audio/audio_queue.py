from queue import Queue, Empty


class AudioQueue:
    """
    Thread-safe audio frame queue.
    """

    def __init__(self, maxsize=100):
        self.queue = Queue(maxsize=maxsize)

    def put(self, frame):
        """
        Push an audio frame into the queue.
        """
        self.queue.put(frame)

    def get(self, timeout=0.1):
        """
        Retrieve an audio frame.
        """
        try:
            return self.queue.get(timeout=timeout)
        except Empty:
            return None

    def clear(self):
        """
        Remove all pending frames.
        """
        while not self.queue.empty():
            self.queue.get_nowait()

    def size(self):
        """
        Number of queued frames.
        """
        return self.queue.qsize()