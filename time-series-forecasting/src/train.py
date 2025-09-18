import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import ReduceLROnPlateau

def build_lstm(input_shape):
    """Build simple LSTM model"""
    model = Sequential([
        LSTM(64, activation="tanh", input_shape=input_shape, return_sequences=False),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

def train_model(X, y, epochs=20, batch_size=16):
    """Train LSTM with learning rate scheduler (fine-tuning)"""
    model = build_lstm((X.shape[1], X.shape[2]))

    lr_scheduler = ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=3, verbose=1)

    history = model.fit(
        X, y,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        callbacks=[lr_scheduler],
        verbose=1
    )
    return model, history
