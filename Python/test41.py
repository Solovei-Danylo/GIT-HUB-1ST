from operator import ge


def get_grade(key):
    grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    return grade.get(key)


def get_description(key):
    description = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
                   "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    return description.get(key)


get_grade()
get_description()
print(get_grade)
print(get_description)
