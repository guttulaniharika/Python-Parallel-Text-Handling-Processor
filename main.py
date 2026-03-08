import time
import concurrent.futures
from multiprocessing import Pool, cpu_count
from collections import Counter

from chunk_manager import load_dataset, create_chunks
from sentiment_rules import clean_text, analyze_sentiment
from db_manager import create_table, bulk_insert, query_test, export_to_csv


CHUNK_SIZE = 1000


# -------- Review Processing --------

def process_review(text):

    cleaned = clean_text(text)

    score, sentiment = analyze_sentiment(cleaned)

    return (text, score, sentiment)


# -------- Single Processing --------

def single_processing(data):

    start = time.time()

    results = []

    for text in data:
        results.append(process_review(text))

    end = time.time()

    return results, end-start


# -------- Thread Processing --------

def thread_processing(data):

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:

        results = list(executor.map(process_review, data))

    end = time.time()

    return results, end-start


# -------- Multiprocessing --------

def multiprocess_processing(data):

    start = time.time()

    with Pool(cpu_count()) as pool:

        results = pool.map(process_review, data)

    end = time.time()

    return results, end-start


# -------- Main Program --------

def main():

    print("\nLoading dataset...")

    data = load_dataset("Dataset.csv")

    print("Total Records:", len(data))


    # Chunk Processing

    chunks = create_chunks(data, CHUNK_SIZE)

    print("\nChunk Processing Result")
    print("-----------------------")

    print("Total rows:", len(data))
    print("Total chunks:", len(chunks))


    # Processing Engines

    single_res, single_time = single_processing(data)

    thread_res, thread_time = thread_processing(data)

    multi_res, multi_time = multiprocess_processing(data)


    print("\nProcessing Performance")
    print("-----------------------")

    print("Single Processing:", round(single_time,4), "sec")
    print("Thread Processing:", round(thread_time,4), "sec")
    print("Multiprocessing:", round(multi_time,4), "sec")


    fastest = min(single_time, thread_time, multi_time)

    if fastest == single_time:
        print("Fastest Method : Single")

    elif fastest == thread_time:
        print("Fastest Method : Thread")

    else:
        print("Fastest Method : Multiprocessing")


    # Sentiment Distribution

    print("\nSentiment Distribution")
    print("-----------------------")

    dist = Counter([r[2] for r in single_res])

    total = len(single_res)

    for k,v in dist.items():

        percent = round((v/total)*100,1)

        print(f"{k} : {v} ({percent} %)")



    # Database Operations

    print("\nDatabase Performance")
    print("-----------------------")

    create_table()

    insert_time = bulk_insert(single_res)

    q1, q2 = query_test()

    print("Bulk Insert Time:", round(insert_time,3), "sec")
    print("Query Before Index:", round(q1,3), "sec")
    print("Query After Index:", round(q2,3), "sec")

    print("Index Improvement:", round(q1/q2,2), "X Faster")


    # CSV Export

    export_to_csv()

    print("\nCSV Export Completed → output_results.csv")


    print("\nProject Execution Completed Successfully")


if __name__ == "__main__":

    main()