from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import (
    PredictIntentRequest, IntentResponse,
    PredictSentimentRequest, SentimentResponse,
    RecommendationRequest, RecommendationResponse, ProductItem,
    LogEventRequest
)
from app.services.database import get_database, Database
import logging
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)

# --- ML Inference Placeholders (Will be replaced by actual models) ---
def mock_predict_intent(message: str):
    # Simple keyword matching for demo
    msg = message.lower()
    if "price" in msg or "cost" in msg:
        return "pricing_inquiry", 0.85
    elif "buy" in msg or "purchase" in msg:
        return "ready_to_buy", 0.92
    elif "help" in msg or "support" in msg:
        return "support_needed", 0.88
    else:
        return "general_inquiry", 0.60

def mock_predict_sentiment(message: str):
    # Simple keyword matching for demo
    msg = message.lower()
    if "bad" in msg or "slow" in msg:
        return "negative", 0.75, "frustrated"
    elif "great" in msg or "thanks" in msg:
        return "positive", 0.90, "excited"
    else:
        return "neutral", 0.50, "calm"

# --- Endpoints ---

@router.post("/predict_intent", response_model=IntentResponse)
async def predict_intent(request: PredictIntentRequest, db: Database = Depends(get_database)):
    logger.info(f"Predicting intent for session: {request.session_id}")
    
    intent, confidence = mock_predict_intent(request.message)
    
    # Log to DB (Async)
    if db.db:
        await db.get_collection("intent_logs").insert_one({
            "session_id": request.session_id,
            "message": request.message,
            "intent": intent,
            "confidence": confidence,
            "timestamp": datetime.utcnow()
        })
    
    return IntentResponse(intent=intent, confidence=confidence)

@router.post("/predict_sentiment", response_model=SentimentResponse)
async def predict_sentiment(request: PredictSentimentRequest):
    sentiment, score, tone = mock_predict_sentiment(request.message)
    return SentimentResponse(sentiment=sentiment, score=score, tone=tone)

@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_products(request: RecommendationRequest, db: Database = Depends(get_database)):
    # Mock recommendations
    products = [
        ProductItem(product_id="p1", name="Premium Plan", url="/pricing", price=99.0, score=0.95),
        ProductItem(product_id="p2", name="Enterprise Add-on", url="/enterprise", price=199.0, score=0.88)
    ]
    return RecommendationResponse(recommendations=products)

@router.post("/log_event")
async def log_event(request: LogEventRequest, db: Database = Depends(get_database)):
    if db.db:
        await db.get_collection("behavior_logs").insert_one({
            "session_id": request.session_id,
            "user_id": request.user_id,
            "event_type": request.event_type,
            "event_data": request.event_data,
            "timestamp": datetime.utcnow()
        })
    return {"status": "logged"}
