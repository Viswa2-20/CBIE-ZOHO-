# Deployment Guide 🚀

## 1. Database (MongoDB Atlas)
1.  Create a free account on [MongoDB Atlas](https://www.mongodb.com/atlas).
2.  Create a new Cluster (Shared Tier M0 is free).
3.  Create a Database User (username/password).
4.  Get the **Connection String** (e.g., `mongodb+srv://<user>:<password>@cluster0.mongodb.net/`).
5.  Save this string for the Backend configuration.

## 2. Backend (Render.com)
We recommend Render for easy Python deployment.

1.  Push this repository to GitHub.
2.  Log in to [Render](https://render.com).
3.  Click **New +** -> **Web Service**.
4.  Connect your GitHub repo.
5.  Settings:
    - **Runtime**: Python 3
    - **Build Command**: `pip install -r backend/requirements.txt`
    - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port 10000`
6.  **Environment Variables**:
    - Add `MONGODB_URL`: Paste your Atlas connection string.
    - Add `DATABASE_NAME`: `cbie_db`
7.  Click **Create Web Service**.
8.  Copy the **Service URL** (e.g., `https://cbie-backend.onrender.com`).

## 3. Zoho SalesIQ Configuration
1.  Go to your Zoho SalesIQ Dashboard -> Settings -> Zobot.
2.  Edit your bot.
3.  Open the `invoke_cbie_backend` function.
4.  Update the `backend_url` variable:
    ```deluge
    backend_url = "https://cbie-backend.onrender.com/api/v1" + endpoint;
    ```
5.  **Publish** the bot.

## 4. Verification
1.  Open your website where SalesIQ is installed.
2.  Type "I want to buy".
3.  Check the Render logs to see the `/predict_intent` call.
4.  Verify the bot responds with the product carousel.
