from fastapi import APIRouter
from app.schemas.requests.user_create_request import UserCreateRequest
from app.services import admin_service

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/students/{admin_id}")
async def create_student(admin_id: str, request: UserCreateRequest):
    return await admin_service.create_student(admin_id, request)

@router.post("/facilitators/{admin_id}")
async def create_facilitator(admin_id: str, request: UserCreateRequest):
    return await admin_service.create_facilitator(admin_id, request)

@router.delete("/students/{admin_id}/{student_id}")
async def delete_student(admin_id: str, student_id: str):
    return await admin_service.delete_student(admin_id, student_id)

@router.delete("/facilitators/{admin_id}/{facilitator_id}")
async def delete_facilitator(admin_id: str, facilitator_id: str):
    return await admin_service.delete_facilitator(admin_id, facilitator_id)