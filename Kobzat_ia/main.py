import os
import json
import tensorflow as tf
import numpy as np
from django.conf import settings
import pprint
from .model.load import LoadModel

MODEL_DATA_DIR = os.path.join(settings.BASE_DIR, 'Kobzat_ia/model_data')
loaded_model = None

# Fonction pour charger le modèle si ce n'est pas déjà fait
def load_chatbot_model():
    global loaded_model
    if loaded_model is None:
        loaded_model = LoadModel()
    return loaded_model

# On charge le modèle et récupère les données nécessaires
model_data_path = os.path.join(MODEL_DATA_DIR, 'model_data.json')
if not os.path.exists(model_data_path):
    # Charger les données du modèle à partir du fichier
    with open(model_data_path, 'r') as file:
        model_data = json.load(file)

    model = tf.keras.models.model_from_json(model_data['model_json'])
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(model_data['tokenizer_json'])
    max_sequence_len = model_data['max_sequence_len']
    labels = model_data['labels']
    data = model_data['data']
else:
    # Les données du modèle n'existent pas, les créer et les sauvegarder
    loaded_model = load_chatbot_model()
    model = loaded_model._get_model()
    tokenizer = loaded_model._get_tokenizer()
    max_sequence_len = loaded_model._get_max_sequence_len()
    labels = loaded_model._get_labels()
    data = loaded_model._get_data()

    # Sauvegarder les données du modèle dans un fichier
    model_data = {
        'model_json': model.to_json(),
        'tokenizer_json': tokenizer.to_json(),
        'max_sequence_len': max_sequence_len,
        'labels': labels,
        'data': data
    }

    os.makedirs(MODEL_DATA_DIR, exist_ok=True)
    with open(model_data_path, 'w') as file:
        json.dump(model_data, file)



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
