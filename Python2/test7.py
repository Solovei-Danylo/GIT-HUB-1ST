def write_employees_to_file(employee_list, path):
    file = open(path, 'a')
    for somes in employee_list:
        for some in somes:
            print(some)
            file.write(some + '\n')
    print(file)

    file.close()


write_employees_to_file([['Robert Stivenson SSSSSSS,28', 'Alex Denver,30'], [
                        'Drake Mikelsson,19']], 'test.txt')
