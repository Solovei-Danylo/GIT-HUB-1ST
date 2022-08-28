
table = {
    "F": {"Assessment": 1, "point": "0-34", "description": "Unsatisfactorily"},
    "FX": {"Assessment": 2, "point": "35-59", "description": "Unsatisfactorily"},
    "E": {"Assessment": 3, "point": "60-66", "description": "Enough"},
    "D": {"Assessment": 3, "point": "67-74", "description": "Satisfactorily"},
    "C": {"Assessment": 4, "point": "75-89", "description": "Good"},
    "B": {"Assessment": 5, "point": "90-95", "description": "Very good"},
    "A": {"Assessment": 5, "point": "96-100", "description": "Perfectly"}
}


def get_grade(key):
    if table.get(key):
        return table[key]['Assessment']
    print(key)


def get_description(key):
    if table.get(key):
        return table[key]['description']
    print(key)


get_grade()
get_description()
print(get_grade)
print(get_description)
