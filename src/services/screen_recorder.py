import cv2
import numpy as np
import pyaudio
import wave
import threading
from interfaces.iscreen_recorder import IScreenRecorder

class ScreenRecorder(IScreenRecorder):
    def __init__(self, screen_number=1):
        self.screen_number = screen_number
        self.is_recording = False
        self.frames = []
        self.audio_frames = []
        self.audio_thread = None

    def start_recording(self):
        self.is_recording = True
        self.frames = []
        self.audio_frames = []
        
        # Start audio recording in a separate thread
        self.audio_thread = threading.Thread(target=self.record_audio)
        self.audio_thread.start()

        # Start screen recording
        screen_capture = cv2.VideoCapture(self.screen_number)
        while self.is_recording:
            ret, frame = screen_capture.read()
            if ret:
                self.frames.append(frame)

        screen_capture.release()

    def stop_recording(self):
        self.is_recording = False
        self.audio_thread.join()  # Wait for audio thread to finish
        self.save_recording()

    def record_audio(self):
        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=sample_format, channels=channels, rate=fs, input=True, frames_per_buffer=chunk)

        while self.is_recording:
            data = stream.read(chunk)
            self.audio_frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def save_recording(self):
        # Save video
        video_filename = "recording.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

        for frame in self.frames:
            out.write(frame)

        out.release()

        # Save audio
        audio_filename = "audio.wav"
        wf = wave.open(audio_filename, 'wb')
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.audio_frames))
        wf.close()

        print(f"Grabación guardada: {video_filename} y {audio_filename}")

