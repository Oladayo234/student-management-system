from fastapi import APIRouter
from app.schemas.requests.user_create_request import UserCreateRequest
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(request: UserCreateRequest):
    return await user_service.create_user(request)

@router.get("/{user_id}")
async def get_user(user_id: str):
    return await user_service.get_user(user_id)