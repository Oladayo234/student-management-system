from fastapi import APIRouter
from app.schemas.requests.course_create_request import CourseCreateRequest
from app.services import course_service

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/")
async def create_course(request: CourseCreateRequest):
    return await course_service.create_course(request)

@router.get("/")
async def get_all_courses():
    return await course_service.get_all_courses()

@router.get("/{course_id}")
async def get_course(course_id: str):
    return await course_service.get_course(course_id)

@router.delete("/{course_id}/{facilitator_id}")
async def delete_course(course_id: str, facilitator_id: str):
    return await course_service.delete_course(course_id, facilitator_id)

@router.put("/{course_id}/{facilitator_id}")
async def update_course(course_id: str, facilitator_id: str, request: CourseCreateRequest):
    return await course_service.update_course(course_id, facilitator_id, request)