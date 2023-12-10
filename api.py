from collections import Counter
from typing import Dict, Union

from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline
from fastapi import FastAPI
import csv

app = FastAPI(title="crypto-bert",
              description='''crypto-bert as a service''',
              version="1.0",
              )

model_name_or_path = "./CryptoBERT"
tokenizer = BertTokenizer.from_pretrained(model_name_or_path)
model = BertForSequenceClassification.from_pretrained(model_name_or_path)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


def get_sentiment_score():
    sentiment_score = []
    with open('./data/output.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            tweet = row[0]
            prediction = get_classifier(tweet)
            if prediction:
                sentiment_score.append(prediction[0])
    return sentiment_score


def get_classifier(input):
    prediction = classifier(input)
    label_map = {"LABEL_1": "Positive", "LABEL_0": "Negative"}
    for item in prediction:
        item["label"] = label_map.get(item["label"], item["label"])
    return prediction


def get_overall_sentiment_score():
    results = get_sentiment_score()
    if not results:
        return {"error": "No data available"}

    average_score = sum(d['score'] for d in results) / len(results)
    label_counts = Counter(d['label'] for d in results)

    sentiment_distribution = {label: count / len(results) * 100 for label, count in label_counts.items()}

    return {
        "average_score": average_score,
        "sentiment_distribution": sentiment_distribution
    }


@app.get("/sentiment/")
async def get_sentiment(input):
    return get_classifier(input)


@app.get("/get_scores/", response_model=Dict[str, Union[float, Dict[str, float]]])
async def get_sentiment():
    return get_overall_sentiment_score()
