source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


def save_applicant_data(source, output):
    with open(output, "w") as f:
        students = [student.values() for student in source]
        for student in students:
            f.write(', '.join([str(item) for item in student]) + "\n")

    # f.write("test")


save_applicant_data(source=source, output="student.txt")


# source2 = {
# "name": "Kovalchuk Oleksiy",
# "specialty": 301,
# "math": 175,
# "lang": 1,
# "eng": 0,
# }
#print([bool(source) for source in source2.values()])
