import unittest
from pybank_functions import (validate_email, calculate_balance, is_strong_password, calculate_interest, get_transaction_summary)

class TestYourLogic(unittest.TestCase):

    def test_email_valid(self):
        self.assertTrue(validate_email("test@gmail.com"))

    def test_email_too_short(self):
        self.assertFalse(validate_email("a@b.c"))

    def test_email_no_at_symbol(self):
        self.assertFalse(validate_email("mywebsite.com"))

    def test_email_starts_with_at(self):
        self.assertFalse(validate_email("@gmail.com"))

    def test_email_ends_with_at(self):
        self.assertFalse(validate_email("user@gmail@"))

    def test_email_boundary_length(self):
        self.assertTrue(validate_email("a@cdef.g")) # Exactly 8 chars


    def test_balance_mixed(self):
        self.assertEqual(calculate_balance([10, -5, 10]), 15)

    def test_balance_only_deposits(self):
        self.assertEqual(calculate_balance([100, 200]), 300)

    def test_balance_only_withdrawals(self):
        self.assertEqual(calculate_balance([-50, -25]), -75)

    def test_balance_empty(self):
        self.assertEqual(calculate_balance([]), 0)

    def test_balance_zero(self):
        self.assertEqual(calculate_balance([0, 0]), 0)

    def test_balance_canceling(self):
        self.assertEqual(calculate_balance([100, -100]), 0)
        

    def test_pass_strong(self):
        self.assertEqual(is_strong_password("password123"), "It is a strong password")

    def test_pass_weak(self):
        self.assertEqual(is_strong_password("abc"), "It is not a strong password")

    def test_pass_boundary_8(self):
        self.assertEqual(is_strong_password("12345678"), "It is a strong password")

    def test_pass_boundary_7(self):
        self.assertEqual(is_strong_password("1234567"), "It is not a strong password")

    def test_pass_empty(self):
        self.assertEqual(is_strong_password(""), "It is not a strong password")

    def test_pass_spaces(self):
        self.assertEqual(is_strong_password("        "), "It is a strong password")
        

    def test_interest_standard(self):
        self.assertEqual(calculate_interest(1000, 0.1, 1), 2100.0)

    def test_interest_zero_rate(self):
        self.assertEqual(calculate_interest(1000, 0, 5), 2000.0)

    def test_interest_negative_rate(self):
        with self.assertRaises(ValueError):
            calculate_interest(1000, -0.05, 2)

    def test_interest_invalid_year(self):
        with self.assertRaises(ValueError):
            calculate_interest(1000, 0.05, 0)

    def test_interest_high_years(self):
        result = calculate_interest(100, 0.1, 10)
        self.assertGreater(result, 100)

    def test_interest_small_amount(self):
        self.assertEqual(calculate_interest(1, 1.0, 1), 3.0)
        
        
    def test_summary_mixed(self):
        data = [["credit", 100], ["debit", 50]]
        res = get_transaction_summary(data)
        self.assertEqual(res["credit"], 100)
        self.assertEqual(res["debit"], 50)

    def test_summary_count(self):
        data = [["credit", 10], ["credit", 10], ["debit", 5]]
        res = get_transaction_summary(data)
        self.assertEqual(res["transaction_count"], 3)

    def test_summary_only_credit(self):
        res = get_transaction_summary([["credit", 500]])
        self.assertEqual(res["debit"], 0)

    def test_summary_empty(self):
        res = get_transaction_summary([])
        self.assertEqual(res["transaction_count"], 0)

    def test_summary_zeros(self):
        res = get_transaction_summary([["credit", 0], ["debit", 0]])
        self.assertEqual(res["credit"], 0)

    def test_summary_unknown_type(self):
        res = get_transaction_summary([["refund", 100]])
        self.assertEqual(res["credit"], 0)
        self.assertEqual(res["debit"], 0)

if __name__ == "__main__":
    unittest.main()