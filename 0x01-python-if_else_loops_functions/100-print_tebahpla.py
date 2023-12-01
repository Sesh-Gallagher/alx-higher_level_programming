#!/usr/bin/python3

for k in range(ord('z'), ord('a') - 1, -1):

    if k % 2 == 0:
        difference = 0
    else:
        difference = 32
    print('{}'.format(chr(k - difference)), end='')
