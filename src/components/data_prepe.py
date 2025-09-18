import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from src.config import DataPrepeConfig
import os
import joblib

class DataPreparation:
    def __init__(self, config: DataPrepeConfig):
        self.config = config
        self.scaler = StandardScaler()
        self.encoder = LabelEncoder()

    def prepare_data(self):
        # Load raw data
        df = pd.read_csv(self.config.raw_data)

        # Encode gender
        df["gender"] = self.encoder.fit_transform(df["gender"])

        # Scale age and salary
        df[["age", "salary"]] = self.scaler.fit_transform(df[["age", "salary"]])

        # Ensure processed_data folder exists
        os.makedirs(os.path.dirname(self.config.processed_data), exist_ok=True)

        # Save processed data
        df.to_csv(self.config.processed_data, index=False)


        joblib.dump(self.scaler, self.config.scaler_path)
        joblib.dump(self.encoder, self.config.encoder_path)

        print(f"✅ Data preparation completed. Processed file saved at {self.config.processed_data}")
        return df
