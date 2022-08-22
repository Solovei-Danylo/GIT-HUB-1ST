while True:
    try:
        a = input("Введите число: ")
        b = input("Введите еще одно число: ")
        a = int(a)
        b = int(b)
        print(a / b)
        break
    except ZeroDivisionError and ValueError:
        print("b не может быть нулем или символом!")
