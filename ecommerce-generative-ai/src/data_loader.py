import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # Simulated product review dataset
    data = {
        "review": [
            "This product is amazing!",
            "Worst purchase ever, waste of money.",
            "Great quality and fast shipping.",
            "Terrible experience, item broke in a week.",
            "Excellent value for money."
        ],
        "label": [1, 0, 1, 0, 1]  # 1 = Positive, 0 = Negative
    }
    df = pd.DataFrame(data)
    return df

def split_data(df):
    return train_test_split(df["review"], df["label"], test_size=0.2, random_state=42)

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    print("Train size:", len(X_train))
    print("Test size:", len(X_test))
