#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            print("{} ".format(i), end='')
        elif i % 3 == 0:
            i = "Fizz"
            print("{} ".format(i), end='')
        elif i % 5 == 0:
            i = "Buzz"
            print("{} ".format(i), end='')
        else:
            print("{} ".format(i), end='')
