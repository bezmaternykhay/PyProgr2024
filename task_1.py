import doctest
"""Библиотека"""

class Book:
    def __init__(self, title: str, authors_name: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param authors_name: Автор книги

        Примеры:
        >>> book1 = Book('Александр Сергеевич Пушкин', 'Капитанская дочка')  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        self.title = title

        if not isinstance(authors_name, str):
            raise TypeError("Имя автора должно быть типа str")
        self.authors_name = authors_name

    def on_shelf(self, shelf_id: int)-> None:
        """
        Функция, которая назначает местоположение книги на полке в бибилиотке

        :raise TypeError: Если вместо номера полки дан неликвидный тип данных (не число).
        :raise ValueError: Если номер полки отрицательный.

        Примеры:
        >>> book1 = Book('Александр Сергеевич Пушкин', 'Капитанская дочка')
        >>> book1.on_shelf(13)
        """
        if not isinstance(shelf_id, int):
            raise TypeError("Номер полки должен быть типа int")
        if shelf_id <= 0:
            raise ValueError("Номер полки должен быть положительным числом")

    def reservation(self, reader_id: int) -> None:
        """
        Бронирование книги

        :param reader_id: Id читателя в системе

        :raise TypeError: Если вместо id читателя дан неликвидный тип данных (не число).
        :raise ValueError: Если id читателя отрицательный.

        Примеры:
        >>> book1 = Book('Александр Сергеевич Пушкин', 'Капитанская дочка')
        >>> book1.reservation(124)
        """
        if not isinstance(reader_id, int):
            raise TypeError("Id читателя должен быть типа int")
        if reader_id <= 0:
            raise ValueError("Id читателя должен быть положительным числом")
        ...

class Librarian:
    def __init__(self, lib_name: str, service_number: int):
        """
        Создание и подготовка к работе объекта "Библиотекарь"

        :param name: Имя работника
        :param service_number: Табельный номер

        Примеры:
        >>> librarian1 = Librarian('Александрова Александра Александровна', 19877)  # инициализация экземпляра класса
        """
        if not isinstance(lib_name, str):
            raise TypeError("Имя работника должно быть типа str")
        self.lib_name = lib_name

        if not isinstance(service_number, int):
            raise TypeError("Табельный номер должен быть типа int")
        self.service_number = service_number

    def is_busy(self, lib_busy:bool) -> None:
        """
        Функция, которая назначает работнику состояние типа занят/не занят

        Примеры:
        >>> librarian1 = Librarian('Александрова Александра Александровна', 19877)
        >>> librarian1.is_busy(True)
        """
        if not isinstance(lib_busy, bool):
            raise TypeError("Занят или нет - состояние типа bool")
        ...

    def ask_for_help(self, book_name: str) -> int:
        """
        Функция, которая спрашивает у бибилиотеря где находится книга

        :param book_name: Название книги
        :return: Номер полки с книгой (если такой книги нет, можно вернуть -1)
        :raise TypeError: Если на вход дали не название книги (не тип str).

        Примеры:
        >>> librarian1 = Librarian('Александрова Александра Александровна', 19877)
        >>> librarian1.ask_for_help('Война и мир')
        """
        if not isinstance(book_name, str):
            raise TypeError("Имя книги должно быть типа str")
        ...

class Bookshelf:
    def __init__(self, number: int, capacity: int):
        """
        Создание и подготовка к работе объекта "Книжная полка"

        :param number: Порядковый номер полки в библиотки
        :param number: Количество книг, которое поместится на полку

        Примеры:
        >>> bookshelf1 = Bookshelf(22, 10)  # инициализация экземпляра класса
        """
        if not isinstance(number, int):
            raise TypeError("Номер полки должен быть типа int")
        self.number = number

        if not isinstance(capacity, int):
            raise TypeError("Объем полки должно быть типа int")
        self.capacity = capacity

    def is_empty(self) -> int:
        """
        Функция, которая возвращает количество доступных мест для книг
        :return: Количество доступных мест для книг (0, если полка полностью забита книгами)
        Примеры:
        >>> bookshelf1 = Bookshelf(22, 10)
        >>> bookshelf1.is_empty()
        """
        ...

    def adding_book(self, add_book: Book) -> None:
        """
        Функция, которая добавляет книгу на полку

        :param book_name: Название книги
        :raise TypeError: Если на вход дали не название книги (не тип str).

        Примеры:
        >>> book1 = Book('Александр Сергеевич Пушкин', 'Капитанская дочка')
        >>> bookshelf1 = Bookshelf(22, 10)
        >>> bookshelf1.adding_book(book1)
        """
        if not isinstance(add_book, Book):
            raise TypeError("На входе должна быть книга")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации