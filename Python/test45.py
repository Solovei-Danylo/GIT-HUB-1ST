points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    index = 0
    if len(coordinates) <= 1:
        return 0
    while index < len(coordinates) - 1:
        first_elem = coordinates[index]
        index = index + 1
        next_element = coordinates[index]
        if next_element < first_elem:
            distance += points.get((next_element, first_elem))
        else:
            distance += points.get((first_elem, next_element))
    return distance
