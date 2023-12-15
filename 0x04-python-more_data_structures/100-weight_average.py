#!/usr/bin/python3

def weight_average(my_list=[]):

    if not (my_list):
        return 0

    average = 0
    _weight = 0

    for score, _weight in my_list:

        average += score * _weight
        _weight += _weight

        return average / _weight
