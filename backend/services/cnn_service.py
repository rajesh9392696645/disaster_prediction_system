# services/cnn_service.py

import numpy as np
from tensorflow.keras.preprocessing import image
from ai_models.model_loader import ModelLoader


class CNNService:

    def __init__(self):

        self.loader = ModelLoader()

        self.model = self.loader.load_cnn_model(
            "models/cnn_disaster_model.h5"
        )

        self.class_names = [
            "Flood",
            "Wildfire",
            "Cyclone",
            "Landslide"
        ]

    def preprocess_image(self, image_path):

        img = image.load_img(
            image_path,
            target_size=(128, 128)
        )

        img_array = image.img_to_array(img)

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        img_array = img_array / 255.0

        return img_array

    def predict_disaster(self, image_path):

        processed_image = self.preprocess_image(
            image_path
        )

        prediction = self.model.predict(
            processed_image
        )

        predicted_index = np.argmax(prediction)

        confidence = float(
            np.max(prediction)
        )

        return {

            "prediction":
            self.class_names[predicted_index],

            "confidence":
            round(confidence * 100, 2)
        }