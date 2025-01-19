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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
