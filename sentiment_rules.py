import re

positive_words = [
    "good","great","excellent","amazing","awesome","fantastic","happy","joy","love","like",
    "wonderful","best","nice","beautiful","brilliant","success","positive","pleasant","perfect",
    "delightful","superb","outstanding","enjoy","smile","win","valuable","strong","favorable",
    "impressive","incredible","marvelous","spectacular","terrific","vibrant","cheerful","optimistic",
    "lucky","satisfied","glad","helpful","kind","friendly","honest","peaceful","excited","graceful"
]
negative_words = [
    "bad","worst","poor","terrible","awful","hate","dislike","sad","angry","pain",
    "problem","negative","failure","ugly","horrible","disaster","annoying","boring","weak",
    "damage","loss","cry","fear","stress","dirty","unhappy","depressed","tired","upset",
    "hurt","nasty","rude","selfish","greedy","frustrated","disappointed","gloomy","miserable",
    "pathetic","useless","inferior","wrong","difficult","hard","issue","trouble","badly","fault"
]

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