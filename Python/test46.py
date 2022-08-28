def game(terra, power):
    for i in terra:
        for x in i:
            if x > power:
                break
            power += x
    return power


def game(terra, power):
    for i in terra:
        for x in i:
            if x <= power:
                power += x
            else:
                break
    return power
