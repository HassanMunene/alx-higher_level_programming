#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)

    if str_len == 0:
        first_char = None
    elif str_len >= 1:
        first_char = sentence[0]
    tuple_a = str_len, first_char
    return tuple_a
