import json
import tensorflow as tf
import numpy as np
import os
from ..settings.get_data import GetData
from django.core.cache import cache

TRAINNED_MODEL = GetData.trainnedModel()
INTENTS = GetData.intents()
class LoadModel:
    def __init__(self):
        self.training_labels = []
        self.labels = []
        # Auto execution des fonctions de chargement du model
        self.loadDataFromCache()
        self.loadDataFromCacheOrFile()
        
        self.tokenizer
        self.num_classes
        self.max_sequence_len
        self.sequences
        self.model
        self.data
       
        
    def loadDataFromCache(self):
        # Charger les données d'entraînement à partir du cache ou du fichier
        training_data_key = 'training_data'

        if training_data_key not in cache:
            with open(INTENTS, encoding='utf8') as file:
                self.data = json.load(file)

            # Prétraitement des données
            training_sentences = []
            responses = []

            label_ids = {}
            label_id = 0

            for intent in self.data['intents']:
                for pattern in intent['patterns']:
                    training_sentences.append(pattern)
                    if intent['tag'] not in label_ids:
                        label_ids[intent['tag']] = label_id
                        label_id += 1
                    self.training_labels.append(label_ids[intent['tag']])

                if intent['tag'] not in self.labels:
                    self.labels.append(intent['tag'])
                if 'responses' in intent:
                    responses.append(intent['responses'])

            self.num_classes = len(self.labels)

            # Créer les vecteurs d'entraînement
            self.tokenizer = tf.keras.preprocessing.text.Tokenizer()
            self.tokenizer.fit_on_texts(training_sentences)
            self.tokenizer.num_words = 1000  # Remplacez 1000 par le nombre maximum de mots/vocabulaire souhaité
            self.sequences = self.tokenizer.texts_to_sequences(training_sentences)
            self.max_sequence_len = max([len(x) for x in self.sequences])
            self.sequences = np.array(tf.keras.preprocessing.sequence.pad_sequences(self.sequences, maxlen=self.max_sequence_len))

            # Créer les vecteurs de sortie
            self.training_labels = np.array(self.training_labels)
            self.training_labels = tf.keras.utils.to_categorical(self.training_labels, num_classes=self.num_classes)

            # Mettre les données d'entraînement en cache
            cache.set(training_data_key, (self.sequences, self.training_labels), None)

        else:
            # Récupérer les données d'entraînement depuis le cache
            self.sequences, self.training_labels = cache.get(training_data_key)


    def loadDataFromCacheOrFile(self):
        # Charger le modèle à partir du cache ou du fichier
        model_key = 'chatbox_model'
        if model_key not in cache:
            # Créer le modèle de chatbox et l'entraîner
            self.model = tf.keras.models.Sequential([
                tf.keras.layers.Embedding(self.tokenizer.num_words + 1, 128, input_length=self.max_sequence_len),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256, return_sequences=True)),  # Augmentation du nombre d'unités LSTM
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.LSTM(128),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dense(self.num_classes, activation='softmax')
            ])


            self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
            self.model.summary()

            # Entraîner le modèle
            self.model.fit(self.sequences, self.training_labels, epochs=100, verbose=1)

            # Enregistrer le modèle entraîné
            self.model.save(TRAINNED_MODEL)

            # Mettre le modèle en cache
            cache.set(model_key, self.model, None)

        else:
            # Récupérer le modèle depuis le cache
            self.model = cache.get(model_key)
    
    def _get_tokenizer(self):
        return self.tokenizer
    
    def _get_max_sequence_len(self)->int:
        return self.max_sequence_len
    
    def _get_model(self):
        return self.model
    
    def _get_labels(self)->list:
        return self.labels
    
    def _get_data(self)->any:
        return self.data
    
    def _as_dict(self)->dict[str,any]:
        return {
            "tokenizer":self.tokenizer,
            "max_sequence_len":self.max_sequence_len,
            "model":self.model,
            "labels":self.labels,
            "data":self.data
        }