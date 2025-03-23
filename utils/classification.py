import json
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def load_data(path):
    with open(path, 'r') as file:
        data = json.load(file)
    texts = [item['text'] for item in data]
    labels = [item['label'] for item in data]
    return texts, labels

def train_classification_model():
    texts, labels = load_data('./data/annotated_data.json')

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    os.makedirs('./models', exist_ok=True)

    with open('./models/compliance_classifier.pkl', 'wb') as model_file:
        pickle.dump((vectorizer, model), model_file)
        print("Model saved to ./models/compliance_classifier.pkl")

def predict_compliance(text):
    with open('./models/compliance_classifier.pkl', 'rb') as model_file:
        vectorizer, model = pickle.load(model_file)
    X = vectorizer.transform([text])
    return model.predict(X)[0]

test_text = "please verify your account number."
prec = predict_compliance(test_text)
print(f"Prediction: {prec}")