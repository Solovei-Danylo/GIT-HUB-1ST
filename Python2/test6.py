#doc = open('test.txt')


def total_salary():
    total_salary = 0
    f = open('test.txt', "r")
    try:
        while True:
            line = f.readline()
            if not line:
                break
            values = line.split(",")
            total_salary += float(values[1])
        print(total_salary)
        return total_salary

    finally:
        f.close()


total_salary()
#test = str(total_salary)
# print(test)
