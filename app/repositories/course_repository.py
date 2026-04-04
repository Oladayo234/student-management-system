from bson import ObjectId
from app.database import db

async def save(course: dict):
    result = await db["courses"].insert_one(course)
    return result.inserted_id

async def find_by_id(course_id: str):
    return await db["courses"].find_one({"_id": ObjectId(course_id)})

async def find_all():
    return await db["courses"].find().to_list(100)