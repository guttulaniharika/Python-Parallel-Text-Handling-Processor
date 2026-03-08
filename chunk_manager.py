import csv

def load_dataset(path):

    data = []

    with open(path, "r", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            # try different possible column names
            if "text" in row:
                data.append(row["text"])

            elif "review" in row:
                data.append(row["review"])

            elif "content" in row:
                data.append(row["content"])

    return data


def create_chunks(data, size):

    chunks = []

    for i in range(0, len(data), size):
        chunks.append(data[i:i+size])

    return chunks