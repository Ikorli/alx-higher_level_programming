def magic_calculation(a, b):
    result = a + b if a < b else None
    if result is None:
        raise Exception('a must be less than b')
    return result
