#!/usr/bin/python3

def weight_average(my_list=[]):

    if not (my_list):
        return 0

    _num = 0
    _den = 0

    for tup in (my_list):
        _num += tup[0] * tup[1]
        _den += tup[1]

    return _num / _den
