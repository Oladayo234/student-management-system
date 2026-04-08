from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.grade import Grade

class EnrollmentResponse(BaseModel):
    id: str
    student_id: str
    course_id: str
    score: Optional[int] = None
    grade: Optional[Grade] = None
    created_at: datetime