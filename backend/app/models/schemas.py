from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

# --- Shared Models ---

class UserProfile(BaseModel):
    user_id: str
    name: Optional[str] = None
    email: Optional[str] = None
    segments: List[str] = []
    last_active: datetime = Field(default_factory=datetime.now)

# --- Input Models ---

class PredictIntentRequest(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    message: str
    page_url: Optional[str] = None
    metadata: Dict[str, Any] = {}

class PredictSentimentRequest(BaseModel):
    message: str

class RecommendationRequest(BaseModel):
    user_id: str
    current_page: Optional[str] = None
    limit: int = 5

class LogEventRequest(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    event_type: str  # e.g., "page_view", "click", "scroll"
    event_data: Dict[str, Any]

# --- Output Models ---

class IntentResponse(BaseModel):
    intent: str
    confidence: float
    suggested_reply: Optional[str] = None

class SentimentResponse(BaseModel):
    sentiment: str  # e.g., "positive", "negative", "neutral"
    score: float
    tone: Optional[str] = None # e.g., "angry", "excited"

class ProductItem(BaseModel):
    product_id: str
    name: str
    url: str
    image_url: Optional[str] = None
    price: Optional[float] = None
    score: Optional[float] = None

class RecommendationResponse(BaseModel):
    recommendations: List[ProductItem]
