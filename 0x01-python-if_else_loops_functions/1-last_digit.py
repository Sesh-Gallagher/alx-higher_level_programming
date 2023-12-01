#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
	last_digit = number % 10
else:
	last_digit = number % -10
if last_digit > 5:
	print("last_digit of {:d} is {:d} and is greater than 5"
	.format(number,last_digit))
elif last_digit != 0 and last_digit < 6:
	print("Last_digit of {:d} is {:d} is not zero and is less than 6"
	.format(number,last_digit))
else:
	print("last_digit of {:d} is 0 abd us 0".format(number))


