from pydantic import BaseModel, Field

class GradeAssignRequest(BaseModel):
    score: int = Field(ge=0, le=100)