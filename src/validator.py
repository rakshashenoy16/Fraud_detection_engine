import logging

# Create a logger for this module
logger = logging.getLogger(__name__)


def validate_transactions(transactions, merchants):
    """
    Validates transaction records before fraud detection.

    Validation checks include:
    1. Merchant must exist in the merchant dataset.
    2. Merchant must not be blocked.
    3. Transaction amount must be positive.
    4. Transaction must contain a valid timestamp.

    Returns a list of valid transactions.
    """

    # List to store transactions that pass validation
    valid_transactions = []

    # Create a lookup table for merchants using merchant_id as index
    # This makes merchant lookups faster
    merchant_lookup = merchants.set_index("merchant_id")

    # Iterate through each transaction record
    for _, tx in transactions.iterrows():

        # Extract merchant ID from transaction
        merchant_id = tx["merchant_id"]

        # Check if merchant exists in merchant dataset
        if merchant_id not in merchant_lookup.index:
            logger.warning("Unknown merchant", extra={"merchant_id": merchant_id})
            continue

        # Retrieve merchant information
        merchant = merchant_lookup.loc[merchant_id]

        # Check if merchant is blocked
        if merchant["status"] == "BLOCKED":
            logger.warning("Blocked merchant", extra={"merchant_id": merchant_id})
            continue

        # Validate transaction amount (must be greater than zero)
        if tx["transaction_amount"] <= 0:
            logger.warning(
                "Invalid amount",
                extra={"transaction_id": tx["transaction_id"]}
            )
            continue

        # Validate transaction timestamp
        if tx["transaction_time"] is None:
            logger.warning(
                "Invalid timestamp",
                extra={"transaction_id": tx["transaction_id"]}
            )
            continue

        # If all checks pass, add transaction to valid list
        valid_transactions.append(tx)

    # Return validated transactions
    return valid_transactions