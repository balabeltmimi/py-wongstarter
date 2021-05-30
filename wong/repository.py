from model import Book


class BookRepository:
    books: list[Book]

    def __init__(self, books: list[Book]) -> None:
        self.books = books
