#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        sum = 0
        for i in range(x):
            print(f"{my_list[i]}", end="")
            sum += 1
    except IndexError:
        print()
        pass
    else:
        print()
    finally:
        return sum
