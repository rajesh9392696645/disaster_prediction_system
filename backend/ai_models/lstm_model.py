# ai_models/lstm_model.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    LSTM,
    Dense,
    Dropout
)
from tensorflow.keras.optimizers import Adam


class LSTMDisasterPredictionModel:

    def __init__(
        self,
        input_shape=(100, 1),
        learning_rate=0.001
    ):

        self.input_shape = input_shape
        self.learning_rate = learning_rate

        self.model = self.build_model()

    def build_model(self):

        model = Sequential()

        # First LSTM Layer
        model.add(
            LSTM(
                128,
                return_sequences=True,
                input_shape=self.input_shape
            )
        )

        model.add(Dropout(0.3))

        # Second LSTM Layer
        model.add(
            LSTM(
                64,
                return_sequences=False
            )
        )

        model.add(Dropout(0.3))

        # Dense Layers
        model.add(Dense(32, activation='relu'))

        model.add(Dense(1))

        model.compile(
            optimizer=Adam(
                learning_rate=self.learning_rate
            ),
            loss='mean_squared_error',
            metrics=['mae']
        )

        return model

    def summary(self):

        return self.model.summary()

    def train(
        self,
        X_train,
        y_train,
        epochs=20,
        batch_size=32,
        validation_split=0.2
    ):

        history = self.model.fit(
            X_train,
            y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split
        )

        return history

    def predict(self, data):

        prediction = self.model.predict(data)

        return prediction

    def save_model(self, path):

        self.model.save(path)

    def load_weights(self, path):

        self.model.load_weights(path)