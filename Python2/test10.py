
def choose_username():
    global username
    username = input("Введите логин: ")
    if len(username) > 5:
        print("Ваш логин сохранен.")
    else:
        print("Пожалуйста, выберите имя пользователя длиной более пяти символов.")
        choose_username()


def print_username():
    print(username)


#def main():
    #choose_username()
    #print_username()


#if __name__ == "__main__":
    #main()
