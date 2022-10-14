# Напишите проверку на то, является ли строка
# палиндромом. Палиндром — это слово или фраза,
# которые одинаково читаются слева направо и справа налево.


def is_palindrom(potentional_palidrom: str) -> bool:

    #palidrom = potentional_palidrom.upper()
    potentional_palidrom = potentional_palidrom.upper()
    print(potentional_palidrom)
    print(list(reversed(potentional_palidrom)))
    print(''.join(list(reversed(potentional_palidrom))))
    return potentional_palidrom == ''.join(list(reversed(potentional_palidrom)))


print(is_palindrom("Kazak"))
