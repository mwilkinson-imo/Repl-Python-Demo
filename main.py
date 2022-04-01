import json
from typing import List

from models.book import Book


def main() -> None:
    books = fetch_all_books()
    output = json.dumps(books, indent=4)
    print(output)


def fetch_all_books() -> List[Book]:
    with open('samples/data.json', 'rb') as input:
        books = json.load(input)
        return books

# Feature-Request: Clients want to be able to display the names of the Authors we support.
def get_authors():
    pass

# Feature-Request: Our support teams want to be able to add new books we support to our data store.
def add_book():
    pass

# Feature-Request: Clients want to be able to search for books by a certain author.
def get_books_by_author_name():
    pass

# Feature-Request: Clients want to be able to search for books within a genre.
def get_books_by_genre():
    pass


if __name__ == '__main__':
    main()
