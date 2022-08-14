result = None
operand = None
operator = None
wait_for_number = True

while True:
    if operator == '=':
        break
    while True:
           try:
                if result == None:
                    result = int(input('>>>'))
                    print(result)
                    break
                else:
                    operand = int(input('>>>'))
                    if type(operand) == int:
                        if operator == '+':
                            result += operand
                            break
                        elif operator == '-':
                            result -= operand
                            break
                        elif operator == '*':
                            result *= operand
                            break
                        elif operator == '/':
                            result /= operand
                            break
                        elif operator == '=':
                            break
                    else:
                        print(f"{operand} is not a number. Try again")
                        continue
            except ValueError:
                print(f'{operand} is not a num.')
while True:
    operator = input('>>>')
    if operator in ("+", '-','*','/','='):
        break
    else:
        print(f"{operator} is not '+' or '-' or '/' or '*'.")
        continue
