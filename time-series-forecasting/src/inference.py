import numpy as np

def forecast(model, recent_sequence, steps, scaler):
    """
    Generate multi-step forecast using trained LSTM.
    recent_sequence: last observed window of shape (look_back, 1)
    """
    predictions = []
    seq = recent_sequence.copy()

    for _ in range(steps):
        pred = model.predict(seq.reshape(1, seq.shape[0], 1), verbose=0)
        predictions.append(pred[0,0])
        seq = np.vstack([seq[1:], pred])  # slide window

    return scaler.inverse_transform(np.array(predictions).reshape(-1,1)).flatten()
