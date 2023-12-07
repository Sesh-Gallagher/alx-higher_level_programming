#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num_count = len(sys.argv) - 1
    if num_count == 1:
        print("1 argument.")
    elif num_count == 0:
        print("0 arguments:")
    else:
        print("{} arguments:".format(num_count))
    for a in range(num_count):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
