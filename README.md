# Fraud Detection and Payment Settlement Engine

A Python-based fraud detection system that processes transaction data, detects suspicious activity using rule-based logic and fraud scoring, generates settlement reports, and provides an interactive monitoring dashboard.


FEATURES

1. Transaction Processing
- Loads merchant and transaction datasets
- Validates transaction records
- Flags invalid or incomplete data

2. Fraud Detection Engine
Detects suspicious transactions using rules such as:
- High value transactions
- Cross-border transactions
- Rapid transaction activity
- Crypto high-value transactions

3. Fraud Scoring
Each transaction receives a fraud risk score based on triggered rules.

4. Merchant Settlement Engine
Calculates merchant settlement reports based on valid transactions.

5. Fraud Analytics
Automatically generates:
- processed_transactions.csv
- merchant_settlement_report.csv
- fraud_summary.json
- fraud_dashboard.csv

6. Interactive Fraud Dashboard
Streamlit dashboard showing:
- Fraud rate
- Fraud trend over time
- Fraud rule breakdown
- Transaction table

7. Docker Support
The project can be run inside a Docker container.

8. Unit Testing
Test cases implemented using Python unittest.

----------------------------------------------------

PROJECT STRUCTURE

fraud-detection-system/

data/
    merchants.csv
    transactions.csv

src/
    loader.py
    validator.py
    fraud_engine.py
    fraud_score_engine.py
    settlement_engine.py
    dashboard_engine.py
    reporter.py
    main.py

tests/
    test_fraud_engine.py

outputs/
    processed_transactions.csv
    merchant_settlement_report.csv
    fraud_summary.json
    fraud_dashboard.csv

logs/
    fraud_engine.log

dashboard.py

requirements.txt
.gitignore
README.md

----------------------------------------------------

INSTALLATION

Clone the repository

git clone https://github.com/YOUR_USERNAME/fraud-detection-system.git

cd fraud-detection-system

Install dependencies

pip install -r requirements.txt

----------------------------------------------------

RUNNING THE FRAUD ENGINE

python src/main.py

Generated outputs will appear in:

outputs/

processed_transactions.csv  
merchant_settlement_report.csv  
fraud_summary.json  
fraud_dashboard.csv  

----------------------------------------------------

RUNNING UNIT TESTS

python -m unittest discover tests



RUNNING THE DASHBOARD

streamlit run dashboard.py

Dashboard will open at

http://localhost:8501



TECHNOLOGIES USED

Python  
Pandas  
Streamlit  
Plotly  

unittest  

