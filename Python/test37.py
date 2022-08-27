from functools import partial
SPAM_DOMAINS = ('yandex.ru', 'rambler.ru', 'mail.ru', 'ya.ru')

#email = input("Enter email: ")


def check_email(email):
    if ("@" not in email):
        return False
    if email.count("@") > 1:
        return False
    parts = email.split('@')

    if '.' not in parts[1]:
        return False
    if parts[1].endswith('.ru'):
        return False
    if len(parts[0]) < 2:
        return False
    if parts[1] in SPAM_DOMAINS:
        return False

    print(parts)
    return True


if __name__ == '__main__':
    email = input("Enter email: ")
    print(check_email(email))
