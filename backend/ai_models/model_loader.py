# ai_models/model_loader.py

import os
from tensorflow.keras.models import load_model


class ModelLoader:

    def __init__(self):

        self.cnn_model = None
        self.lstm_model = None

    def load_cnn_model(self, model_path):

        if os.path.exists(model_path):

            self.cnn_model = load_model(model_path)

            print("CNN Model Loaded Successfully")

            return self.cnn_model

        else:

            raise FileNotFoundError(
                f"CNN model not found at {model_path}"
            )

    def load_lstm_model(self, model_path):

        if os.path.exists(model_path):

            self.lstm_model = load_model(model_path)

            print("LSTM Model Loaded Successfully")

            return self.lstm_model

        else:

            raise FileNotFoundError(
                f"LSTM model not found at {model_path}"
            )

    def predict_disaster_image(self, image):

        if self.cnn_model is None:

            raise Exception(
                "CNN model is not loaded"
            )

        prediction = self.cnn_model.predict(image)

        return prediction

    def predict_weather_forecast(self, sequence_data):

        if self.lstm_model is None:

            raise Exception(
                "LSTM model is not loaded"
            )

        prediction = self.lstm_model.predict(
            sequence_data
        )

        return prediction