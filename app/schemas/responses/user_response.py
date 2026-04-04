from pydantic import BaseModel
from app.models.role import Role

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: Role