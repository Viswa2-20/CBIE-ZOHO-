from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_database(self):
        logger.info("Connecting to MongoDB...")
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.DATABASE_NAME]
        logger.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logger.info("Closing MongoDB connection...")
        if self.client:
            self.client.close()
        logger.info("MongoDB connection closed.")

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

db = Database()

# Dependency to get DB instance
async def get_database():
    return db
