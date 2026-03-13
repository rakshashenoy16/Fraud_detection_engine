import pandas as pd
from settlement_engine import generate_settlement


def test_settlement_only_valid_transactions():

    processed = pd.DataFrame([
        {"merchant_id":1,"transaction_status":"VALID","transaction_amount":100},
        {"merchant_id":1,"transaction_status":"SUSPICIOUS","transaction_amount":1000}
    ])

    merchants = pd.DataFrame([
        {"merchant_id":1,"merchant_name":"ABC"}
    ])

    report = generate_settlement(processed, merchants)

    assert report.iloc[0]["settlement_amount"] == 100