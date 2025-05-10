from textblob import TextBlob

def bias_check(news):

    blob = TextBlob(news)
    sentiment = blob.sentiment

    '''
    determining polarity in text
    -1 < polarity < 1 --> 1 = positive sentiment (eg. I like you) , -1 = negative sentiment (eg. I hate you), 0 = no sentiment (not enough data)
    '''
    polarity = sentiment.polarity

    '''
    determining subjectivity in text
    0 < subjectivity < 1 --> 0 = conpletly objective, 1 = completely subjective
    '''
    subjectivity = sentiment.subjectivity

    return polarity, subjectivity