# print / dir / help /int / float /bool /
# bool / Nonetype / str / input / len

default_domain = 'goit.ua'

email = input("Enter your email:")
phone = input("Enter your phone:")


index = email.index('@')

nickname = email[:index]
domain = email[index+1:]
new_email = nickname + '@' + default_domain

print('nik: ', nickname)
print('Domen: ', domain)
print('nnewmail: ', new_email)
