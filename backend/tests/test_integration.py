from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CBIE System is Online", "status": "active"}

def test_predict_intent_pricing():
    payload = {
        "session_id": "test_session_123",
        "message": "How much does the premium plan cost?"
    }
    response = client.post("/api/v1/predict_intent", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] == "pricing_inquiry"
    assert data["confidence"] > 0.5

def test_predict_intent_buy():
    payload = {
        "session_id": "test_session_124",
        "message": "I want to buy this now."
    }
    response = client.post("/api/v1/predict_intent", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] == "ready_to_buy"

def test_predict_sentiment_negative():
    payload = {
        "message": "This service is really bad and slow."
    }
    response = client.post("/api/v1/predict_sentiment", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "negative"
    assert data["tone"] == "frustrated"

def test_recommendations():
    payload = {
        "user_id": "test_user@example.com",
        "limit": 3
    }
    response = client.post("/api/v1/recommend", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["recommendations"]) > 0
    assert data["recommendations"][0]["product_id"] == "p1"
