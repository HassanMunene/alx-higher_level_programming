#!/usr/bin/python3.8
"""
Here we are importing a compiled python file hidden_4.pyc
we will then investigate this file to print its namespaces
"""
if __name__ == "__main__":
    import hidden_4
    namespaces = dir(hidden_4)
    for name in namespaces:
        if name[:2] != '__':
            print(name)
