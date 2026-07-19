from app.audio.audio_interface import AudioInterface


class VirtualAudio(AudioInterface):
    """
    Software-based audio device for testing.
    Used when physical audio hardware is unavailable.
    """

    def __init__(self):
        self.input_active = False
        self.output_active = False

    def start_input(self):
        self.input_active = True
        return True

    def stop_input(self):
        self.input_active = False
        return True

    def start_output(self):
        self.output_active = True
        return True

    def stop_output(self):
        self.output_active = False
        return True

    def get_status(self):
        return {
            "input": self.input_active,
            "output": self.output_active,
            "device": "Virtual Audio"
        }