from pydantic import BaseModel, field_validator

class EnrollmentCreateRequest(BaseModel):
    student_id: str
    course_id: str
    enrolled_by: str

    @field_validator("student_id", "course_id", "enrolled_by")
    @classmethod
    def must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty or whitespace")
        return value.strip()