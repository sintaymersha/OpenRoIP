import sounddevice as sd

from app.audio.audio_device import AudioDevice


class AudioDiscovery:

    def discover(self):
        devices = []

        device_list = sd.query_devices()

        print("\n========== AUDIO DEVICES ==========")
        print(f"Found {len(device_list)} device(s)\n")

        default_input, default_output = sd.default.device

        for index, device in enumerate(device_list):

            print(
                f"[{index}] "
                f"{device['name']} | "
                f"IN={device['max_input_channels']} | "
                f"OUT={device['max_output_channels']} | "
                f"SR={int(device['default_samplerate'])}"
            )

            input_channels = device["max_input_channels"]
            output_channels = device["max_output_channels"]

            if input_channels == 0 and output_channels == 0:
                continue

            device_type = (
                "USB"
                if "USB" in device["name"].upper()
                else "Unknown"
            )

            audio_device = AudioDevice(
                id=index,
                name=device["name"],
                type=device_type,
                input_channels=input_channels,
                output_channels=output_channels,
                sample_rate=int(device["default_samplerate"]),
                default_input=(index == default_input),
                default_output=(index == default_output),
            )

            devices.append(audio_device)

        print(f"\nReturned {len(devices)} usable device(s)")
        print("===================================\n")

        return devices