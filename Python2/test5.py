def sanitize_phone_number(phone: str):
    print("old phone:", phone)

    for exc in ('-', '(', '+', ')', ' '):
        print("variable exc:", exc)

        phone = phone.replace(exc, '')

        print(phone)

    return phone


result = sanitize_phone_number(" +380(97)555-78-98   ")

print("new phone:", result)
