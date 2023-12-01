#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    lst_dgt = number % 10
else:
    lst_dgt = number % -10

if lst_dgt > 5:
    print("Last digit of {} is {} and is greater\
            than 5".format(number, lst_dgt))

elif 0 < lst_dgt < 6:
    print("Last digit of {} is {} and is less than 6\
            and not 0".format(number, lst_dgt))

else:
    print("Last digit of {} is 0 and is 0".format(number))
