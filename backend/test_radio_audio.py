from app.radio.virtual_radio import VirtualRadio


radio = VirtualRadio()

frame = radio.receive_audio()

print(frame.info())
