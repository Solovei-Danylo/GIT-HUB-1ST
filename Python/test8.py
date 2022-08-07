x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))

        if x == 0:
            print("X can`t be equal to zero")
            x = int(input("X: "))

result = y / x
result = int(result)
print(result)
