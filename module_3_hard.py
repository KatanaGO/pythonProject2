def calculate_structure_sum(data):
    total_sum = 0  # Переменная для хранения итоговой суммы

    # Обрабатываем каждый элемент в data
    for item in data:
        if isinstance(item, (int, float)):  # Если элемент число
            total_sum += item
        elif isinstance(item, str):  # Если элемент строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент коллекция
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Если элемент словарь
            for key, value in item.items():
                if isinstance(key, str):
                    total_sum += len(key)  # Добавляем длину ключа
                total_sum += calculate_structure_sum([value])  # Рекурсивный вызов для значения

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
print(result)  # Вывод: 99
