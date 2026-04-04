from pydantic import BaseModel

class GradeAssignRequest(BaseModel):
    grade: str