from abc import ABC, abstractmethod

class IAudioListener(ABC):
    @abstractmethod
    def listen_to_audio(self):
        pass
