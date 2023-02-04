class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

class PaperBook(Book):
    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        if not isinstance(pages, (int)):
            raise TypeError("Кол-во страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Книга должна иметь положительное и отличное от нуля кол-во страниц")
        self.pages = pages

class AudioBook(Book):
    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        if not isinstance(duration, (float)):
            raise TypeError("Длительность аудиокниги должно быть типа float")
        if duration <= 0:
            raise ValueError("Книга должна иметь положительную и отличную от нуля длительность")
        self.duration = duration

if __name__ == "__main__":
    book_1 = Book("Мастер и Маргарита", "Булгаков")
    print(book_1.__str__())

    book_2 = PaperBook(150, "Мастер и Маргарита", "Булгаков")
    print(book_2.__str__())

    book_3 = AudioBook(220.8 , "Мастер и Маргарита", "Булгаков")
    print(book_3.__str__())




