import email


email = input("Enter your email: ")
phone = input("Enter yourphone number: ")

# "serg@gmail.com"
# "sergdsds.sdsdsds.sdsd@gmail.com"

index = email.index('@')

nickname = email[:index]

domain = email[index+1:]
print('Нік: ', nickname)
print('Домен: ', domain)
