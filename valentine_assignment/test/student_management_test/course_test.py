import unittest
from student_management_system.Course import Course

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.course = Course(
            course_id="CS101",
            course_title="Introduction to Programming"
        )

    def test_course_id_exists(self):
        self.assertEqual(self.course.get_course_id(), "CS101")

    def test_course_id_can_be_updated(self):
        self.course.set_course_id("CS102")
        self.assertEqual(self.course.get_course_id(), "CS102")

    def test_course_id_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            self.course.set_course_id("")

    def test_course_id_strips_whitespace(self):
        self.course.set_course_id("  CS103  ")
        self.assertEqual(self.course.get_course_id(), "CS103")

    def test_course_title_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            self.course.set_course_title("")

    def test_course_title_strips_whitespace(self):
        self.course.set_course_title("  Data Structures  ")
        self.assertEqual(self.course.get_course_title(), "Data Structures")



if __name__ == '__main__':
    unittest.main()
