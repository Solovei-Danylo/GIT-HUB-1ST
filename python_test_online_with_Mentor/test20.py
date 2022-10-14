# помощью анонимной функции извлеките из списка числа, делимые на 15.


x = [22, 15, 44, 90]


def test_true(numb):
    return not numb % 15  # not or not


print(list(filter(test_true, x)))
