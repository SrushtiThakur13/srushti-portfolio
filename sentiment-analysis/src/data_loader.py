import pandas as pd

def load_sample_data():
    # Example multilingual dataset
    data = {
        "text": [
            "I love this product!",   # English
            "Me encanta este lugar",  # Spanish
            "यह बहुत अच्छा है",         # Hindi
            "I am really disappointed", # English
            "Esto es terrible"         # Spanish
        ],
        "label": [1, 1, 1, 0, 0]  # 1 = Positive, 0 = Negative
    }
    return pd.DataFrame(data)
