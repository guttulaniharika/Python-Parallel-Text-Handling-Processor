from chunk_manager import load_dataset
from sentiment_rules import clean_text, analyze_sentiment
from db_manager import create_table, bulk_insert

def process_file(file_path):

    data = load_dataset(file_path)

    results = []

    for text in data:
        cleaned = clean_text(text)
        score, sentiment = analyze_sentiment(cleaned)
        results.append((text, score, sentiment))

    # store in DB
    create_table()
    bulk_insert(results)

    return results