from datetime import datetime
from app.repositories import user_repository
from app.models.admin import Admin
from app.models.student import Student
from app.models.facilitator import Facilitator
from app.models.role import Role
from app.schemas.requests.user_create_request import UserCreateRequest
from app.schemas.responses.user_response import UserResponse
from app.exceptions import (UserNotFoundException, DuplicateEmailException, UnauthorizedRoleException)
from app.utils.validators import validate_user_exists_by_id, validate_user_has_role

async def create_admin(request: UserCreateRequest):
    existing = await user_repository.find_by_email(request.email)
    if existing:
        raise DuplicateEmailException()

    admin = Admin(request.name, request.email)
    new_admin = request.model_dump()
    new_admin["created_at"] = datetime.now()

    inserted_id = await user_repository.save(new_admin)
    return UserResponse(
        id=str(inserted_id),
        name=request.name,
        email=request.email,
        role=request.role,
        created_at=new_admin["created_at"]
    )

async def create_student(admin_id: str, request: UserCreateRequest):
    admin = await validate_user_exists_by_id(admin_id, "Admin")
    await validate_user_has_role(admin, "admin")

    existing = await user_repository.find_by_email(request.email)
    if existing:
        raise DuplicateEmailException()

    student = Student(request.name, request.email)
    student_dict = request.model_dump()
    student_dict["created_at"] = datetime.now()

    inserted_id = await user_repository.save(student_dict)
    return UserResponse(
        id=str(inserted_id),
        name=request.name,
        email=request.email,
        role=Role.STUDENT,
        created_at=student_dict["created_at"]
    )

async def create_facilitator(admin_id: str, request: UserCreateRequest):
    admin = await validate_user_exists_by_id(admin_id, "Admin")
    await validate_user_has_role(admin, "admin")

    existing = await user_repository.find_by_email(request.email)
    if existing:
        raise DuplicateEmailException()

    facilitator = Facilitator(request.name, request.email)
    facilitator_dict = request.model_dump()
    facilitator_dict["created_at"] = datetime.now()

    inserted_id = await user_repository.save(facilitator_dict)
    return UserResponse(
        id=str(inserted_id),
        name=request.name,
        email=request.email,
        role=Role.FACILITATOR,
        created_at=facilitator_dict["created_at"]
    )

async def delete_student(admin_id: str, student_id: str):
    admin = await validate_user_exists_by_id(admin_id, "Admin")
    await validate_user_has_role(admin, "admin")

    student = await validate_user_exists_by_id(student_id, "Student")
    await validate_user_has_role(student, "student")

    await user_repository.delete_by_id(student_id)
    return {"message": "Student deleted successfully"}

async def delete_facilitator(admin_id: str, facilitator_id: str):
    admin = await validate_user_exists_by_id(admin_id, "Admin")
    await validate_user_has_role(admin, "admin")

    facilitator = await validate_user_exists_by_id(facilitator_id, "Facilitator")
    await validate_user_has_role(facilitator, "facilitator")

    await user_repository.delete_by_id(facilitator_id)
    return {"message": "Facilitator deleted successfully"}