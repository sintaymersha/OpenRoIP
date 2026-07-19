from app.audio.audio_discovery import AudioDiscovery


discovery = AudioDiscovery()

devices = discovery.discover()

print("Detected Audio Devices:")

for device in devices:
    print(device.to_dict())
