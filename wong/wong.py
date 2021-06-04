from model import Book
from loader import load_db
from render import render_table
from repository import BookRepository


def main():
    books = load_db('./book-db.csv')
    # TODO: query from author, hardest book, date range
    repository = BookRepository(books)
    result = repository.find_by_author('Dan')
    # TODO: render result from query
    render_table(result)
    # Note: flake8 -> should have newline at the end of file


if __name__ == '__main__':
    main()
