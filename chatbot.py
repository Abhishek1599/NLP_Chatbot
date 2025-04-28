from transformers import pipeline
import json
import random

# Load intents
with open("intents.json") as f:
    intents = json.load(f)

labels = [i["tag"] for i in intents["intents"]]
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def get_response(user_input):
    result = classifier(user_input, labels)
    predicted_tag = result["labels"][0]

    for intent in intents["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])
    return "Sorry, I don't understand."
