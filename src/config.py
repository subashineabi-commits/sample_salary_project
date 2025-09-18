import os

class DataIngestionConfig:
    def __init__(self):
        # project root is one level above src
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.source_data = os.path.join(self.root_dir, "data", "source", "data.csv")
        self.raw_data = os.path.join(self.root_dir, "data", "raw_data", "raw.csv")
     
class DataPrepeConfig:
    def __init__(self):
        # project root is one level above src
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.raw_data = os.path.join(self.root_dir, "data", "raw_data", "raw.csv")
        self.processed_data = os.path.join(self.root_dir, "data", "processed_data", "processed_data.csv")




        # Artifacts (models, encoders, scalers, etc.)
        self.artifacts_dir = os.path.join(self.root_dir, "artifacts")
        os.makedirs(self.artifacts_dir, exist_ok=True)

        self.scaler_path = os.path.join(self.artifacts_dir, "scaler.pkl")
        self.encoder_path = os.path.join(self.artifacts_dir, "encoder.pkl")



class ModelTrainingConfig:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Input data
        self.processed_data = os.path.join(self.root_dir, "data", "processed_data", "processed_data.csv")

        # Artifacts (model)
        self.artifacts_dir = os.path.join(self.root_dir, "artifacts")
        os.makedirs(self.artifacts_dir, exist_ok=True)

        self.model_path = os.path.join(self.artifacts_dir, "model.pkl")    