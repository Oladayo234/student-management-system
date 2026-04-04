from pydantic import BaseModel, EmailStr
from app.models.role import Role

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    role: Role