import unittest
from perfect_square import perfect_square

class TestPerfectSquare(unittest.TestCase):

    def test_valid_perfect_number(self):
        self.assertTrue(perfect_square([
                [2, 2],
                [2, 2]
            ])
        )

    def test_invalid_number(self):
        self.assertFalse(perfect_square([
                [1, 2],
                [3, 4]
            ])
        )

    def test_given_example(self):
        self.assertFalse(perfect_square([
                [10, 4, 5],
                [3, 9, 5],
                [6, 4, 1]
            ])
        )

    def test_3_by_3_array(self):
        self.assertTrue(perfect_square([
                [8, 1, 6],
                [3, 5, 7],
                [4, 9, 2]
            ])
        )

    def test_array_not_balanced(self):
        self.assertFalse(perfect_square([
                [1, 2, 3],
                [3, 4]
            ])
        )

    def test_negative_numbers(self):
        self.assertTrue(perfect_square([
                [1, -1],
                [-1, 1]
            ])
        )

    def test_unequal_number(self):
        self.assertFalse(perfect_square([
                [5, 5, 5],
                [1, 1, 1],
                [2, 2, 2]
            ])
        )

if __name__ == "__main__":
    unittest.main()
