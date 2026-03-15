import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 Payment Fraud Monitoring Dashboard")

# Load data
transactions = pd.read_csv("outputs/processed_transactions.csv")
dashboard = pd.read_csv("outputs/fraud_dashboard.csv")

with open("outputs/fraud_summary.json") as f:
    summary = json.load(f)

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", summary["total_transactions"])
col2.metric("Valid Transactions", summary["valid_transactions"])
col3.metric("Fraud Transactions", summary["fraud_transactions"])
fraud_rate = summary["fraud_transactions"] / summary["total_transactions"]
col4.metric("Fraud Rate", f"{fraud_rate:.2%}")

st.divider()

# Fraud Trend Chart
st.subheader("Fraud Trend Over Time")

fig = px.line(
    dashboard,
    x="date",
    y=["total_transactions", "fraud_transactions"],
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Fraud Reason Breakdown
st.subheader("Fraud Rule Breakdown")

fraud_df = transactions[transactions["transaction_status"] == "SUSPICIOUS"]

reasons = fraud_df["fraud_reason"].str.split(",", expand=True).stack()

reason_counts = reasons.value_counts().reset_index()
reason_counts.columns = ["Fraud Rule", "Count"]

fig2 = px.bar(reason_counts, x="Fraud Rule", y="Count")

st.plotly_chart(fig2, use_container_width=True)

# Transaction Table
st.subheader("Processed Transactions")

st.dataframe(transactions)