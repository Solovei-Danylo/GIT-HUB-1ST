from ast import arg


def print_name(name, age, status):
    print(name, age, status)


def summary(x: int | float, y: int | float, *args, **kwargs) -> int | float:
    print(args, type(args))
    print(kwargs, type(kwargs))
    print_name(**kwargs)
    return x+y


#print(summary(1, 2, 3, ["5"], "7", name="Alex", age=2, status=True))
