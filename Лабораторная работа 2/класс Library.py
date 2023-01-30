from typing import Optional

from pydantic import BaseModel

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

# TODO написать класс Library
class Library(BaseModel):
    books: Optional[list]

    def get_next_book_id(self) -> int:
        if self.books == None:
            return 1
        else:
            return (BOOKS_DATABASE[1]["id"] + 1)

    def get_index_by_book_id(self, index: int) -> int:
        if self.books == None:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            for i, key in enumerate(BOOKS_DATABASE):
                if key["id"] == index:
                    return i

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
