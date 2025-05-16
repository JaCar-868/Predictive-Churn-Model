import pandas as pd

def export_top_risk_customers(model, X, top_n=20):
    """
    Score all users, pick top_n most likely to churn,
    and write CSV for Power BI ingestion.
    """
    X = X.copy()
    X["risk_score"] = model.predict_proba(X)[:, 1]
    df_top = X.nlargest(top_n, "risk_score")
    df_top[["risk_score"]].to_csv("top_risk_customers.csv", index_label="user_id")
    print(f"Exported top {top_n} at-risk users.")
