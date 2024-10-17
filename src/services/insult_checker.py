from interfaces.iinsult_checker import IInsultChecker
from models.insult_list import InsultList

class InsultChecker(IInsultChecker):
    def __init__(self, config_file):
        self.insult_list = InsultList(config_file).get_insults()

    def check_insult(self, text):
        return any(insult in text for insult in self.insult_list)

