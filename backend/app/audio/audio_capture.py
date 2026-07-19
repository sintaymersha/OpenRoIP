import sounddevice as sd


class AudioCapture:

    def __init__(
        self,
        device_id=None,
        sample_rate=48000,
        channels=1,
    ):

        self.device_id = device_id
        self.sample_rate = sample_rate
        self.channels = channels

        self.stream = None
        self.running = False


    def start(self):

        if self.running:
            return

        self.stream = sd.InputStream(
            device=self.device_id,
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=self.audio_callback,
        )

        self.stream.start()

        self.running = True


    def stop(self):

        if self.stream:

            self.stream.stop()
            self.stream.close()

            self.stream = None

        self.running = False


    def audio_callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        if status:
            print(status)

        # Temporary processing point
        # Later:
        # send audio frames to buffer/RTP


    def is_running(self):

        return self.running
