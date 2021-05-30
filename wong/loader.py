import csv
# stdlib

# 3rd party lib

# local package
from model import Book


def load_db(filename: str) -> list[Book]:
    books = []

    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            books.append(row)

    return books
