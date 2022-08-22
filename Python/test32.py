
while True:
    import random
    num = random.randint(1, 10)
    guess = int(input('Введите число от 1 до 10: '))
    if guess == num:
        print('Угадали!')
        break
    elif guess > 10:
        print('Число не может быть больше 10')
    elif guess < 1:
        print('Число не может быть меньше 1')
    else:
        print('Извините, было загадано число ', num)
