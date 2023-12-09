#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    orderd_list = list(a_dictionary.keys())
    orderd_list.sort()
    for a in orderd_list:

        print("{}: {}".format(a, a_dictionary.get(a)))
