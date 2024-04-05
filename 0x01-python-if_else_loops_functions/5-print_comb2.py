#!/usr/bin/python3
for i in range(100):
    if i < 10:
        a, b = hex(i).split('x')
        i = a+b
    elif i == 99:
        print("{}".format(i))
        break
    print("{}, ".format(i), end='')
