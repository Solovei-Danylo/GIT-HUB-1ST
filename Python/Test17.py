
work_experience = int(input("Enter your full work experience in years: "))

if work_experience >= 5:
    developer_type = "Senior"
elif work_experience < 1:
    developer_type = "Junior"
elif work_experience >= 1:
    developer_type = "Middle"

print(developer_type)
