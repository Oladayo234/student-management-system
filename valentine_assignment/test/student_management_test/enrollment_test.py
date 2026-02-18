import unittest
from student_management_system.Student import Student
from student_management_system.Course import Course
from student_management_system.Enrollment import Enrollment

class EnrollmentTestCase(unittest.TestCase):

    def setUp(self):
        self.student = Student("John Doe", 20, "male", "john@example.com", "08130556161")
        self.course = Course("CS101", "Introduction to Programming")
        self.enrollment = Enrollment(self.student, self.course)

    def test_enrollment_has_student(self):
        self.assertEqual(self.enrollment.get_student().get_name(), "John Doe")
        self.assertEqual(self.enrollment.get_student(), self.student)

    def test_enrollment_has_course(self):
        self.assertEqual(self.enrollment.get_course().get_course_title(), "Introduction to Programming")
        self.assertEqual(self.enrollment.get_course(), self.course)

    def test_can_set_valid_grade_A(self):
        self.enrollment.set_grade("A")
        self.assertEqual(self.enrollment.get_grade(), "A")

    def test_can_set_valid_grade_B(self):
        self.enrollment.set_grade("B")
        self.assertEqual(self.enrollment.get_grade(), "B")

    def test_can_set_valid_grade_lowercase(self):
        self.enrollment.set_grade("c")
        self.assertEqual(self.enrollment.get_grade(), "C")

    def test_cannot_set_invalid_grade_Z(self):
        with self.assertRaises(ValueError):
            self.enrollment.set_grade("Z")

    def test_cannot_set_invalid_grade_G(self):
        with self.assertRaises(ValueError):
            self.enrollment.set_grade("G")

    def test_cannot_set_empty_grade(self):
        with self.assertRaises(ValueError):
            self.enrollment.set_grade("")

    def test_multiple_enrollments_are_independent(self):
        student2 = Student("Jane Smith", 22, "female", "jane@example.com", "08140556162")
        course2 = Course("CS102", "Data Structures")
        enrollment2 = Enrollment(student2, course2)

        self.assertNotEqual(self.enrollment.get_student(), enrollment2.get_student())
        self.assertNotEqual(self.enrollment.get_course(), enrollment2.get_course())

if __name__ == '__main__':
    unittest.main()