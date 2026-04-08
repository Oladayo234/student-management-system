import inspect

from bson import ObjectId
from app.database import get_db

async def save(user: dict):
    result = get_db()["users"].insert_one(user)
    if inspect.isawaitable(result):
        result = await result
    return result.inserted_id

async def find_by_id(user_id: str):
    result = get_db()["users"].find_one({"_id": ObjectId(user_id)})
    if inspect.isawaitable(result):
        result = await result
    return result

async def find_by_email(email: str):
    result = get_db()["users"].find_one({"email": email})
    if inspect.isawaitable(result):
        result = await result
    return result

async def delete_by_id(user_id: str):
    result = get_db()["users"].delete_one({"_id": ObjectId(user_id)})
    if inspect.isawaitable(result):
        result = await result
    return result

async def update_user(user: dict, user_id: str):
    result = get_db()["users"].update_one({"_id": ObjectId(user_id)},{"$set": user})
    if inspect.isawaitable(result):
        result = await result
    return result