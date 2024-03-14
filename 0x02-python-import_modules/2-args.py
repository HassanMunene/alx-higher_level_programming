#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv)

    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        i = 1
        print("{} arguments:".format(length - 1))
        for arg in argv:
            if i < length:
                print("{}: {}".format(i, argv[i]))
                i = i + 1
