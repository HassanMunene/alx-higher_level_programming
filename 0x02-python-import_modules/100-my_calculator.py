#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args_len = len(sys.argv)
    if args_len != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    arg_op = sys.argv[2]
    add_op = '+'
    sub_op = '-'
    mul_op = '*'
    div_op = '/'

    if arg_op == add_op:
        print(f'{num1} + {num2} = {add(num1, num2)}')
    elif arg_op == sub_op:
        print(f'{num1} - {num2} = {sub(num1, num2)}')
    elif arg_op == mul_op:
        print(f'{num1} * {num2} = {mul(num1, num2)}')
    elif arg_op == div_op:
        print(f'{num1} / {num2} = {div(num1, num2)}')
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
