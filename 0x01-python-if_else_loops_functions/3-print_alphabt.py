#!/usr/bin/python3
for k in range(ord('a'), ord('z') + 1):
    if chr(k) != 'e' and chr(k) != 'q':
        print("{:s}".format(chr(k)), end="")
