import json

class InsultList:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
            self.insults = config['insult_words']

    def get_insults(self):
        return self.insults

