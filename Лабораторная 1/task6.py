list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate(list_numbers):   #получен индекс максмального числа
    if current_number >= max_number:
        max_number = current_number
        max_index = i

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]   #меняем местами

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
