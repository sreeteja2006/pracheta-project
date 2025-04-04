import unittest
import sys

from finance_tracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FinanceTracker()

    def test_add_transaction(self):
        self.tracker.add_transaction(100, "2023-04-01", "income", "Test")
        self.assertEqual(len(self.tracker.transactions), 1)

    def test_total_expense(self):
        self.tracker.add_transaction(100, "2023-04-01", "expense", "Test")
        self.assertEqual(self.tracker.total_expense(), 100)

    def test_total_income(self):
        self.tracker.add_transaction(100, "2023-04-01", "income", "Test")
        self.assertEqual(self.tracker.total_income(), 100)

if __name__ == "__main__":
    unittest.main()
