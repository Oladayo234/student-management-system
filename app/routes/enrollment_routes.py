from fastapi import APIRouter
from app.schemas.requests.enrollment_create_request import EnrollmentCreateRequest
from app.schemas.requests.grade_assign_request import GradeAssignRequest
from app.services import enrollment_service

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/")
async def enroll_student(request: EnrollmentCreateRequest):
    return await enrollment_service.enroll_student(request)

@router.get("/student/{student_id}")
async def get_student_courses(student_id: str):
    return await enrollment_service.get_student_by_courses(student_id)

@router.get("/course/{course_id}")
async def get_course_students(course_id: str):
    return await enrollment_service.get_course_by_students(course_id)

@router.patch("/{enrollment_id}/grade")
async def assign_grade(enrollment_id: str, request: GradeAssignRequest):
    return await enrollment_service.assign_grade(enrollment_id, request)