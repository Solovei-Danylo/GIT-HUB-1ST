# Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874,
           'c': 560, 'd': 400, 'e': 5874, 'f': 20}


my_dict2 = sorted(my_dict.items(), key=lambda arg: arg[1], reverse=True)
print(my_dict2)

my_dict2 = [my_dict2[0], my_dict2[-1]]

my_dict3 = []

for dict in my_dict2:
    my_dict3.append(dict[0])


print(my_dict2)
print(my_dict3)
