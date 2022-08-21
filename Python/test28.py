def get_fullname(first_name, last_name, middle_name):
    if middle_name != 0 or " ":
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"


get_fullname(first_name=input("Enter your First name: "),
             last_name=input("Enter your Last name: "),
             middle_name=input("Enter your Middle name: "))


print(get_fullname)
print = input("SSSS?")
