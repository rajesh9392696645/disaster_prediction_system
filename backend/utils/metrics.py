# utils/metrics.py

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import numpy as np


class ModelMetrics:

    @staticmethod
    def calculate_accuracy(y_true, y_pred):

        return accuracy_score(y_true, y_pred)

    @staticmethod
    def calculate_precision(y_true, y_pred):

        return precision_score(
            y_true,
            y_pred,
            average='weighted'
        )

    @staticmethod
    def calculate_recall(y_true, y_pred):

        return recall_score(
            y_true,
            y_pred,
            average='weighted'
        )

    @staticmethod
    def calculate_f1_score(y_true, y_pred):

        return f1_score(
            y_true,
            y_pred,
            average='weighted'
        )

    @staticmethod
    def generate_confusion_matrix(
        y_true,
        y_pred
    ):

        return confusion_matrix(
            y_true,
            y_pred
        )

    @staticmethod
    def evaluate_model(
        y_true,
        y_pred
    ):

        metrics = {

            "accuracy":
            ModelMetrics.calculate_accuracy(
                y_true,
                y_pred
            ),

            "precision":
            ModelMetrics.calculate_precision(
                y_true,
                y_pred
            ),

            "recall":
            ModelMetrics.calculate_recall(
                y_true,
                y_pred
            ),

            "f1_score":
            ModelMetrics.calculate_f1_score(
                y_true,
                y_pred
            )
        }

        return metrics