#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list is None and len(my_list) > 0:

        average = 0
        weight = 0

        for tup in my_list:
            average += tup[0] * tup[1]
            weight += tup[1]

            return (average / weight)

        return 0
