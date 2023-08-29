#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(roman_string) - 1, -1, -1):
        intVal = digits[roman_string[i]]
        total += intVal if total < intVal * 5 else -intVal
    return total
