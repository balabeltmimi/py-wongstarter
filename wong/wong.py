from loader import load_db


def main():
    books = load_db('./book-db.csv')
    # TODO: query from author, hardest book, date range
    repository = BookRepository(books)
    result = repository.find_by_author('Dan')
    # TODO: render result from query
    # Note: flake8 -> should have newline at the end of file
