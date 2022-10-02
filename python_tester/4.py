def tester(x, *args):
    print(args)
    return x + len(args)


print(tester(11, 21, 3))
