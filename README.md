# Cognitive Buyer Intent Engine (CBIE) 🧠🤖

> **A Production-Ready AI SalesIQ Bot for Zoho Cliqtrix**

CBIE is an advanced AI-driven chatbot system designed for Zoho SalesIQ. It goes beyond simple scripted responses by using Machine Learning to detect buyer intent, sentiment, and behavioral patterns in real-time, delivering hyper-personalized experiences that drive conversions.

## 🚀 Key Features

- **Intent Detection**: Uses XGBoost to classify users as "Ready to Buy", "Researching", "Support Needed", etc.
- **Sentiment Analysis**: Real-time emotion detection (Positive, Negative, Neutral) using DistilBERT.
- **Smart Recommendations**: Hybrid recommender system suggesting products based on user behavior.
- **Dynamic Personality**: The bot adapts its tone (Friendly, Professional, Empathetic) based on user sentiment.
- **Zoho Integration**: Seamlessly integrates with SalesIQ via Deluge and `invokeUrl`.

## 📂 Project Structure

```
cbie_system/
├── backend/                 # Python FastAPI Backend (The Brain)
│   ├── app/                 # API Logic
│   ├── ml_engine/           # Machine Learning Models & Training Scripts
│   └── requirements.txt     # Python Dependencies
├── zoho_deluge/             # Deluge Scripts (The Body)
│   ├── bot_handler.deluge   # Main Zobot Script
│   └── functions/           # Helper Functions
├── docs/                    # Documentation & Guides
└── dashboard/               # Analytics Dashboard Designs
```

## 🛠️ Quick Start

### 1. Backend Setup
1.  Navigate to `backend/`:
    ```bash
    cd backend
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### 2. Zoho SalesIQ Setup
1.  Create a new **Zobot** in SalesIQ.
2.  Choose **Deluge** as the platform.
3.  Copy the content of `zoho_deluge/bot_handler.deluge` into the main handler.
4.  Create a function named `invoke_cbie_backend` and paste the content from `zoho_deluge/functions/invoke_backend.deluge`.
5.  Update the `backend_url` in the function to point to your deployed backend (e.g., on Render/Vercel).

## 🧠 Machine Learning
- **Train Intent Model**: `python backend/ml_engine/training/train_intent.py`
- **Train Recommender**: `python backend/ml_engine/training/train_recommender.py`

## 📊 Dashboard
Check `dashboard/` for analytics mockups and implementation details.

## 📄 License
MIT License. Built for Zoho Cliqtrix Hackathon.
