import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def generate_synthetic_data(n_points=200):
    """Generate synthetic time series with trend + seasonality + noise"""
    np.random.seed(42)
    time = np.arange(n_points)
    series = 0.05 * time + 2 * np.sin(0.2*time) + np.random.normal(0, 0.3, n_points)
    return pd.DataFrame({"time": time, "value": series})

def prepare_data(series, look_back=10):
    """Prepare sliding windows for LSTM training"""
    values = series["value"].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    X, y = [], []
    for i in range(len(scaled) - look_back):
        X.append(scaled[i:i+look_back, 0])
        y.append(scaled[i+look_back, 0])
    X, y = np.array(X), np.array(y)
    X = X.reshape(X.shape[0], X.shape[1], 1)
    return X, y, scaler
