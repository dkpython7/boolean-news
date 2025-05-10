import os
import re
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize spaces
    return text

def main():
    os.makedirs("models", exist_ok=True)

    print("Loading data...")
    fake_data = pd.read_csv("data/dataset_fake.csv", header=None, names=["id", "text"], usecols=["text"], quotechar='"', on_bad_lines="skip")
    real_data = pd.read_csv("data/dataset_true.csv", header=None, names=["id", "text"], usecols=["text"], quotechar='"', on_bad_lines="skip")

    fake_data["label"] = 0
    real_data["label"] = 1

    data = pd.concat([fake_data, real_data], ignore_index=True)
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    data["text"] = data["text"].fillna("")

    print("Cleaning text data...")
    data["text"] = data["text"].apply(clean_text)

    print("Vectorizing text data...")
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7, min_df=5, ngram_range=(1, 2))
    X_tfidf = tfidf.fit_transform(data["text"])
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    print("Training models...")
    models = {
        "random_forest": RandomForestClassifier(n_estimators=200, max_depth=None, n_jobs=-1, random_state=42),
        "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
        "xgboost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        accuracy = accuracy_score(y_test, preds)
        results[name] = (model, accuracy)
        print(f"{name.replace('_', ' ').title()} Accuracy: {accuracy:.4f}")

    best_model_name, (best_model, best_accuracy) = max(results.items(), key=lambda item: item[1][1])
    print(f"\nBest model: {best_model_name} with accuracy {best_accuracy:.4f}")

    with open("models/fake_news_model.pkl", "wb") as model_file:
        pickle.dump(best_model, model_file)

    with open("models/tfidf_vectorizer.pkl", "wb") as vectorizer_file:
        pickle.dump(tfidf, vectorizer_file)

    print("\nModel and vectorizer saved in 'models' folder.")
    print("\nClassification Report:")
    best_preds = best_model.predict(X_test)
    print(classification_report(y_test, best_preds))

if __name__ == "__main__":
    main()