# TODO написать функцию для получения списка уникальных целых чисел
import random

def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15
    list_ = random.sample(range(start, stop), count)

    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
