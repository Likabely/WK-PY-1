# TODO написать функцию генерации случайных паролей
from random import sample
from string import ascii_uppercase, ascii_lowercase, digits

def get_random_password(n: int) -> str:
    str_ = sample(ascii_uppercase + ascii_lowercase + digits, n)

    return "".join(str_)

print(get_random_password(8))
