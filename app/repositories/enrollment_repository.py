from bson import ObjectId
from app.database import get_db
import inspect

from app.schemas.requests.grade_assign_request import GradeAssignRequest
from app.utils.grade_calculator import calculate_grade

async def save(enrollment: dict):
    result = get_db()["enrollments"].insert_one(enrollment)
    if inspect.isawaitable(result):
        result = await result
    return result.inserted_id

async def find_by_student_id(student_id: str):
    cursor = get_db()["enrollments"].find({"student_id": student_id})
    if hasattr(cursor, 'to_list'):
        return await cursor.to_list(100)
    return list(cursor)

async def find_by_course_id(course_id: str):
    cursor = get_db()["enrollments"].find({"course_id": course_id})
    if hasattr(cursor, 'to_list'):
        return await cursor.to_list(100)
    return list(cursor)

async def find_by_student_and_course(student_id: str, course_id: str):
    result = get_db()["enrollments"].find_one({
        "student_id": student_id,
        "course_id": course_id
    })
    if inspect.isawaitable(result):
        result = await result
    return result

async def update_grade(enrollment_id: str, score: int, grade: str):
    result = get_db()["enrollments"].update_one(
        {"_id": ObjectId(enrollment_id)},
        {"$set": {"score": score, "grade": grade}}
    )
    if inspect.isawaitable(result):
        result = await result
    return result