count = 0
while True:

    count = count + 1
    age = input("How old are u : ")
    age = int(age)
    try:
        if age >= 18:
            print("You are welcome !")
        if age < 18:
            print("Cannot enter for u, need be 18+ :")
        if age == "":
            print("Error")
        if count >= 5:
            break
    except:
        print("somes wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
