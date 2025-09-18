import os
import shutil
from src.config import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def ingest_data(self):
        """Copy data from source to raw_data folder"""
        source_path = self.config.source_data
        raw_path = self.config.raw_data

        os.makedirs(os.path.dirname(raw_path), exist_ok=True)

        shutil.copy(source_path, raw_path)
        print(f"✅ Data copied from {source_path} to {raw_path}")
