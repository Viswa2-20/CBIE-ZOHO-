import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle
import os

def train_recommender_system():
    print("Training Recommender System...")
    
    # Dummy Product Catalog
    products = pd.DataFrame([
        {"id": "p1", "name": "Basic Plan", "desc": "Starter plan for small teams"},
        {"id": "p2", "name": "Pro Plan", "desc": "Advanced features for growing business"},
        {"id": "p3", "name": "Enterprise", "desc": "Full control and support"},
        {"id": "p4", "name": "Consulting", "desc": "Expert advice and implementation"}
    ])
    
    # Content-Based Filtering (TF-IDF)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(products['desc'])
    
    # Compute Cosine Similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    save_path = "ml_engine/artifacts/recommender_model.pkl"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with open(save_path, "wb") as f:
        pickle.dump({
            "tfidf_matrix": tfidf_matrix,
            "cosine_sim": cosine_sim,
            "products": products
        }, f)
        
    print(f"Recommender model saved to {save_path}")

if __name__ == "__main__":
    train_recommender_system()
