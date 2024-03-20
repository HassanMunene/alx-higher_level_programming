#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    use the intersection math exp to get elements
    that are different
    """
    diff_set = set_1 ^ set_2
    return diff_set
