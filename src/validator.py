import logging

logger = logging.getLogger(__name__)


def validate_transactions(transactions, merchants):

    valid_transactions = []

    merchant_lookup = merchants.set_index("merchant_id")

    for _, tx in transactions.iterrows():

        merchant_id = tx["merchant_id"]

        if merchant_id not in merchant_lookup.index:
            logger.warning("Unknown merchant", extra={"merchant_id": merchant_id})
            continue

        merchant = merchant_lookup.loc[merchant_id]

        if merchant["status"] == "BLOCKED":
            logger.warning("Blocked merchant", extra={"merchant_id": merchant_id})
            continue

        if tx["transaction_amount"] <= 0:
            logger.warning("Invalid amount", extra={"transaction_id": tx["transaction_id"]})
            continue

        if tx["transaction_time"] is None:
            logger.warning("Invalid timestamp", extra={"transaction_id": tx["transaction_id"]})
            continue

        valid_transactions.append(tx)

    return valid_transactions