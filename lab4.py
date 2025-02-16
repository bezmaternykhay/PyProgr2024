class Drink:
    """Описание напитка в ресторане"""
    def __init__(self, price: int, volume: int):
        """
        Инициализация класса Напиток
        :param price: цена
        :param volume: объем
        """
        self.__price = price
        self.__volume = volume

    def __str__(self):
        return f"Напиток. Объем: {self.__volume} мл. Цена: {self.__price} руб."

    def __repr__(self):
        return f"{self.__class__.__name__}(volume={self.__volume!r}, price={self.__price!r})"

    def _pour(self, tare = "glass") -> None:
        """
        Метод наливает напиток в указанную тару
        :param tare: тара
        """
        print(f"{self.__class__.__name__} is poured into {tare}")

    def _put(self, place = "table") -> None:
        """
        Метод ставит стакан с напитком в указанное место
        :param place: место
        """
        print(f"{self.__class__.__name__} served on the {place}")

    def serve_to_the_guest(self) -> None:
        """Метод позволяет подать напиток гостю"""
        self._pour()
        self._put()

class Coffee(Drink):
    """Описание напитка Кофе в ресторане"""
    def __init__(self, price: int, volume: int, country: str, saturation: str):
        """
        Инициализация класса Кофе
        :param price: цена
        :param volume: объем
        :param country: Старана произрастания
        :param saturation: Насыщенность
        """
        self.__price = price
        self.__volume = volume
        self.__country = country
        self.__saturation = saturation

    def __str__(self):
        return f"Кофе. Объем: {self.__volume} мл. Цена: {self.__price} руб. Старана произрастания: {self.__country}. Насыщенность: {self.__saturation}."

    def __repr__(self):
        return f"{self.__class__.__name__}(volume={self.__volume!r}, price={self.__price!r}, country={self.__country!r}, saturation={self.__saturation!r})"

    def _brew(self, temperature = 94)  -> None:
        """Метод позволяет заварить кофе"""
        print(f"{self.__class__.__name__} is brewed at a temperature of {temperature} deg")

    def serve_to_the_guest(self) -> None:
        self._brew()
        self._pour()
        self._put()

if __name__ == "__main__":
    # Проверка работспособности кода
    drink1 = Drink(650, 400)
    latte = Coffee(740, 300, "Колумбия", "Средняя")
    print(drink1)
    print(latte)
    print(repr(drink1))
    print(repr(latte))
    drink1.serve_to_the_guest()
    latte.serve_to_the_guest()
