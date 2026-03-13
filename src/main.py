import logging
import os

from loader import load_merchants, load_transactions
from validator import validate_transactions
from fraud_engine import detect_fraud
from settlement_engine import generate_settlement
from reporter import *

# Create required folders if they don't exist
os.makedirs("../logs", exist_ok=True)
os.makedirs("../outputs", exist_ok=True)

logging.basicConfig(
    filename="../logs/fraud_engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    merchants = load_merchants("../data/merchants.csv")
    transactions = load_transactions("../data/transactions.csv")

    valid_tx = validate_transactions(transactions, merchants)

    processed = detect_fraud(valid_tx, merchants)

    settlement = generate_settlement(processed, merchants)

    save_processed_transactions(
        processed,
        "../outputs/processed_transactions.csv"
    )

    save_settlement_report(
        settlement,
        "../outputs/merchant_settlement_report.csv"
    )

    save_fraud_summary(
        processed,
        "../outputs/fraud_summary.json"
    )


if __name__ == "__main__":
    main()