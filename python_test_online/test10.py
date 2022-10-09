# Вы принимаете от пользователя последовательность
# чисел, разделённых запятой. Составьте список и
# кортеж с этими числами.


test1 = []  # Список . Робити шо хош
test2 = ()  # Кортеж - тюпл. Не змінна
test3 = {}  # Словник. Ключ значення.
test4 = set([])  # Множинні . Унікальні і швидкі


def cleaner_list():
    input_text = input("Input please : чисел, разделённых запятой: ")
    test1 = input_text.split(',')
    test2 = tuple(input_text.split(","))
    print(test1, test2)


2

print(cleaner_list())
