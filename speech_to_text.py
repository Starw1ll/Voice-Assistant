import vosk
import sys
import sounddevice as sd
import queue
import json
from pycparser.c_ast import While

model = vosk.Model("model-small")
samplerate = 16000
device = 1

q = queue.Queue()

def respond(voice: str):
    print(voice)


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])

if __name__ == "__main__":
    while True:
        listen(respond)