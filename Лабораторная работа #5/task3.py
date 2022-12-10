# TODO написать функцию для получения списка уникальных целых чисел
from random import randint

def get_unique_list_numbers(start: int, stop: int, count: int) -> list[int]:
    list_unique_ = []
    while len(list_unique_) < count:
        num = randint(start, stop)
        if num not in list_unique_:
            list_unique_.append(num)

    return list_unique_

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
