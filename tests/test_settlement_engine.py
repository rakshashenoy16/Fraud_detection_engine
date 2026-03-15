import unittest
import pandas as pd
from src.settlement_engine import generate_settlement


class TestSettlementEngine(unittest.TestCase):

    def setUp(self):

        self.merchants = pd.DataFrame([
            {"merchant_id": 1, "merchant_name": "StoreA"}
        ])

    def test_settlement_only_valid_transactions(self):

        processed = pd.DataFrame([
            {"merchant_id": 1, "transaction_status": "VALID", "transaction_amount": 100},
            {"merchant_id": 1, "transaction_status": "SUSPICIOUS", "transaction_amount": 1000}
        ])

        report = generate_settlement(processed, self.merchants)

        self.assertEqual(report.iloc[0]["settlement_amount"], 100)

    def test_settlement_amount_calculation(self):

        processed = pd.DataFrame([
            {"merchant_id": 1, "transaction_status": "VALID", "transaction_amount": 100},
            {"merchant_id": 1, "transaction_status": "VALID", "transaction_amount": 200}
        ])

        report = generate_settlement(processed, self.merchants)

        self.assertEqual(report.iloc[0]["settlement_amount"], 300)


if __name__ == "__main__":
    unittest.main()