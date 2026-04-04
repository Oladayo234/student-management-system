from app.repositories import enrollment_repository, user_repository, course_repository
from app.schemas.requests.enrollment_create_request import EnrollmentCreateRequest
from app.schemas.requests.grade_assign_request import GradeAssignRequest
from app.schemas.responses.enrollment_response import EnrollmentResponse
from app.exceptions import UserNotFoundException, CourseNotFoundException, DuplicateEnrollmentException, UnauthorizedRoleException

async def enroll_student(request: EnrollmentCreateRequest):
    student = await user_repository.find_by_id(request.student_id)
    if not student:
        raise UserNotFoundException("Student not found")
    if student["role"] != "student":
        raise UnauthorizedRoleException("User is not a student")

    course = await course_repository.find_by_id(request.course_id)
    if not course:
        raise CourseNotFoundException()

    existing = await enrollment_repository.find_by_student_and_course(
        request.student_id, request.course_id
    )
    if existing:
        raise DuplicateEnrollmentException()

    enrollment = {
        "student_id": request.student_id,
        "course_id": request.course_id,
        "grade": None
    }

    inserted_id = await enrollment_repository.save(enrollment)
    return EnrollmentResponse(
        id=str(inserted_id),
        student_id=request.student_id,
        course_id=request.course_id,
        grade=None
    )

async def get_student_courses(student_id: str):
    enrollments = await enrollment_repository.find_by_student_id(student_id)
    result = []
    for enrollment in enrollments:
        result.append(EnrollmentResponse(
            id=str(enrollment["_id"]),
            student_id=enrollment["student_id"],
            course_id=enrollment["course_id"],
            grade=enrollment.get("grade")
        ))
    return result

async def get_course_students(course_id: str):
    enrollments = await enrollment_repository.find_by_course_id(course_id)
    result = []
    for enrollment in enrollments:
        result.append(EnrollmentResponse(
            id=str(enrollment["_id"]),
            student_id=enrollment["student_id"],
            course_id=enrollment["course_id"],
            grade=enrollment.get("grade")
        ))
    return result

async def assign_grade(enrollment_id: str, request: GradeAssignRequest):
    await enrollment_repository.update_grade(enrollment_id, request.grade)
    return {"message": "Grade assigned successfully"}