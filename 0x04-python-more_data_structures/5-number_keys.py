#!/usr/bin/python3

def number_keys(a_dictionary):

    list_of_keys = list(a_dictionary.keys())
    rslt = 0

    for a in list_of_keys:
        rslt += 1
    return rslt
