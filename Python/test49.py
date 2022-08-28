def is_valid_password(password: str):
    if len(password) != 8:
        return False

    isdigit = False
    isupper = False
    islower = False

    for x in password:
        if x.isdigit():
            isdigit = True
        elif x.isupper():
            isupper = True
        elif x.islower():
            islower = True

    return (isdigit, isupper, islower)
