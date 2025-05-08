import vosk
import pyaudio

def check_pronunciation():
    model_path = "./models/vosk-model-small-en-us-0.15"
    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)
    
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    
    print("🎤 Parlez maintenant... (Ctrl+C pour arrêter)")
    try:
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                print(f"Vous avez dit: {text[14:-3]}")  # Extrait le texte
    except KeyboardInterrupt:
        stream.stop_stream()
        stream.close()
