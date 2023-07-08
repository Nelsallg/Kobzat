from settings.get_files import GetFiles


class Trainning:
    def __init__(self):
        self.training_sentences = []
        self.training_labels = []
        self.labels = []
        self.responses = []

        self.label_ids = {}
        self.label_id = 0

        self.file = GetFiles('intents.json')
        self.data = self.file.get_data()

    def train(self):
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                self.training_sentences.append(pattern)
                if intent['tag'] not in self.label_ids:
                    self.label_ids[intent['tag']] = self.label_id
                    self.label_id += 1
                self.training_labels.append(self.label_ids[intent['tag']])

            if intent['tag'] not in self.labels:
                self.labels.append(intent['tag'])
            if 'responses' in intent:
                self.responses.append(intent['responses'])
        print(
            f"trs:${self.training_sentences}\ntrl:${self.training_labels}\nlabels:${self.labels}\nresponses:${self.response}")
