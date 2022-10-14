free_list = [2, 5, 6, 7, 7, 7]       # Создать произвольный список

free_list.append("hello")  # Добавить новый элемент типа str в конец списка
# free_list.extend тоже самое +- ???????
print(free_list)

# Добавить новый элемент типа int на место с индексом
free_list.insert(3, 5)
print(free_list)

# Добавить новый элемент типа list в конец списка
free_list.append(['a', 'bbb', 'dddsd'])
print(free_list)

# Добавить новый элемент типа tuple на место с индексом
free_list[1] = (6666, 77777, 88888)
print(free_list)
# help(free_list)

# Получить элемент по индексу
info_list_index = free_list[1]
print(info_list_index)

# Удалить элемент
delete_index = free_list.remove("hello")
print(delete_index)  # не выводит нефига
print(free_list)

# Найти число повторений элемента списка
searching_element = free_list.count(7)
print(searching_element)
print(free_list)

# free_list.add(["333"])
# print(free_list)
