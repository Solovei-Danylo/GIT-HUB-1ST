# Напишите программу, которая принимает два
# списка и выводит все
# элементы первого, которых нет во втором.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

# for number in a:
# if number not in b:
# result.append(number)
# print(result)


#result = list(filter(lambda number: number not in b, a))
# print(result)
#result = [elem for elem in a if elem not in b]
# print(result)
result = list(set(a) - set(b))
print(result)
