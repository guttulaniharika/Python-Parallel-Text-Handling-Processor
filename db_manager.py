import sqlite3
import time
import csv

DB = "project.db"


def create_table():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        score INTEGER,
        sentiment TEXT
    )
    """)

    conn.commit()
    conn.close()


def bulk_insert(data):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    start = time.time()

    cur.executemany(
        "INSERT INTO reviews(text,score,sentiment) VALUES (?,?,?)",
        data
    )

    conn.commit()

    end = time.time()

    conn.close()

    return end-start


def query_test():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    start = time.time()

    cur.execute("SELECT * FROM reviews WHERE score>0")
    cur.fetchall()

    t1 = time.time() - start

    cur.execute("CREATE INDEX IF NOT EXISTS idx_score ON reviews(score)")

    start = time.time()

    cur.execute("SELECT * FROM reviews WHERE score>0")
    cur.fetchall()

    t2 = time.time() - start

    conn.close()

    return t1, t2


def export_to_csv():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT text,score,sentiment FROM reviews")

    rows = cur.fetchall()

    with open("output_results.csv","w",newline="",encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["text","score","sentiment"])

        writer.writerows(rows)

    conn.close()