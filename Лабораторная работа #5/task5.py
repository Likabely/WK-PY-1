# TODO написать функцию генерации случайных паролей
import random
import string

def get_random_password() -> str:
    n = 8
    letters_upper = string.ascii_uppercase
    letters_lower = string.ascii_lowercase
    digits = string.digits
    str_ = random.sample(letters_upper + letters_lower + digits, n)

    return "".join(str_)

print(get_random_password())
