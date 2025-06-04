import sounddevice as sd
from scipy.io.wavfile import write
import whisper

def record_audio(filename="output.wav", duration=5, fs=44100):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Audio recorded and saved as", filename)

def transcribe_with_whisper(filename="output.wav"):
    print("Transcribing with Whisper...")
    model = whisper.load_model("tiny")  
    result = model.transcribe(filename)
    return result["text"]

if __name__ == "__main__":
    record_audio()
    text = transcribe_with_whisper()
    print("Transcription:", text)