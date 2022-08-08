

phone = input('Enter your phone number : ')

if '050' in phone[0:5]:
    print('Your mobile operator is Vodaphone ')

elif '063' in phone[0:5]:
    print('Your mobile operator is Life ')

elif '067' in phone[0:5]:
    print('Your mobile operator is Kyivstar ')

else:
    print('This is uknowns operator :')

print('Program is completed.')
