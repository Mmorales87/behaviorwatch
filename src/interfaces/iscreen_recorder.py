from abc import ABC, abstractmethod

class IScreenRecorder(ABC):
    @abstractmethod
    def start_recording(self):
        pass

    @abstractmethod
    def stop_recording(self):
        pass
