#!/user/bin/python3


def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    if roman_string is None:
        return 0

    answer = 0
    """handle edge cases"""
    if "CM" in roman_string:
        answer += 900
        roman_string = roman_string.replace("CM", "")
    if "CD" in roman_string:
        answer += 400
        roman_string = roman_string.replace("CD", "")
    if "XC" in roman_string:
        answer += 90
        roman_string = roman_string.replace("XC", "")
    if "XL" in roman_string:
        answer += 40
        roman_string = roman_string.replace("XL", "")
    if "IX" in roman_string:
        answer += 9
        roman_string = roman_string.replace("IX", "")
    if "IV" in roman_string:
        answer += 4
        roman_string = roman_string.replace("IV", "")

    for i in roman_string:
        if i == "M":
            answer += 1000
        elif i == "D":
            answer += 500
        elif i == "C":
            answer += 100
        elif i == "L":
            answer += 50
        elif i == "X":
            answer += 10
        elif i == "V":
            answer += 5
        elif i == "I":
            answer += 1
    return answer
