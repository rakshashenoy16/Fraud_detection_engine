from collections import defaultdict
import pandas as pd


def detect_fraud(transactions, merchants):

    merchant_lookup = merchants.set_index("merchant_id")

    results = []

    customer_transactions = defaultdict(list)

    for tx in transactions:

        reasons = []

        merchant = merchant_lookup.loc[tx["merchant_id"]]

        amount = tx["transaction_amount"]

        # Rule 1
        if amount > 100000:
            reasons.append("HIGH_VALUE_TRANSACTION")

        # Rule 2
        if tx["country"] != merchant["country"]:
            reasons.append("CROSS_BORDER_TRANSACTION")

        # Rule 4
        if tx["payment_method"] == "CRYPTO" and amount > 50000:
            reasons.append("CRYPTO_HIGH_VALUE")

        # Rule 3 Rapid transactions
        customer_id = tx["customer_id"]
        time = tx["transaction_time"]

        history = customer_transactions[customer_id]

        recent = [t for t in history if (time - t).total_seconds() <= 120]

        if len(recent) >= 3:
            reasons.append("RAPID_TRANSACTIONS")

        history.append(time)

        fraud_flag = 1 if reasons else 0
        status = "SUSPICIOUS" if reasons else "VALID"

        results.append({
            "transaction_id": tx["transaction_id"],
            "merchant_id": tx["merchant_id"],
            "customer_id": tx["customer_id"],
            "transaction_amount": amount,
            "transaction_time": time,
            "fraud_flag": fraud_flag,
            "fraud_reason": ",".join(reasons),
            "transaction_status": status
        })

    return pd.DataFrame(results)