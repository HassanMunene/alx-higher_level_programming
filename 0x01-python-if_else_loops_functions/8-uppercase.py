#!/usr/bin/python3

def uppercase(str):
    new_l = ""
    for l in str:
        if 97 <= ord(l) <= 122:
            new_l += chr(ord(l) - 32)
        elif 65 <= ord(l) <= 90:
            new_l += l
        elif ord(l) == 32 or l.isspace():
            new_l += " "
        else:
            new_l += l
    print("{}".format(new_l), end='')
    print()
