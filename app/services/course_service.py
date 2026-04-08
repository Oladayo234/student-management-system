from datetime import datetime
from app.repositories import course_repository
from app.schemas.requests.course_create_request import CourseCreateRequest
from app.schemas.responses.course_response import CourseResponse
from app.exceptions import CourseNotFoundException
from app.utils.validators import validate_user_exists_by_id, validate_user_has_role

async def create_course(request: CourseCreateRequest):
    facilitator = await validate_user_exists_by_id(request.facilitator_id, "Facilitator")
    await validate_user_has_role(facilitator, "facilitator")

    course = request.model_dump()
    course["created_at"] = datetime.now()

    inserted_id = await course_repository.save(course)
    return CourseResponse(
        id=str(inserted_id),
        title=request.title,
        description=request.description,
        facilitator_id=request.facilitator_id,
        created_at=course["created_at"]
    )

async def get_all_courses():
    courses = await course_repository.find_all()
    result = []
    for course in courses:
        result.append(CourseResponse(
            id=str(course["_id"]),
            title=course["title"],
            description=course["description"],
            facilitator_id=course["facilitator_id"],
            created_at=course["created_at"]
        ))
    return result

async def get_course(course_id: str):
    course = await course_repository.find_by_id(course_id)
    if not course:
        raise CourseNotFoundException()
    return CourseResponse(
        id=str(course["_id"]),
        title=course["title"],
        description=course["description"],
        facilitator_id=course["facilitator_id"],
        created_at=course["created_at"]
    )

async def delete_course(course_id: str):
    course = await course_repository.find_by_id(course_id)
    if not course:
        raise CourseNotFoundException()
    await course_repository.delete_by_id(course_id)
    return {"message": "Course deleted successfully"}

async def update_course(course_id: str, request: CourseCreateRequest):
    course = await course_repository.find_by_id(course_id)
    if not course:
        raise CourseNotFoundException()

    updated = request.model_dump()

    await course_repository.edit_course(course_id, updated)
    return CourseResponse(
        id=course_id,
        title=request.title,
        description=request.description,
        facilitator_id=request.facilitator_id,
        created_at=course["created_at"]
    )