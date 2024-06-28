def send_email(message, recipient, sender = 'ipatova.dasha@gmail.com'):
    if not ('@' in recipient and '@' in sender and (recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'ipatova.dasha@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Здравствуйте, высылаю на проверку документы о перевод.', 'alina.bercova@mail.ru' )

send_email('Проверка завершена! Отличный результат.', 'ipatova.dasha@gmail.com' )

send_email('Перевод оформлен.', 'alina.bercova@mail.u' )

send_email('Здравствуйте, добро пожаловать в команду.', 'alina.bercova@mail.ru', 'oleg1971@bk.ru' )