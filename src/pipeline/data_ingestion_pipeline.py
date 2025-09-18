from src.config import DataIngestionConfig
from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    config = DataIngestionConfig()
    ingestion = DataIngestion(config)
    ingestion.ingest_data()
