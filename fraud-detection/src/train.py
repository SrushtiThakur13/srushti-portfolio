import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from data_loader import generate_transactions

# Generate dataset
df = generate_transactions(n=2000)

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

# Train model
model = IsolationForest(contamination=0.05, random_state=42)
y_pred = model.fit_predict(X)
y_pred = [1 if x == -1 else 0 for x in y_pred]  # -1 = anomaly

print(classification_report(y, y_pred))

# Save model
import joblib
joblib.dump(model, "fraud_model.pkl")
