from pydantic import BaseModel

class EnrollmentCreateRequest(BaseModel):
    student_id: str
    course_id: str
    enrolled_by: str