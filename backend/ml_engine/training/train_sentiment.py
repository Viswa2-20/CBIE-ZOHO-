from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from app.core.config import settings
import os

def save_sentiment_model():
    print("Downloading and saving Sentiment Model (DistilBERT)...")
    model_name = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    save_path = settings.SENTIMENT_MODEL_PATH
    os.makedirs(save_path, exist_ok=True)
    
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)
    
    print(f"Sentiment model saved to {save_path}")

if __name__ == "__main__":
    save_sentiment_model()
