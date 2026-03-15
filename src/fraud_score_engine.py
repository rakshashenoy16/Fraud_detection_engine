import pandas as pd

RULE_SCORES = {
    "HIGH_VALUE_TRANSACTION": 40,
    "CROSS_BORDER_TRANSACTION": 30,
    "RAPID_TRANSACTIONS": 50,
    "CRYPTO_HIGH_VALUE": 20
}


def calculate_fraud_score(processed_transactions):

    df = processed_transactions.copy()

    scores = []

    for _, row in df.iterrows():

        fraud_reasons = str(row["fraud_reason"]).split(",")

        score = 0

        for reason in fraud_reasons:
            reason = reason.strip()
            if reason in RULE_SCORES:
                score += RULE_SCORES[reason]

        scores.append(score)

    df["fraud_score"] = scores

    return df