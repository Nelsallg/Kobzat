import tensorflow as tf
import numpy as np
from .model.load import LoadModel

# Définir une variable pour stocker le modèle chargé
loaded_model = None
load_model = None

# Fonction pour charger le modèle si ce n'est pas déjà fait
def load_chatbot_model():
    global loaded_model
    if loaded_model is None:
        load_model = LoadModel()
    return load_model

# On charge le modèle et récupère les données nécessaires
loaded_model = load_chatbot_model()
model = loaded_model.getModel()
tokenizer = loaded_model.getTokenizer()
max_sequence_len = loaded_model.getMaxSequenceLen()
labels = loaded_model.getLabels()
data = loaded_model.getData()

# Fonction pour prédire la classe d'une phrase donnée
def predict_class(sentence):
    sequence = tokenizer.texts_to_sequences([sentence])
    sequence = np.array(tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=max_sequence_len))
    predicted_probs = model.predict(sequence)[0]
    predicted_class = labels[np.argmax(predicted_probs)]
    return predicted_class

# Fonction pour obtenir une réponse aléatoire en fonction de la classe prédite
def get_response(intent):
    intent_tag = intent.lower()
    for intent_data in data['intents']:
        if intent_tag == intent_data['tag'].lower():
            return np.random.choice(intent_data['responses'])
    return "Désolé, je n'ai pas compris. Pouvez-vous reformuler votre question ?"
