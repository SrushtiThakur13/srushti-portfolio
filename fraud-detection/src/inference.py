import joblib
import pandas as pd

def predict_transaction(model_path, transaction):
    model = joblib.load(model_path)
    df = pd.DataFrame([transaction])
    pred = model.predict(df)[0]
    return "Fraudulent" if pred == -1 else "Legit"

if __name__ == "__main__":
    tx = {"amount": 5000, "time_gap": 0.01, "merchant_id": 3, "device_id": 10}
    print(predict_transaction("fraud_model.pkl", tx))
