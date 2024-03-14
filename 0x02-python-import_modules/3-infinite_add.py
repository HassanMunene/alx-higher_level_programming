#!/usr/bin/python3
"""
Calculate the sum of all commandline arguments provided
assume that all those commands are strings that can be casted to
integers
"""

if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args)
    if length == 1:
        print("0")
    elif length > 1:
        i = 0
        sum = 0
        for num in args:
            if i > 0:
                sum = sum + int(num)
            i += 1
        print(sum)
