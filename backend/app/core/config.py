import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CBIE System"
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "cbie_db")
    API_V1_STR: str = "/api/v1"
    
    # ML Model Paths
    INTENT_MODEL_PATH: str = "ml_engine/artifacts/intent_model.pkl"
    SENTIMENT_MODEL_PATH: str = "ml_engine/artifacts/sentiment_model"
    
    class Config:
        env_file = ".env"

settings = Settings()
