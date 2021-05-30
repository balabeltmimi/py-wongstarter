#   import lib should be alphabetal orderlly
from datetime import date
from typing import TypedDict
#   gap between import and core code shall be
#   2 lines gap interval -> flake8 convention


class Book(TypedDict):
    name: str
    author: str
    length: int
    language: str
    publication_date: date
    isbn13: str
    publisher: str
