from transformers import BertTokenizer, BertForSequenceClassification
import torch

def predict_sentiment(text):
    model = BertForSequenceClassification.from_pretrained("sentiment_model")
    tokenizer = BertTokenizer.from_pretrained("sentiment_model")

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    label = torch.argmax(probs).item()
    confidence = probs[0][label].item()
    sentiment = "Positive" if label == 1 else "Negative"
    return sentiment, confidence

if __name__ == "__main__":
    print(predict_sentiment("Me encanta este lugar"))
