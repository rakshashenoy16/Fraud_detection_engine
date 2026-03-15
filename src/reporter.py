import json


def save_processed_transactions(df, path):
    df.to_csv(path, index=False)


def save_settlement_report(df, path):
    df.to_csv(path, index=False)


def save_fraud_summary(df, path):

    summary = {
        "total_transactions": int(len(df)),
        "valid_transactions": int(len(df[df.transaction_status == "VALID"])),
        "fraud_transactions": int(len(df[df.transaction_status == "SUSPICIOUS"])),
        "high_value_frauds": int(df.fraud_reason.str.contains("HIGH_VALUE", na=False).sum()),
        "cross_border_frauds": int(df.fraud_reason.str.contains("CROSS_BORDER", na=False).sum()),
        "rapid_transaction_frauds": int(df.fraud_reason.str.contains("RAPID", na=False).sum())
    }

    with open(path, "w") as f:
        json.dump(summary, f, indent=4)
def save_fraud_dashboard(df, path):
    df.to_csv(path, index=False)