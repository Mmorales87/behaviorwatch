from abc import ABC, abstractmethod

class IReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, insult, user, media_file):
        pass
