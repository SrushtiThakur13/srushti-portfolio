import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

MODEL_PATH = "model.pth"

def predict_sentiment(text):
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
    model.eval()

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        label = torch.argmax(probs).item()

    return "Positive" if label == 1 else "Negative"

if __name__ == "__main__":
    print(predict_sentiment("The product was fantastic!"))
    print(predict_sentiment("Worst experience ever."))
