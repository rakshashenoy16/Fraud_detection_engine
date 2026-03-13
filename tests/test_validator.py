import pandas as pd
from validator import validate_transactions


def test_negative_amount_rejected():

    merchants = pd.DataFrame([
        {"merchant_id": 1, "status": "ACTIVE"}
    ])

    transactions = pd.DataFrame([
        {"transaction_id": 1, "merchant_id": 1, "transaction_amount": -10, "transaction_time": "2024-01-01"}
    ])

    result = validate_transactions(transactions, merchants)

    assert len(result) == 0