import pandas as pd
import numpy as np

def generate_transactions(n=1000, fraud_ratio=0.05, seed=42):
    np.random.seed(seed)
    data = pd.DataFrame({
        "amount": np.random.exponential(scale=100, size=n),
        "time_gap": np.random.exponential(scale=1, size=n),
        "merchant_id": np.random.randint(1, 50, n),
        "device_id": np.random.randint(1, 100, n),
        "is_fraud": [1 if i < fraud_ratio*n else 0 for i in range(n)]
    })
    return data
