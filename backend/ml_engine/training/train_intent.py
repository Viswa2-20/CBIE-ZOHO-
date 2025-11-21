import pandas as pd
import pickle
import os
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
from app.core.config import settings
from ml_engine.pipelines.preprocessing import TextPreprocessor

# Dummy Dataset for Training
data = [
    ("How much does this cost?", "pricing_inquiry"),
    ("What is the price?", "pricing_inquiry"),
    ("Is there a free trial?", "pricing_inquiry"),
    ("I want to buy this.", "ready_to_buy"),
    ("Can I purchase now?", "ready_to_buy"),
    ("Where is the checkout?", "ready_to_buy"),
    ("I need help with my account.", "support_needed"),
    ("My login is not working.", "support_needed"),
    ("Can I speak to an agent?", "support_needed"),
    ("What does this feature do?", "general_inquiry"),
    ("Tell me more about the product.", "general_inquiry"),
    ("Hello", "greeting"),
    ("Hi there", "greeting")
]

def train_intent_model():
    print("Training Intent Model...")
    df = pd.DataFrame(data, columns=["text", "intent"])
    
    pipeline = Pipeline([
        ("preprocessor", TextPreprocessor()),
        ("tfidf", TfidfVectorizer(max_features=1000)),
        ("clf", XGBClassifier(n_estimators=100, random_state=42))
    ])
    
    # Encode labels
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(df["intent"])
    
    pipeline.fit(df["text"], y)
    
    # Save Model & Encoder
    os.makedirs(os.path.dirname(settings.INTENT_MODEL_PATH), exist_ok=True)
    
    artifacts = {
        "pipeline": pipeline,
        "label_encoder": le
    }
    
    with open(settings.INTENT_MODEL_PATH, "wb") as f:
        pickle.dump(artifacts, f)
        
    print(f"Model saved to {settings.INTENT_MODEL_PATH}")

if __name__ == "__main__":
    # Adjust path for standalone execution
    import sys
    sys.path.append(os.getcwd())
    train_intent_model()
