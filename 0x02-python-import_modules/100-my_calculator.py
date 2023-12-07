#!/usr/bin/python3

if __name__ == '__main__':

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    ops = ({"+": add, "-": sub, "*": mul, "/": div})

    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    b = int(sys.argv[3])
    a = int(sys.argv[1])

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
