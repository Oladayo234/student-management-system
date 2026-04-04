from pydantic import BaseModel

class CourseCreateRequest(BaseModel):
    title: str
    description: str
    facilitator_id: str