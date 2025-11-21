# API Documentation 📡

Base URL: `/api/v1`

## Endpoints

### 1. Predict Intent
**POST** `/predict_intent`

Analyzes the user's message and session context to determine their intent.

**Request Body:**
```json
{
  "session_id": "string",
  "message": "string",
  "user_id": "string (optional)",
  "metadata": {}
}
```

**Response:**
```json
{
  "intent": "ready_to_buy | researching | support_needed | pricing_inquiry",
  "confidence": 0.95,
  "suggested_reply": "string (optional)"
}
```

### 2. Predict Sentiment
**POST** `/predict_sentiment`

Analyzes the emotional tone of the message.

**Request Body:**
```json
{
  "message": "string"
}
```

**Response:**
```json
{
  "sentiment": "positive | negative | neutral",
  "score": 0.8,
  "tone": "excited | frustrated | calm"
}
```

### 3. Get Recommendations
**POST** `/recommend`

Returns product recommendations based on user profile and behavior.

**Request Body:**
```json
{
  "user_id": "string",
  "limit": 3
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "product_id": "string",
      "name": "string",
      "url": "string",
      "price": 99.99,
      "score": 0.9
    }
  ]
}
```

### 4. Log Event
**POST** `/log_event`

Logs user behavioral events (clicks, scrolls) for the ML model.

**Request Body:**
```json
{
  "session_id": "string",
  "event_type": "click | scroll | view",
  "event_data": {}
}
```
