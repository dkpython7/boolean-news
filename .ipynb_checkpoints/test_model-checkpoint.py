import pickle

# Load the trained model
with open('models/fake_news_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TF-IDF vectorizer
with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

# Function to predict real or fake news with confidence
def predict_news(news_text):
    # Transform the input text using the loaded vectorizer
    text_tfidf = tfidf.transform([news_text])
    # Get prediction probabilities
    prediction_prob = model.predict_proba(text_tfidf)
    # Get the predicted class (0 for fake, 1 for real)
    prediction = model.predict(text_tfidf)
    
    # Probability of the prediction
    prob = prediction_prob[0][prediction[0]] * 100  # Convert to percentage
    label = "TRUE" if prediction[0] == 1 else "FALSE"
    
    # Determine the message based on confidence benchmarks
    if 40 <= prob <= 60:
        return f"This information is possibly {label} with an confidence level of {prob:.2f}%."
    elif 66.01 <= prob <= 70:
        return f"This information is likely {label} with an confidence level of {prob:.2f}%."
    else:
        return f"This information is {label}!"

# Example news to test
news_to_test = input("Enter a news article: ")
result = predict_news(news_to_test)
print(result)