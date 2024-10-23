def single_root_words(root_word, *other_words):
    # Создаем пустой список для подходящих слов
    same_words = []

    # Приводим root_word к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем условие, что одно слово содержится в другом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем в список подходящее слово

    return same_words  # Возвращаем список подходящих слов


# Вызовы функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на консоль
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
