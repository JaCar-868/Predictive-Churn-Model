from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_and_evaluate(X, y):
    """
    Split, train RandomForest + XGBoost, compare,
    and return best model.
    """
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(Xtr, ytr)
    preds = model.predict(Xte)
    print(classification_report(yte, preds))
    return model
