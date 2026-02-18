from student_management_system.Course import Course
from student_management_system.Student import Student

class Enrollment:
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        self.is_enrolled = False
        self.grade = None

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course

    def get_grade(self):
        return self.grade

    def set_grade(self, grade:str):
        valid_grades = ["A", "B", "C", "D", "E", "F"]
        if grade.upper() not in valid_grades:
            raise ValueError("Invalid grade")
        self.grade = grade.upper()