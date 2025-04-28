import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open('intents.json') as f:
    data = json.load(f)

X, y = [], []

for intent in data['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

# Vectorize and train
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vect, y)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")
