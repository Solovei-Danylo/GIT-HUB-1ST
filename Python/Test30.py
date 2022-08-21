n = 50
k = 0


def factorial(n=50):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n=50, k=0):
    if n >= 1:
        n = n - 1
    k = n / ((n - k) * k)
    return int(k)


print(number_of_groups)
print(factorial)
