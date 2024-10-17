import pyaudio
import wave
import json
from interfaces.iaudio_listener import IAudioListener
from models.insult_list import InsultList

class AudioListener(IAudioListener):
    def __init__(self, config_file):
        self.insult_list = InsultList(config_file).get_insults()
        self.is_listening = False
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100
        self.p = pyaudio.PyAudio()

    def listen_to_audio(self):
        self.is_listening = True
        print("Escuchando audio...")
        stream = self.p.open(format=self.sample_format,
                              channels=self.channels,
                              rate=self.fs,
                              frames_per_buffer=self.chunk,
                              input=True)

        frames = []

        while self.is_listening:
            data = stream.read(self.chunk)
            frames.append(data)
            # Aquí puedes agregar la lógica para procesar el audio y detectar insultos

        stream.stop_stream()
        stream.close()
        self.p.terminate()

    def stop(self):
        self.is_listening = False
        print("Deteniendo la escucha de audio.")

