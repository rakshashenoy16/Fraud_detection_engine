import unittest
import pandas as pd
from src.fraud_engine import detect_fraud


class TestFraudDetection(unittest.TestCase):

    def setUp(self):

        self.merchants = pd.DataFrame([
            {"merchant_id": 1, "merchant_name": "StoreA", "country": "US"}
        ])

    def test_high_value_transaction_flag(self):

        transactions = [{
            "transaction_id": 1,
            "merchant_id": 1,
            "customer_id": 1,
            "transaction_amount": 200000,
            "transaction_time": pd.Timestamp("2024-01-01 10:00:00"),
            "payment_method": "CARD",
            "country": "US"
        }]

        result = detect_fraud(transactions, self.merchants)

        self.assertEqual(result.iloc[0]["transaction_status"], "SUSPICIOUS")

    def test_cross_border_transaction_flag(self):

        transactions = [{
            "transaction_id": 2,
            "merchant_id": 1,
            "customer_id": 2,
            "transaction_amount": 1000,
            "transaction_time": pd.Timestamp("2024-01-01"),
            "payment_method": "CARD",
            "country": "UK"
        }]

        result = detect_fraud(transactions, self.merchants)

        self.assertIn("CROSS_BORDER_TRANSACTION", result.iloc[0]["fraud_reason"])

    def test_crypto_high_value_flag(self):

        transactions = [{
            "transaction_id": 3,
            "merchant_id": 1,
            "customer_id": 3,
            "transaction_amount": 60000,
            "transaction_time": pd.Timestamp("2024-01-01"),
            "payment_method": "CRYPTO",
            "country": "US"
        }]

        result = detect_fraud(transactions, self.merchants)

        self.assertIn("CRYPTO_HIGH_VALUE", result.iloc[0]["fraud_reason"])

    def test_multiple_fraud_rules_trigger(self):

        transactions = [{
            "transaction_id": 4,
            "merchant_id": 1,
            "customer_id": 4,
            "transaction_amount": 200000,
            "transaction_time": pd.Timestamp("2024-01-01"),
            "payment_method": "CRYPTO",
            "country": "UK"
        }]

        result = detect_fraud(transactions, self.merchants)

        self.assertEqual(result.iloc[0]["transaction_status"], "SUSPICIOUS")


if __name__ == "__main__":
    unittest.main()