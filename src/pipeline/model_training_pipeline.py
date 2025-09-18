from src.config import ModelTrainingConfig
from src.components.model_training import ModelTrainer

if __name__ == "__main__":
    

    config = ModelTrainingConfig()
    
    trainer = ModelTrainer(config)
   
    model = trainer.train()
    
