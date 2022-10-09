# Задача 2
# Даны списки:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
for number in a:
    if number in b:
        result.append(number)
# print(number)
print(result)


result = list(filter(lambda elem: elem in b, a))
result = [elem for elem in a if elem in b]
result = list(set(a) & set(b))
