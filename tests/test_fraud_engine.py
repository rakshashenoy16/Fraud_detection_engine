from fraud_engine import detect_fraud
import pandas as pd


def test_high_value_transaction_flag():

    merchants = pd.DataFrame([
        {"merchant_id": 1, "country": "US"}
    ])

    transactions = [{
        "transaction_id": 1,
        "merchant_id": 1,
        "customer_id": 1,
        "transaction_amount": 200000,
        "transaction_time": pd.Timestamp("2024-01-01"),
        "payment_method": "CARD",
        "country": "US"
    }]

    df = detect_fraud(transactions, merchants)

    assert df.iloc[0]["transaction_status"] == "SUSPICIOUS"