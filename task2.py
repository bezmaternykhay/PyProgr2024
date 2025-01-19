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

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Индетиикатор книги должно быть типа int")
        self.book_id = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.book_name = name

        if not isinstance(pages, int):
            raise TypeError("Колличество страниц в книге должно быть типа int")
        elif pages <= 0:
            raise TypeError("Колличество страниц в книге должно быть положительным числом")
        else:
            self.book_pages = pages

    def __str__(self) -> str:
        return f'''Книга "{self.book_name}"'''

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.book_id}, name='{self.book_name}', pages={self.book_pages})"

class Library:
    def __init__(self, books = []):
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типом List")
        self.books = books

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, book_ind) -> int:
        for index, Book in enumerate(self.books):
            if Book.book_id == book_ind:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
