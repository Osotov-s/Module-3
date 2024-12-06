def check_substrings(string, substrings=[".com", ".ru", ".net"]):
    for s in substrings:
        if string.endswith(s):
            return True

    return False


def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or not check_substrings(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif "@" not in recipient or not check_substrings(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
            print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("hello", "uiversity.help@gmail.net")