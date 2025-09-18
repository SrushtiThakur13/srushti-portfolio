from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import Dataset
import torch
from src.data_loader import load_sample_data

class SentimentDataset(Dataset):
    def __init__(self, tokenizer, max_len=64):
        df = load_sample_data()
        self.encodings = tokenizer(list(df["text"]), truncation=True, padding=True, max_length=max_len)
        self.labels = df["label"]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

def train_model():
    tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
    dataset = SentimentDataset(tokenizer)
    model = BertForSequenceClassification.from_pretrained("bert-base-multilingual-cased", num_labels=2)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=1,
        per_device_train_batch_size=2,
        save_steps=10,
        logging_dir="./logs"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    trainer.train()
    model.save_pretrained("sentiment_model")
    tokenizer.save_pretrained("sentiment_model")

if __name__ == "__main__":
    train_model()
