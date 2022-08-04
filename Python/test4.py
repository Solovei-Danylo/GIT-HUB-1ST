
DEFAULT_DOMAIN = "goit.ua"

email = input("Enter your email: ")
phone = input("Enter yourphone number: ")

# "serg@gmail.com"
# "sergdsds.sdsdsds.sdsd@gmail.com"

index = email.index('@')

nickname = email[:index]

domain = email[index+1:]
new_email = nickname + '@' + DEFAULT_DOMAIN

print('Нік: ', nickname)
print('Домен: ', domain)
print('Домен: ', domain)
print('Новий email: ', new_email)
