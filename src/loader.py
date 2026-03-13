import pandas as pd


def load_merchants(path):
    return pd.read_csv(path)


def load_transactions(path):
    df = pd.read_csv(path)
    df["transaction_time"] = pd.to_datetime(df["transaction_time"], errors="coerce")
    return df