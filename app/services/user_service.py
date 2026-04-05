from app.repositories import user_repository
from app.schemas.requests.user_create_request import UserCreateRequest
from app.schemas.responses.user_response import UserResponse
from app.exceptions import UserNotFoundException, DuplicateEmailException
from app.models.student import Student
from app.models.facilitator import Facilitator
from app.models.role import Role

async def create_user(request: UserCreateRequest):
    existing = await user_repository.find_by_email(request.email)
    if existing:
        raise DuplicateEmailException()

    if request.role == Role.STUDENT:
        user = Student(request.name, request.email)
    else:
        user = Facilitator(request.name, request.email)

    user_dict = {
        "name": request.name,
        "email": request.email,
        "role": request.role.value
    }

    inserted_id = await user_repository.save(user_dict)
    return UserResponse(
        id=str(inserted_id),
        name=request.name,
        email=request.email,
        role=request.role
    )

async def get_user(user_id: str):
    user = await user_repository.find_by_id(user_id)
    if not user:
        raise UserNotFoundException()

    return UserResponse(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        role=user["role"]
    )