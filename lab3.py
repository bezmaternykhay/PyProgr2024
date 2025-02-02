class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.__name = name
        self.__author = author

        if not isinstance(pages, int):
            raise TypeError("Колличество страниц в книге должно быть типа int")
        elif pages <= 0:
            raise TypeError("Колличество страниц в книге должно быть положительным числом")
        else:
            self.pages = pages

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.__name = name
        self.__author = author

        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должно быть типа float")
        elif duration <= 0:
            raise TypeError("Продолжительность книги должно быть положительным числом")
        else:
            self.duration = duration

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.duration!r})"