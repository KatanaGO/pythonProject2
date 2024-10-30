# Функция для отправки email с проверками
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка корректности e-mail отправителя и получателя
    if ("@" not in sender or not sender.endswith((".com", ".ru", ".net"))) or \
       ("@" not in recipient or not recipient.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    # Проверка на отправку самому себе
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    # Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    # Обработка нестандартного отправителя
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

# Тестовые вызовы функций
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
