#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    total = 0
    roman_values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev_value = 0
    
    for roman in reversed(roman_string):
        int_value = roman_values.get(roman, 0)
        
        if int_value < prev_value:
            total -= int_value
        else:
            total += int_value
        
        prev_value = int_value
    
    return total
