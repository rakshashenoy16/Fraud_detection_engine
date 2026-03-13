import json


def save_processed_transactions(df, path):
    df.to_csv(path, index=False)


def save_settlement_report(df, path):
    df.to_csv(path, index=False)


def save_fraud_summary(df, path):

    summary = {
        "total_transactions": len(df),
        "valid_transactions": len(df[df.transaction_status == "VALID"]),
        "fraud_transactions": len(df[df.transaction_status == "SUSPICIOUS"]),
        "high_value_frauds": df.fraud_reason.str.contains("HIGH_VALUE").sum(),
        "cross_border_frauds": df.fraud_reason.str.contains("CROSS_BORDER").sum(),
        "rapid_transaction_frauds": df.fraud_reason.str.contains("RAPID").sum()
    }

    with open(path, "w") as f:
        json.dump(summary, f, indent=4)