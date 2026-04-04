from typing import Optional

class Enrollment:
    def __init__(self, student_id: str, course_id: str, grade: Optional[str] = None):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__grade = grade