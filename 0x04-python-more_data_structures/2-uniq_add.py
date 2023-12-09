#!/usr/bin/python3

def uniq_add(my_list=[]):

    rslt = 0
    created_list = set(my_list)
    for a in created_list:
        rslt += a

    return rslt
