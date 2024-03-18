#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    #if tuple a is empty the it should be (0, 0)
    if lenA < 1:
        tuple_a = 0,0
    elif lenA < 2:
        tuple_a = tuple_a[0], 0
    elif lenA > 2:
        tuple_a = tuple_a[0], tuple_a[1]

    if lenB < 1:
        tuple_b = 0, 0
    elif lenB < 2:
        tuple_b = tuple_b[0], 0
    elif lenB > 2:
        tuple_b = tuple_b[0], tuple_b[1]

    a, b = tuple_a
    c, d = tuple_b

    e = a + c
    f = b + d
    new_tuple = e, f
    return new_tuple
