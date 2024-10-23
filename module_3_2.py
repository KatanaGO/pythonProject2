# Функция для отправки email с проверками
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на валидный email (наличие "@" и окончание на ".com", ".ru", ".net")
    if "@" not in recipient or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        # Проверка на отправку самому себе
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        # Проверка на отправителя по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        # Сообщение о нестандартном отправителе
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Тестовые вызовы функций
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
