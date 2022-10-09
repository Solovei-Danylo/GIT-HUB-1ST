# Отсортируйте словарь по значению в порядке возрастания и убывания

vocalabura = {"a": 55, "b": 33, "c": 22, "d": 99}

new_vocalab = {}


def fnc(arg):
    return arg[1]


print(vocalabura.items())
print(dict(sorted(vocalabura.items(), key=fnc, reverse=True)))

print(dict(sorted(vocalabura.items(), key=lambda arg: arg[1], reverse=True)))


#print(list(filter(lambda elem: elem < 5, a)))
