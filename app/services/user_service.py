from app.repositories import user_repository
from app.schemas.requests.user_create_request import UserCreateRequest
from app.schemas.responses.user_response import UserResponse
from app.exceptions import UserNotFoundException, DuplicateEmailException

async def create_user(request: UserCreateRequest):
    existing = await user_repository.find_by_email(request.email)
    if existing:
        raise DuplicateEmailException()

    user = {
        "name": request.name,
        "email": request.email,
        "role": request.role.value
    }

    inserted_id = await user_repository.save(user)
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