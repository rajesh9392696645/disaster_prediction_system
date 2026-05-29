# ai_models/cnn_model.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    BatchNormalization
)
from tensorflow.keras.optimizers import Adam


class CNNDisasterModel:

    def __init__(
        self,
        image_size=(128, 128, 3),
        num_classes=4,
        learning_rate=0.001
    ):

        self.image_size = image_size
        self.num_classes = num_classes
        self.learning_rate = learning_rate

        self.model = self.build_model()

    def build_model(self):

        model = Sequential()

        # First Convolution Layer
        model.add(
            Conv2D(
                32,
                (3, 3),
                activation='relu',
                input_shape=self.image_size
            )
        )

        model.add(BatchNormalization())

        model.add(
            MaxPooling2D(pool_size=(2, 2))
        )

        # Second Convolution Layer
        model.add(
            Conv2D(
                64,
                (3, 3),
                activation='relu'
            )
        )

        model.add(BatchNormalization())

        model.add(
            MaxPooling2D(pool_size=(2, 2))
        )

        # Third Convolution Layer
        model.add(
            Conv2D(
                128,
                (3, 3),
                activation='relu'
            )
        )

        model.add(BatchNormalization())

        model.add(
            MaxPooling2D(pool_size=(2, 2))
        )

        # Flatten Layer
        model.add(Flatten())

        # Fully Connected Layers
        model.add(Dense(256, activation='relu'))

        model.add(Dropout(0.5))

        model.add(Dense(128, activation='relu'))

        model.add(Dropout(0.3))

        # Output Layer
        model.add(
            Dense(
                self.num_classes,
                activation='softmax'
            )
        )

        model.compile(
            optimizer=Adam(
                learning_rate=self.learning_rate
            ),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        return model

    def summary(self):

        return self.model.summary()

    def train(
        self,
        train_data,
        validation_data,
        epochs=20
    ):

        history = self.model.fit(
            train_data,
            validation_data=validation_data,
            epochs=epochs
        )

        return history

    def predict(self, image):

        prediction = self.model.predict(image)

        return prediction

    def save_model(self, path):

        self.model.save(path)

    def load_weights(self, path):

        self.model.load_weights(path)