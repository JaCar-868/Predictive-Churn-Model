### `main.py`
```python
#!/usr/bin/env python3
"""
Entry point for Predictive Churn & Adoption Model
"""
import os
from dotenv import load_dotenv
from modules.data_prep import load_and_engineer_features
from modules.modeling import train_and_evaluate
from modules.reporting import export_top_risk_customers
from powerbi_refresh.powerbi_api import refresh_dataset

def main():
    load_dotenv()
    # 1. Load & feature-engineer
    df_features, y = load_and_engineer_features(
        db_url=os.getenv("DATABASE_URL")
    )

    # 2. Train & evaluate model
    model = train_and_evaluate(df_features, y)

    # 3. Export top 20 at-risk users
    export_top_risk_customers(model, df_features, top_n=20)

    # 4. Trigger Power BI refresh
    refresh_dataset(
        group_id=os.getenv("PBI_GROUP_ID"),
        dataset_id=os.getenv("PBI_DATASET_ID"),
        access_token=os.getenv("PBI_TOKEN")
    )

if __name__ == "__main__":
    main()
