import torch
from torch.utils.data import Dataset, DataLoader
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, AdamW
from data_loader import load_data, split_data

class ReviewDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=64):
        self.texts = list(texts)
        self.labels = list(labels)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        encoding = self.tokenizer(
            self.texts[idx],
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt"
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(),
            "attention_mask": encoding["attention_mask"].squeeze(),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long),
        }

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    train_dataset = ReviewDataset(X_train, y_train, tokenizer)
    train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)

    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
    optimizer = AdamW(model.parameters(), lr=1e-5)

    model.train()
    for epoch in range(2):
        for batch in train_loader:
            optimizer.zero_grad()
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                labels=batch["labels"]
            )
            loss = outputs.loss
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    torch.save(model.state_dict(), "model.pth")
    print("✅ Training complete, model saved!")

if __name__ == "__main__":
    train_model()
