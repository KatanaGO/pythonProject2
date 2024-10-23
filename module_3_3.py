def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции
print_params()                      # Без аргументов
print_params(10)                    # Только a
print_params(10, 25)                # a и b
print_params(10, 25, False)         # Все три аргумента
print_params(b=25)                  # Изменяем только b
print_params(c=[1, 2, 3])           # Изменяем только c

# Распаковка параметров
values_list = [3.14, 'Hello', False]
values_dict = {'a': 42, 'b': 'World', 'c': False}

print_params(*values_list)          # Используя список
print_params(**values_dict)         # Используя словарь

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)    # Распаковка и передача 42
