from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import endpoints
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Cognitive Buyer Intent Engine (CBIE)",
    description="AI-driven backend for Zoho SalesIQ integration",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific Zoho domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(endpoints.router, prefix="/api/v1")

from app.services.database import db

@app.on_event("startup")
async def startup_event():
    await db.connect_to_database()

@app.on_event("shutdown")
async def shutdown_event():
    await db.close_database_connection()

@app.get("/")
async def root():
    return {"message": "CBIE System is Online", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
