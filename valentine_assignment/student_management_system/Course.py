class Course:
    def __init__(self, course_id: str, course_title: str):
        self.set_course_id(course_id)
        self.set_course_title(course_title)

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id:str):
        if not course_id.strip():
            raise ValueError("Course ID cannot be empty")
        self.__course_id = course_id.strip()

    def get_course_title(self):
        return self.__course_title

    def set_course_title(self, course_title:str):
        if not course_title.strip():
            raise ValueError("Course title cannot be empty")
        self.__course_title = course_title.strip()
