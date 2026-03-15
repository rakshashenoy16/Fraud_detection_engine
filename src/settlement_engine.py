import pandas as pd


def generate_settlement(processed_transactions, merchants):
    """
    Generates a merchant settlement report.

    Steps:
    1. Merge processed transaction data with merchant details.
    2. Group transactions by merchant.
    3. Calculate transaction metrics for each merchant.
    4. Return a settlement summary dataframe.
    """

    # Merge transaction data with merchant information using merchant_id
    merged = processed_transactions.merge(merchants, on="merchant_id")

    # List to store settlement report rows
    report = []

    # Group transactions by merchant_id
    for merchant_id, group in merged.groupby("merchant_id"):

        # Total number of transactions for the merchant
        total = len(group)

        # Count of valid transactions
        valid = len(group[group["transaction_status"] == "VALID"])

        # Count of suspicious (fraud) transactions
        fraud = len(group[group["transaction_status"] == "SUSPICIOUS"])

        # Sum of settlement amount (only valid transactions are settled)
        settlement = group[
            group["transaction_status"] == "VALID"
        ]["transaction_amount"].sum()

        # Append calculated metrics for the merchant
        report.append({
            "merchant_id": merchant_id,
            "merchant_name": group["merchant_name"].iloc[0],
            "total_transactions": total,
            "valid_transactions": valid,
            "fraud_transactions": fraud,
            "settlement_amount": settlement
        })

    # Convert list of dictionaries into a DataFrame
    return pd.DataFrame(report)