#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    tuple_len = 2

    if lenA < tuple_len or lenB < tuple_len:
        tuple_a = tuple_a + (0, ) *(tuple_len - lenA)
        tuple_b = tuple_b + (0, ) *(tuple_len - lenB)

    if lenA >= tuple_len or lenB >= tuple_b:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]

    a, b = tuple_a
    c, d = tuple_b

    e = a + c
    f = b + d

    new_tuple = e, f
    return new_tuple
