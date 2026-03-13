import pandas as pd


def generate_settlement(processed_transactions, merchants):

    merged = processed_transactions.merge(merchants, on="merchant_id")

    report = []

    for merchant_id, group in merged.groupby("merchant_id"):

        total = len(group)

        valid = len(group[group["transaction_status"] == "VALID"])

        fraud = len(group[group["transaction_status"] == "SUSPICIOUS"])

        settlement = group[group["transaction_status"] == "VALID"]["transaction_amount"].sum()

        report.append({
            "merchant_id": merchant_id,
            "merchant_name": group["merchant_name"].iloc[0],
            "total_transactions": total,
            "valid_transactions": valid,
            "fraud_transactions": fraud,
            "settlement_amount": settlement
        })

    return pd.DataFrame(report)