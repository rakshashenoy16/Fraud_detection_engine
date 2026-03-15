import unittest
import pandas as pd
from src.validator import validate_transactions


class TestTransactionValidation(unittest.TestCase):

    def setUp(self):
        self.merchants = pd.DataFrame([
            {"merchant_id": 1, "merchant_name": "StoreA", "country": "US", "status": "ACTIVE"},
            {"merchant_id": 2, "merchant_name": "StoreB", "country": "US", "status": "BLOCKED"}
        ])

    def test_invalid_merchant_rejected(self):

        transactions = pd.DataFrame([
            {"transaction_id": 1, "merchant_id": 99, "transaction_amount": 100,
             "transaction_time": "2024-01-01"}
        ])

        result = validate_transactions(transactions, self.merchants)

        self.assertEqual(len(result), 0)

    def test_blocked_merchant_rejected(self):

        transactions = pd.DataFrame([
            {"transaction_id": 1, "merchant_id": 2, "transaction_amount": 100,
             "transaction_time": "2024-01-01"}
        ])

        result = validate_transactions(transactions, self.merchants)

        self.assertEqual(len(result), 0)

    def test_negative_amount_rejected(self):

        transactions = pd.DataFrame([
            {"transaction_id": 1, "merchant_id": 1, "transaction_amount": -50,
             "transaction_time": "2024-01-01"}
        ])

        result = validate_transactions(transactions, self.merchants)

        self.assertEqual(len(result), 0)

    def test_invalid_timestamp_handling(self):

        transactions = pd.DataFrame([
            {"transaction_id": 1, "merchant_id": 1, "transaction_amount": 100,
             "transaction_time": None}
        ])

        result = validate_transactions(transactions, self.merchants)

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()