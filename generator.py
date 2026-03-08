import csv
import random

samples=[
"this product is really good",
"average product nothing special",
"happy with the purchase",
"not satisfied with this item",
"very bad quality item",
"terrible delivery experience"
]

def generate(path,n):

    with open(path,"w",newline="",encoding="utf-8") as f:

        writer=csv.writer(f)

        writer.writerow(["text"])

        for _ in range(n):

            writer.writerow([random.choice(samples)])