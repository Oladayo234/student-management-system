from bson import ObjectId
from app.database import get_db
import inspect

async def save(course: dict):
    result = get_db()["courses"].insert_one(course)
    if inspect.isawaitable(result):
        result = await result
    return result.inserted_id

async def find_by_id(course_id: str):
    result = get_db()["courses"].find_one({"_id": ObjectId(course_id)})
    if inspect.isawaitable(result):
        result = await result
    return result

async def find_all():
    cursor = get_db()["courses"].find()
    if hasattr(cursor, 'to_list'):
        return await cursor.to_list(100)
    return list(cursor)