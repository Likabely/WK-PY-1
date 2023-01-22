import doctest

class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        """
        ...

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.

        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.
        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        ...

class Krasnyj_diplom:
    def __init__(self, number_five: int, number_four: int):
        """
        Создание и подготовка к работе объекта "Красный диплом"

        :param number_five: кол-во пятёрок
        :param number_four: кол-во четвёрок

        Примеры:
        >>> diplom = Krasnyj_diplom(10, 1)  # инициализация экземпляра класса
        """
        if not isinstance(number_five, int):
            raise TypeError("Кол-во пятёрок должно быть типа int")
        if number_five <= 0:
            raise ValueError("Кол-во пятёрок не должно быть меньше или равно нулю")
        self.number_five = number_five

        if not isinstance(number_four, int):
            raise TypeError("Кол-во четвёрок должно быть типа int")
        if number_four > number_five:
            raise ValueError("Красного диплома не будет :(")
        self.number_four = number_four

    def average_mark(self, average: float) -> None:
        """
        Функция, которая проверяет средний балл диплома

        :param average: Средний балл
        :raise ValueError: Если среднй балл ниже 4,75
        :return: Средний балл диплома

        Примеры:
        >>> diplom = Krasnyj_diplom(10, 1)
        >>> diplom.average_mark(4.85)
        """
        if not isinstance(average, float):
            raise TypeError("Средний балл должен быть типа float")
        if average < 4.75:
            raise ValueError("Средний балл ниже проходного")
        ...

    def have_three(self, number_three: int) -> bool:
        """
        Функция проверяет наличие троек.

        :param number_three: Кол-во троек
        :raise ValueError: Если кол-во троек меньше нуля
        :return: Есть ли тройки

        Примеры:
        >>> diplom = Krasnyj_diplom(10, 1)
        >>> diplom.have_three(0)
        """
        if not isinstance(number_three, int):
            raise TypeError("Кол-во троек должно быть типа int")
        if number_three < 0:
            raise ValueError("Кол-во троек не должно быть меньше нуля")
        ...

class Instagram:
    def __init__(self, number_likes: int, number_followers: int):
        """
        Создание и подготовка к работе объекта "Инстаграм"

        :param number_likes: Кол-во лайков
        :param number_followers: Кол-во подписчиков

        Примеры:
        >>> insta = Instagram(500, 100)  # инициализация экземпляра класса
        """
        if not isinstance(number_likes, int):
            raise TypeError("Кол-во лайков должно быть типа int")
        if number_likes < 0:
            raise ValueError("Кол-во лайков не должно быть отрицательным")
        self.number_likes = number_likes

        if not isinstance(number_followers, int):
            raise TypeError("Кол-во подписчиков должно быть типа int")
        if number_followers < 0:
            raise ValueError("Кол-во подписчиков не должно быть отрицательным")
        self.number_followers = number_followers

    def add_repost(self, repost: int) -> None:
        """
        Репост поста.

        :param repost: Кол-во репостов
        :raise ValueError: Если кол-во репостов отрицательное
        :return: Кол-во репостов

        Примеры:
        >>> insta = Instagram(500, 100)
        >>> insta.add_repost(1)
        """
        if not isinstance(repost, int):
            raise TypeError("Кол-во репостов должно быть типа int")
        if repost < 0:
            raise ValueError("Кол-во репостов должно быть положительным числом")
        ...

    def other_girls(self, other_likes: int) -> bool:
        """
        Поиск лайков на фотографиях у других девушек.

        :param other_likes: Лайки на фотографиях у других девушек
        :raise ValueError: Если количество лайков меньше нуля
        :return: Нужно ли расставаться с парнем

        Примеры:
        >>> insta = Instagram(500, 100)
        >>> insta.other_girls(0)
        """
        if not isinstance(other_likes, int):
            raise TypeError("Кол-во лайков должно быть типа int")
        if other_likes < 0:
            raise ValueError("Кол-во лайков не должно быть меньше нуля")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
