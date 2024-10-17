from abc import ABC, abstractmethod

class IInsultChecker(ABC):
    @abstractmethod
    def check_insult(self, text):
        pass
