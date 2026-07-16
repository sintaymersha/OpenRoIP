class AudioPipeline:


    def __init__(self):

        self.running = False


    def start_receive(self):

        self.running = True

        return {
            "status":"RX started"
        }


    def stop_receive(self):

        self.running = False

        return {
            "status":"RX stopped"
        }
