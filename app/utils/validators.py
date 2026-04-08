from app.repositories import user_repository, course_repository, enrollment_repository
from app.exceptions import (UserNotFoundException, CourseNotFoundException, DuplicateEnrollmentException, UnauthorizedRoleException)

async def validate_user_exists_by_id(user_id: str, label: str = "User"):
    user = await user_repository.find_by_id(user_id)
    if not user:
        raise UserNotFoundException(f"{label} not found")
    return user

async def validate_user_has_role(user: dict, expected_role: str):
    if user["role"] != expected_role:
        raise UnauthorizedRoleException(f"User is not a {expected_role}")

async def validate_course_exists_by_id(course_id: str):
    course = await course_repository.find_by_id(course_id)
    if not course:
        raise CourseNotFoundException()
    return course

async def validate_student_not_already_enrolled(student_id: str, course_id: str):
    existing = await enrollment_repository.find_by_student_and_course(
        student_id, course_id
    )
    if existing:
        raise DuplicateEnrollmentException()

async def validate_enroller_has_permission(enroller_id: str, student_id: str):
    enroller = await user_repository.find_by_id(enroller_id)
    if not enroller:
        raise UserNotFoundException("Enroller not found")
    if enroller["role"] not in ["student", "admin"]:
        raise UnauthorizedRoleException("Only students or admins can enroll students")
    if enroller["role"] == "student" and enroller_id != student_id:
        raise UnauthorizedRoleException("Students can only enroll themselves")
    return enroller