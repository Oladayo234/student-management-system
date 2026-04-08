from fastapi import APIRouter
from app.schemas.requests.enrollment_create_request import EnrollmentCreateRequest
from app.schemas.requests.grade_assign_request import GradeAssignRequest
from app.services import enrollment_service

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/")
async def enroll_student(request: EnrollmentCreateRequest):
    return await enrollment_service.enroll_student(request)

@router.get("/student/{student_id}")
async def get_courses_by_student(student_id: str):
    return await enrollment_service.get_courses_by_student_id(student_id)

@router.get("/course/{course_id}")
async def get_students_by_course(course_id: str):
    return await enrollment_service.get_students_by_course_id(course_id)

@router.patch("/{enrollment_id}/grade")
async def assign_grade(enrollment_id: str, request: GradeAssignRequest):
    return await enrollment_service.assign_grade(enrollment_id, request)