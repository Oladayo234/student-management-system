from pydantic import BaseModel, EmailStr, field_validator
from app.models.role import Role

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    role: Role

    @field_validator("email")
    @classmethod
    def email_must_be_lowercase(cls, value):
        return value.lower()

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty or whitespace")
        return value.strip()