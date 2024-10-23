def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Получаем первую цифру как число
        first = int(str_number[0])
        # Рекурсивно умножаем первую цифру на произведение оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась только одна цифра, возвращаем её
        return int(str_number)


# Вызов функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
