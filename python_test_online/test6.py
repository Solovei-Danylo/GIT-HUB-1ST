# Напишите код, который переводит целое число в строку,
# при том что его можно применить в любой системе счисления

chislo3 = "Hello world"
chislo4 = []

for word in chislo3:
    chislo4.append(bin(ord(word)))
print(chislo4)

test_dict = {"o": 8, "b": 2, "x": 16}
# 10 # 12 ??????   ^^^   ## 2 and 16 must be ^^^^^
chislo5 = ""
for cyfra in chislo4:
    print(cyfra[1])
    if cyfra[1] in test_dict:
        base = test_dict[cyfra[1]]
        cyfra2 = cyfra[2:]
        cyfra2 = int(cyfra2, base)
        chislo5 += chr(cyfra2)
        print(cyfra2, chislo5)

# cyfra2 = int(cyfra2, 8)  # 2 якої системи обчислення!!!!
#chislo5 += chr(cyfra2)
# print(cyfra2)


print(chislo5)


chislo = 4
chislo2 = str(chislo)
# print(chislo2)


#print(int("FF", 16))
#print(int("1000", 2))
# print(bin(8))
