import sounddevice
import torch
import sounddevice as sd
import soundfile as sf
import time
from scipy.io.wavfile import write

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'
put_accent = True
put_yo = True
device = torch.device('cpu')
text = "Тестовый текст для проверки синтеза голоса."

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)

def speak(text: str):
    audio = model.apply_tts(text=text+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    audio_np = audio.cpu().numpy()
    write("greetings.wav", sample_rate, (audio_np * 32767).astype('int16'))
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

def speak_phrase(phrase: str):
    file = phrase + ".wav"
    data, fs = sf.read("audio_files/"+file, dtype='float32')
    sd.play(data,fs)
    status = sd.wait()

def record_phrase(phrase, filename):
    text = phrase
    audio = model.apply_tts(text=text + "..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    audio_np = audio.cpu().numpy()
    write(f"{filename}.wav", sample_rate, (audio_np * 32767).astype('int16'))
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

if __name__ == "__main__":
    record_phrase(phrase="На вашем компьютере не найдено данного приложения", filename="no_app")