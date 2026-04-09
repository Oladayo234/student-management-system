from pydantic import BaseModel, field_validator

class CourseCreateRequest(BaseModel):
    code: str
    title: str
    description: str
    facilitator_id: str

    @field_validator("title", "description", "code")
    @classmethod
    def must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty or whitespace")
        return value.strip()