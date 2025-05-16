# Predictive-Churn-Model

A Python workflow to join clickstream, transaction, and CRM data; engineer features; train a churn-prediction model; and feed results into Power BI for live dashboards.

## Features

1. **Data Prep & Feature Engineering**  
   - Complex SQL joins across multiple tables  
   - Session, transaction, and abandon metrics  

2. **Machine Learning**  
   - Random Forest (and XGBoost) classifiers  
   - Precision/recall reporting at 85%+ precision  

3. **Automated Reporting**  
   - CSV export of top-risk users (for Power BI ingestion)  
   - Python script to trigger Power BI dataset refresh  

## Setup

```bash
git clone https://github.com/<you>/predictive-churn-model.git
cd predictive-churn-model
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

Create a .env:

DATABASE_URL=postgresql://user:pass@host:port/dbname
PBI_GROUP_ID=...
PBI_DATASET_ID=...
PBI_TOKEN=...

Run:


python main.py
