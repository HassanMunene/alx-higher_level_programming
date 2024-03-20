#!/usr/bin/python3


def best_score(a_dictionary):
    best_score = 0
    name = ''
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                name = key
        return name
    else:
        return None
