num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(num):
        sum += i + 1

    num = int(input("Enter integer (0 for output): "))
print(num)
print(sum)
print(i)
