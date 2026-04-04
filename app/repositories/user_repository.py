from bson import ObjectId
from app.database import db

async def save(user: dict):
    result = await db["users"].insert_one(user)
    return result.inserted_id

async def find_by_id(user_id: str):
    return await db["users"].find_one({"_id": ObjectId(user_id)})

async def find_by_email(email: str):
    return await db["users"].find_one({"email": email})