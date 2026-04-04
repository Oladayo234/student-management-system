from pydantic import BaseModel
from typing import Optional

class EnrollmentResponse(BaseModel):
    id: str
    student_id: str
    course_id: str
    grade: Optional[str] = None