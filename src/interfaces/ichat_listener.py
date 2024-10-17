from abc import ABC, abstractmethod

class IChatListener(ABC):
    @abstractmethod
    def monitor_chat(self):
        pass
