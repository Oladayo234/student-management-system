import unittest

from student_management_system.Student import Student
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            name="John Doe",
            age=20,
            gender="male",
            email="johndoe@example.com",
            phone_number="08130556161"
        )

    def test_that_student_name_exists(self):
        self.assertEqual(self.student.get_name(), "John Doe")

    def test_that_name_is_not_empty(self):
        with self.assertRaises(ValueError):
            self.student.set_name("")

    def test_that_student_age_exists(self):
        self.assertEqual(self.student.get_age(), 20)
        self.student.set_age(18)
        self.assertEqual(self.student.get_age(), 18)

    def test_that_student_age_is_not_negative(self):
        with self.assertRaises(ValueError):
            self.student.set_age(-1)

    def test_that_student_age_is_not_above_60(self):
        with self.assertRaises(ValueError):
            self.student.set_age(65)

    def test_that_student_gender(self):
        self.assertEqual(self.student.get_gender(), "male")
        self.student.set_gender("female")
        self.assertEqual(self.student.get_gender(), "female")

    def test_that_gender_is_either_male_or_female(self):
        with self.assertRaises(ValueError):
            self.student.set_gender("she")

    def test_that_student_email(self):
        self.student.set_email("oladayoolubunmi@gmail.com")
        self.assertEqual(self.student.get_email(), "oladayoolubunmi@gmail.com")

    def test_email_with_wrong_email(self):
        with self.assertRaises(ValueError):
            self.student.set_email("@mail.example.com")

    def test_that_student_phone_number(self):
        self.student.set_phone_number("08130556161")
        self.assertEqual(self.student.get_phone_number(), "08130556161")

    def test_phone_too_long(self):
        with self.assertRaises(ValueError):
            self.student.set_phone_number("080123456789")

    def test_phone_too_short(self):
        with self.assertRaises(ValueError):
            self.student.set_phone_number("080123456")


if __name__ == '__main__':
    unittest.main()
