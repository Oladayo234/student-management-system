from pydantic import BaseModel
from app.models.grade import Grade

class GradeAssignRequest(BaseModel):
    grade: Grade