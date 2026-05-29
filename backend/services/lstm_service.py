# services/lstm_service.py

import numpy as np
from ai_models.model_loader import ModelLoader


class LSTMService:

    def __init__(self):

        self.loader = ModelLoader()

        self.model = self.loader.load_lstm_model(
            "models/lstm_weather_model.h5"
        )

    def predict_weather_risk(
        self,
        sequence_data
    ):

        sequence_data = np.array(
            sequence_data
        )

        sequence_data = sequence_data.reshape(
            (1, len(sequence_data), 1)
        )

        prediction = self.model.predict(
            sequence_data
        )

        risk_probability = float(
            prediction[0][0]
        )

        return {

            "risk_probability":
            round(risk_probability, 2),

            "risk_level":
            self.get_risk_level(
                risk_probability
            )
        }

    def get_risk_level(self, probability):

        if probability >= 0.8:

            return "HIGH"

        elif probability >= 0.5:

            return "MEDIUM"

        return "LOW"