from bson import ObjectId
from app.database import db

async def save(enrollment: dict):
    result = await db["enrollments"].insert_one(enrollment)
    return result.inserted_id

async def find_by_student_id(student_id: str):
    return await db["enrollments"].find({"student_id": student_id}).to_list(100)

async def find_by_course_id(course_id: str):
    return await db["enrollments"].find({"course_id": course_id}).to_list(100)

async def find_by_student_and_course(student_id: str, course_id: str):
    return await db["enrollments"].find_one({
        "student_id": student_id,
        "course_id": course_id
    })

async def update_grade(enrollment_id: str, grade: str):
    await db["enrollments"].update_one(
        {"_id": ObjectId(enrollment_id)},
        {"$set": {"grade": grade}}
    )