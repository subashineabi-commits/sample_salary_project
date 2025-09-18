from src.config import DataPrepeConfig
from src.components.data_prepe import DataPreparation

if __name__ == "__main__":
    config = DataPrepeConfig()
    preprocessor = DataPreparation(config)
    processed_df = preprocessor.prepare_data()
    print(processed_df.head())
