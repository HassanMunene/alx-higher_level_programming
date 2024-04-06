#!/usr/bin/python3

def uppercase(str):
    new_l = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            new_l += chr(ord(char) - 32)
        elif 65 <= ord(char) <= 90:
            new_l += char
        elif ord(char) == 32 or char.isspace():
            new_l += " "
        else:
            new_l += char
    print("{}".format(new_l), end='')
    print()
