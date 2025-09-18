import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from src.config import ModelTrainingConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.model = LinearRegression()

    def train(self):
        # Load processed data
        df = pd.read_csv(self.config.processed_data)

        # Features and target
        X = df[["age", "gender"]]   # input features
        y = df["salary"]            # target variable

        # Train model
        self.model.fit(X, y)

        # Save model
        joblib.dump(self.model, self.config.model_path)
        print(f"✅ Model training completed. Model saved at {self.config.model_path}")

        return self.model
