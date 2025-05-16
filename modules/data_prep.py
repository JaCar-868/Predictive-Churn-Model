import pandas as pd
from sqlalchemy import create_engine

def load_and_engineer_features(db_url: str):
    """
    Connect to warehouse, join analytics + transaction + CRM tables,
    and engineer session, transaction, and abandon features.
    """
    engine = create_engine(db_url)
    # Example SQL join
    query = """
    SELECT u.user_id,
           COUNT(DISTINCT s.session_id) AS sessions,
           AVG(s.duration) AS avg_duration,
           SUM(t.amount) AS first_week_txn
    FROM sessions AS s
    JOIN transactions AS t ON s.user_id = t.user_id
    JOIN users AS u ON u.user_id = s.user_id
    WHERE s.date >= CURRENT_DATE - INTERVAL '7 days'
    GROUP BY u.user_id;
    """
    df = pd.read_sql(query, engine)
    # label churn: no login in 30 days
    df["churn"] = df["last_login_date"] < (pd.Timestamp.today() - pd.Timedelta(days=30))
    y = df.pop("churn")
    return df, y
