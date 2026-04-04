from app.repositories import course_repository, user_repository
from app.schemas.requests.course_create_request import CourseCreateRequest
from app.schemas.responses.course_response import CourseResponse
from app.exceptions import CourseNotFoundException, UserNotFoundException, UnauthorizedRoleException

async def create_course(request: CourseCreateRequest):
    facilitator = await user_repository.find_by_id(request.facilitator_id)
    if not facilitator:
        raise UserNotFoundException("Facilitator not found")
    if facilitator["role"] != "facilitator":
        raise UnauthorizedRoleException("User is not a facilitator")

    course = {
        "title": request.title,
        "description": request.description,
        "facilitator_id": request.facilitator_id
    }

    inserted_id = await course_repository.save(course)
    return CourseResponse(
        id=str(inserted_id),
        title=request.title,
        description=request.description,
        facilitator_id=request.facilitator_id
    )

async def get_all_courses():
    courses = await course_repository.find_all()
    result = []
    for course in courses:
        result.append(CourseResponse(
            id=str(course["_id"]),
            title=course["title"],
            description=course["description"],
            facilitator_id=course["facilitator_id"]
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
        facilitator_id=course["facilitator_id"]
    )