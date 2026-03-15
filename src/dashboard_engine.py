import pandas as pd


def generate_fraud_dashboard(processed_transactions):

    df = processed_transactions.copy()

    # Convert to datetime safely
    df["date"] = pd.to_datetime(df["transaction_time"], errors="coerce").dt.date

    # Replace missing dates so transactions are not dropped
    df["date"] = df["date"].fillna("UNKNOWN")

    dashboard = []

    for date, group in df.groupby("date"):

        total = len(group)

        fraud = len(group[group["transaction_status"] == "SUSPICIOUS"])

        fraud_rate = fraud / total if total else 0

        dashboard.append({
            "date": date,
            "total_transactions": total,
            "fraud_transactions": fraud,
            "fraud_rate": fraud_rate
        })

    return pd.DataFrame(dashboard)