def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0 or len(list(pin_codes)) != len(set(pin_codes)):
        return False
    for code in pin_codes:
        if not isinstance(code, str) or len(code) != 4 or not code.isdigit():
            return False
    return True
