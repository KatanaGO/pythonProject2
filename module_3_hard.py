def calculate_structure_sum(data):
    total_sum = 0  # Переменная для хранения итоговой суммы

    # Проверяем каждый элемент
    if isinstance(data, (int, float)):  # Если элемент - число
        total_sum += data
    elif isinstance(data, str):  # Если элемент - строка
        total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):  # Если элемент - коллекция
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для каждого элемента
    elif isinstance(data, dict):  # Если элемент - словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Рекурсивный вызов для ключа
            total_sum += calculate_structure_sum(value)  # Рекурсивный вызов для значения

    return total_sum  # Возвращаем итоговую сумму

# Пример данных
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции
result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99
