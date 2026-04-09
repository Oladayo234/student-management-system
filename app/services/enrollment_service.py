from datetime import datetime
from app.schemas.requests.enrollment_create_request import EnrollmentCreateRequest
from app.schemas.requests.grade_assign_request import GradeAssignRequest
from app.schemas.responses.course_response import CourseResponse
from app.schemas.responses.enrollment_response import EnrollmentResponse
from app.utils.grade_calculator import calculate_grade
from app.utils.validators import*

async def enroll_student(request: EnrollmentCreateRequest):
    student = await validate_user_exists_by_id(request.student_id, "Student")
    await validate_user_has_role(student, "student")
    await validate_enroller_has_permission(request.enrolled_by, request.student_id)
    await validate_course_exists_by_id(request.course_id)
    await validate_student_not_already_enrolled(request.student_id, request.course_id)

    enrollment = request.model_dump()
    enrollment["grade"] = None
    enrollment["score"] = None
    enrollment["created_at"] = datetime.now()

    inserted_id = await enrollment_repository.save(enrollment)
    return EnrollmentResponse(
        id=str(inserted_id),
        student_id=request.student_id,
        course_id=request.course_id,
        score=None,
        grade=None
    )

async def get_courses_by_student_id(student_id: str):
    enrollments = await enrollment_repository.find_by_student_id(student_id)
    result = []
    for enrollment in enrollments:
        course = await course_repository.find_by_id(enrollment["course_id"])
        result.append({
            "enrollment_id": str(enrollment["_id"]),
            "score": enrollment.get("score"),
            "grade": enrollment.get("grade"),
            "course": CourseResponse(
                id=str(course["_id"]),
                code=course["code"],
                title=course["title"],
                description=course["description"],
                facilitator_id=course["facilitator_id"]
            )
        })
    return result


async def get_students_by_course_id(course_id: str):
    enrollments = await enrollment_repository.find_by_course_id(course_id)
    result = []
    for enrollment in enrollments:
        student = await user_repository.find_by_id(enrollment["student_id"])
        result.append({
            "enrollment_id": str(enrollment["_id"]),
            "score": enrollment.get("score"),
            "grade": enrollment.get("grade"),
            "student": {
                "id": str(student["_id"]),
                "name": student["name"],
                "email": student["email"]
            }
        })
    return result

async def assign_grade(enrollment_id: str, request: GradeAssignRequest):
    grade = calculate_grade(request.score)
    await enrollment_repository.update_grade(enrollment_id, request.score, grade.value)
    return {
        "message": "Grade assigned successfully",
        "score": request.score,
        "grade": grade.value
    }