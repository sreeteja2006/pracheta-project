import unittest
import sys
sys.path.insert(1,"/home/sreeteja/Projects/pracheta_projects/data_storage.py")
import data_storage

class TestDataStorage(unittest.TestCase):
    def test_load_transactions(self):
        transactions = load_transactions()
        self.assertIsInstance(transactions, list)

    def test_save_transactions(self):
        transactions = [{"amount": 100, "date": "2023-04-01", "category": "income", "description": "Test"}]
        save_transactions(transactions)
        loaded_transactions = load_transactions()
        self.assertEqual(transactions, loaded_transactions)

if __name__ == "__main__":
    unittest.main()
