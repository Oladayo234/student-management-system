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