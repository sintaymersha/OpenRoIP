from app.audio.audio_manager import AudioManager


audio = AudioManager()

audio.initialize()

print(audio.get_devices())
