if __name__ == "__main__":

    class Embroidery:
        """ Базовый класс вышивка """
        def __init__(self, colours: int, square: float):
            """
            Создание и подготовка к работе объекта родительского класса "Вышивка"

            :param colours: Кол-во цветов в вышивке
            :param square: Площадь вышиваемого дизайна

            Примеры:
            >>> embroidery = Embroidery(3, 2.15)  # инициализация экземпляра класса
            """
            self.colours = colours
            self.square = square

        def price(self, time_on_sew: float) -> int:
            """
            Подсчет стоимости вышивки с учетом затраченного времени !на вышивание!

            :param time_on_sew: Кол-во времени в часах
            :return: Стоимость вышивки

            Примеры:
            >>> embroidery = Embroidery(3, 2.15)
            >>> embroidery.price(5.15)
            """
            ...

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(colours={self.colours!r}, square={self.square!r})"

        def __str__(self) -> str:
            return f"Цвета {self.colours}. Площадь {self.square}"

    class MachineEmbroidery(Embroidery):
        """ Машинная вышивка """
        def __init__(self, colours: int, square: float, stitches: int):
            """
            Создание и подготовка к работе объекта дочернего класса "Машинная вышивка"

            :param colours: Кол-во цветов в вышивке
            :param square: Площадь вышиваемого дизайна
            :param stitches: Кол-во стежков в дизайне

            Примеры:
            >>> embroidery = MachineEmbroidery(3, 2.15, 1000)  # инициализация экземпляра класса
            """
            super().__init__(colours, square)
            self.stitches = stitches

        def price(self, time_on_design: float) -> int:
            """
            Подсчет стоимости вышивки с учетом кол-ва стежков и затраченного времени !на создание дизайна вышивки!

            :param time_on_design: Кол-во времени в часах
            :return: Стоимость вышивки

            Примеры:
            >>> embroidery = MachineEmbroidery(3, 2.15, 1000)
            >>> embroidery.price(5.15)
            """
            ...

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(colours={self.colours!r}, square={self.square!r}, stitches={self.stitches!r})"

    pass
