from flask import Flask, request, jsonify, render_template
import sqlite3
import pickle
from textblob import TextBlob


app = Flask(__name__)


# Load the model and vectorizer
with open('models/fake_news_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


# Bias analysis function
def bias_check(news):
    blob = TextBlob(news)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity
    return polarity, subjectivity


# Root route
@app.route('/')
def home():
    return render_template("main.html", prediction=None)


# Predict route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    confidence = None
    polarity = None
    subjectivity = None
    news_text = None


    if request.method == 'POST':
        news_text = request.form.get('news_text', '').strip()


        if news_text:
            text_tfidf = vectorizer.transform([news_text])
            pred = model.predict(text_tfidf)[0]
            confidence = model.predict_proba(text_tfidf).max() * 100
            prediction = "TRUE" if pred == 1 else "FALSE"


            # Perform bias analysis
            polarity, subjectivity = bias_check(news_text)
            polarity = round((polarity + 1) * 50, 2)  # Convert -1 to 1 range into 0-100%
            subjectivity = round(subjectivity * 100, 2)  # Convert 0-1 to percentage


    return render_template(
        "main.html",
        prediction=prediction,
        confidence=round(confidence, 2) if confidence else None,
        polarity=polarity if polarity else None,
        subjectivity=subjectivity if subjectivity else None,
        news_text=news_text,
    )


# Feedback route
@app.route('/feedback', methods=['POST'])
def feedback():
    news_text = request.form.get('feedback_text', '').strip()
    predicted_label = request.form.get('predicted_label', '').strip()
    actual_label = request.form.get('actual_label', '').strip()


    if not news_text or not predicted_label or not actual_label:
        return jsonify({"error": "Invalid feedback data"}), 400


    try:
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (text, predicted_label, actual_label)
            VALUES (?, ?, ?)
        ''', (news_text, predicted_label, actual_label))
        conn.commit()
        conn.close()
        return render_template("main.html", message="Feedback submitted successfully!")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
