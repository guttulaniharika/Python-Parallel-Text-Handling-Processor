import re

positive_words = ["good","great","excellent","happy"]
negative_words = ["bad","terrible","worst"]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


def analyze_sentiment(text):

    words = text.split()

    pos = 0
    neg = 0

    for w in words:

        if w in positive_words:
            pos += 1

        if w in negative_words:
            neg += 1

    score = pos - neg

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment