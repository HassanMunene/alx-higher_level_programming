#!/usr/bin/python3
"""
print a text with two new line after
., ? and :
"""


def text_indentation(text):
    """
    splits text to lines along "?", ":", "." followed by 2 new lines
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
