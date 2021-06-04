from ward import test

from repository import BookRepository


@test('test find by author and should return list of book')
def _():
    books = [
        {
            'name': 'Belt book',
            'author': 'Belt',
        },
        {
            'name': 'The girl book',
            'author': 'John',
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_author(name='Belt')
    assert 1 == len(actual)
    assert 'Belt' == actual[0]['author']
