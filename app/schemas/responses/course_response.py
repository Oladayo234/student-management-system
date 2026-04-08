from pydantic import BaseModel

class CourseResponse(BaseModel):
    id: str
    code: str
    title: str
    description: str
    facilitator_id: str