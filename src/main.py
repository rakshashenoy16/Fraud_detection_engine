import logging
import os

from loader import load_merchants, load_transactions
from validator import validate_transactions
from fraud_engine import detect_fraud
from settlement_engine import generate_settlement
from fraud_score_engine import calculate_fraud_score
from dashboard_engine import generate_fraud_dashboard
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

    logging.info("Starting Fraud Detection Engine")

    # Load data
    merchants = load_merchants("../data/merchants.csv")
    transactions = load_transactions("../data/transactions.csv")

    # Validate transactions
    valid_tx = validate_transactions(transactions, merchants)

    # Detect fraud
    processed = detect_fraud(valid_tx, merchants)

    #  NEW FEATURE: Fraud Scoring
    processed_with_score = calculate_fraud_score(processed)

    # Settlement calculation
    settlement = generate_settlement(processed_with_score, merchants)

    # Save processed transactions
    save_processed_transactions(
        processed_with_score,
        "../outputs/processed_transactions.csv"
    )

    # Save settlement report
    save_settlement_report(
        settlement,
        "../outputs/merchant_settlement_report.csv"
    )

    # Save fraud summary
    save_fraud_summary(
        processed_with_score,
        "../outputs/fraud_summary.json"
    )

    #  NEW FEATURE: Fraud Dashboard
    dashboard = generate_fraud_dashboard(processed_with_score)

    save_fraud_dashboard(
        dashboard,
        "../outputs/fraud_dashboard.csv"
    )

    logging.info("Fraud Detection Engine completed successfully")


if __name__ == "__main__":
    main()