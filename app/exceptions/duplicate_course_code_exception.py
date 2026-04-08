

class DuplicateCourseCodeException(Exception):
    def __init__(self, message="Course code already exists"):
        self.message = message
        super().__init__(self.message)