from numbers import Integral
from random import randint
import string


def get_random_password():
    password = ""
    for _ in range(8):
        password += chr(randint(40, 126))
    print(password)
    return password


test = get_random_password
test = Integral.test
print(test)
