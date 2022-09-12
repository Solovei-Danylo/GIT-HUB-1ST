def read_employees_from_file(path):
    list = []
    file = open(path, 'w')
    new = file.readlines()
    for n in new:
        n.strip('\n')
        list.append(1)
    print(list)
    file.close()


read_employees_from_file(path)
