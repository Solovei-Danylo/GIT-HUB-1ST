"""cоздайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».
"""


"""def three_args(var1, var2=None, var3=None):
    result = f"Переданы аргументы: var1 = {var1}"
    if var2 is not None:
        result += f" var2 = {var2}"
        # print(var2)
    if var3 is not None:
        result += f" var3 = {var3}"
        # print(var3)
    return result"""


def three_args(var1, var2=None, var3=None):
    #args = locals().items()
    arguments = [f"{arg[0]} = {arg[1]}" for arg in locals().items()
                 if arg[1] is not None]
    print(arguments)
    return f"Переданы аргументы: {', '.join(arguments)}"


print(three_args(1, 2,))


#example = [i for i in range(10) if i//2 == 0]
