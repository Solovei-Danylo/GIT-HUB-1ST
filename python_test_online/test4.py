# Напишите программу для слияния нескольких словарей в один.


vocalabura = {"a": 55, "b": 33, "c": 22, "d": 99}
vocalabura2 = {"e": 115, "f": 133, "g": 212, "h": 919}


vocalabura3 = {**vocalabura, **vocalabura2}

print(vocalabura3)

for vocal in vocalabura, vocalabura2:
vocalabura3.update(vocal)

print(vocalabura3)
